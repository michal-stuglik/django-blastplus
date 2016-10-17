"""Module with utility functions for blastplus app.   """

import tempfile
import os
from Bio.Application import ApplicationError

from blastplus.features.record import Alignment, BlastRecord, Hsp


def get_sample_data(sample_file):
    """Read and returns sample data to fill form with default sample sequence.  """

    sequence_sample_in_fasta = None
    with open(sample_file) as handle:
        sequence_sample_in_fasta = handle.read()

    return sequence_sample_in_fasta


def blast_records_to_object(blast_records):
    """Transforms biopython's blast record into blast object defined in django-blastplus app.  """

    # container for transformed objects
    blast_objects_list = []

    for blast_record in blast_records:

        br = BlastRecord(**{'query': blast_record.query,
                            'version': blast_record.version,
                            'expect': blast_record.expect,
                            'application': blast_record.application,
                            'reference': blast_record.reference})

        for alignment in blast_record.alignments:

            al = Alignment(**{
                'hit_def': alignment.hit_def,
                'title': alignment.title,
                'length': alignment.length,
            })

            for hsp in alignment.hsps:
                h = Hsp(**{
                    'align_length': hsp.align_length,
                    'bits': hsp.bits,
                    'expect': hsp.expect,
                    'frame': hsp.frame,
                    'gaps': hsp.gaps,
                    'identities': hsp.identities,
                    'match': hsp.match,
                    'num_alignments': hsp.num_alignments,
                    'positives': hsp.positives,
                    'query': hsp.query,
                    'query_end': hsp.query_end,
                    'query_start': hsp.query_start,
                    'sbjct': hsp.sbjct,
                    'sbjct_end': hsp.sbjct_end,
                    'sbjct_start': hsp.sbjct_start,
                    'score': hsp.score,
                    'strand': hsp.strand,
                    'str': str(hsp),
                })

                al.hsp_list.append(h)
            br.alignments.append(al)
        blast_objects_list.append(br)
    return blast_objects_list


def run_blast_commands(ncbicommandline_method, **keywords):
    """Runs blastplus/tblastn search, collects result and pass as a xml temporary file.  """

    # temporary files for output
    blast_out_tmp = tempfile.NamedTemporaryFile(delete=False)
    keywords['out'] = blast_out_tmp.name

    # unpack query temp file object
    query_file_object_tmp = keywords['query']
    keywords['query'] = query_file_object_tmp.name

    stderr = ''
    error_string = ''
    try:
        # formating blastplus command
        blastplusx_cline = ncbicommandline_method(**keywords)
        stdout, stderr = blastplusx_cline()

    except ApplicationError as e:
        error_string = "Runtime error: " + stderr + "\n" + e.cmd

    # remove query temp file
    os.unlink(query_file_object_tmp.name)
    # os.remove(query_file_object_tmp.name)

    return blast_out_tmp, error_string


def get_annotation(db_path, db_list):
    """ Checks if database is set as annotated. """

    annotated = False
    for db in db_list:
        if db["path"] == db_path:
            annotated = db["annotated"]
            break

    return annotated
