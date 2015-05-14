import ast
import os

from Bio.Blast.Applications import NcbiblastnCommandline, NcbitblastnCommandline
from Bio.Blast import NCBIXML

from django.shortcuts import render_to_response
from django.template import RequestContext

from blastplus.settings import EVALUE_BLAST_DEFAULT, BLAST_MAX_NUMBER_SEQ_IN_INPUT
from blastplus.settings import EXAMPLE_FASTA_NUCL_FILE_PATH, EXAMPLE_FASTA_PROT_FILE_PATH

from blastplus.forms import BlastForm, TBlastnForm
from blastplus import utils


def blast(request, blast_form, template_init, template_result, blast_commandline, sample_fasta_path, extra_context=None):
    """
    Process blastn/tblastn (blast+) query or set up initial blast form.
    """

    if request.method == 'POST':

        form = blast_form(request.POST)

        if form.is_valid():

            query_file_object_tmp = form.cleaned_data['sequence_in_form']
            evalue = float(form.cleaned_data['evalue_in_form'])
            word_size = int(form.cleaned_data['word_size_in_form'])
            database_path = str(form.cleaned_data['blast_nucl_in_form'])

            standard_opt_dic = {'query': query_file_object_tmp, 'evalue': evalue, 'outfmt': 5, 'db': database_path, 'word_size': word_size}

            # none standard options:
            try:
                matrix = str(form.cleaned_data['matrix_in_form'])
                standard_opt_dic["matrix"] = matrix
            except:
                pass

            sensitivity_opt_dic = ast.literal_eval(str(form.cleaned_data['search_sensitivity_in_form']))

            # standard_opt_dic = {'query': query_file_object_tmp, 'evalue': evalue, 'outfmt': 5, 'db': blastplus_db, "matrix": matrix, 'word_size': word_size}

            blast_records__file_xml = None
            try:
                """
                blast search, parse results from temp file, put them into template for rendering.
                """

                blast_records__file_xml, blast_error = utils.run_blast_commands(blast_commandline, **dict(standard_opt_dic, **sensitivity_opt_dic))

                if len(blast_error) > 0:
                    return render_to_response(template_result, {"blast_record": ''}, context_instance=RequestContext(request))

                else:
                    blast_records = NCBIXML.parse(blast_records__file_xml)

                    # converts blast results into objects and pack into list
                    blast_records_in_object_and_list = utils.blast_records_to_object(list(blast_records))

                    try:
                        '''
                        user defined function to modify blast results
                        e.g. join blast results with external database in template

                        '''
                        if extra_context is not None:
                            blast_records_in_object_and_list = extra_context(blast_records_in_object_and_list)
                    except:
                        pass

                    return render_to_response(template_result,
                                              {'application': blast_records_in_object_and_list[0].application,
                                               'version': blast_records_in_object_and_list[0].version,
                                               'blast_records': blast_records_in_object_and_list, },
                                              context_instance=RequestContext(request))

            finally:
                # remove result - temporary file
                if blast_records__file_xml is not None:
                    os.remove(blast_records__file_xml.name)

    else:
        form = blast_form(initial={'sequence_in_form': '', 'evalue_in_form': EVALUE_BLAST_DEFAULT})

    return render_to_response(template_init, {'form': form, 'sequence_sample_in_fasta': utils.get_sample_data(sample_fasta_path),
                                              "blast_max_number_seq_in_input": BLAST_MAX_NUMBER_SEQ_IN_INPUT,
                                              }, context_instance=RequestContext(request))


def tblastn(request, blast_form=TBlastnForm, template_init='blastplus/blast.html', template_result='blastplus/blast_results.html', extra_context=None):
    return blast(request, blast_form=blast_form, template_init=template_init, template_result=template_result, blast_commandline=NcbitblastnCommandline,
                 sample_fasta_path=EXAMPLE_FASTA_PROT_FILE_PATH, extra_context=extra_context)


def blastn(request, blast_form=BlastForm, template_init='blastplus/blast.html', template_result='blastplus/blast_results.html', extra_context=None):
    return blast(request, blast_form=blast_form, template_init=template_init, template_result=template_result, blast_commandline=NcbiblastnCommandline,
                 sample_fasta_path=EXAMPLE_FASTA_NUCL_FILE_PATH, extra_context=extra_context)
