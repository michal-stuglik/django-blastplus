import ast
import os

from Bio.Blast import NCBIXML
from Bio.Blast.Applications import NcbiblastnCommandline, NcbitblastnCommandline, NcbiblastpCommandline, \
    NcbiblastxCommandline
from django.shortcuts import render

from blastplus import utils
from blastplus.forms import BlastForm, TBlastnForm, BlastpForm, BlastxForm
from blastplus.settings import BLAST_CORRECT_PARAMS
from blastplus.settings import EVALUE_BLAST_DEFAULT, BLAST_MAX_NUMBER_SEQ_IN_INPUT
from blastplus.settings import EXAMPLE_FASTA_NUCL_FILE_PATH, EXAMPLE_FASTA_PROT_FILE_PATH
from blastplus.settings import BLAST_DB_NUCL_LIST


def blast(request, blast_form, template_init, template_result, blast_commandline, sample_fasta_path,
          extra_context=None):
    """
    Process blastn/tblastn (blast+) query or set up initial blast form.
    """

    if request.method == 'POST':

        form = blast_form(request.POST)

        if form.is_valid():

            query_file_object_tmp = form.cleaned_data['sequence_in_form']
            evalue = float(form.cleaned_data['evalue_in_form'])
            word_size = int(form.cleaned_data['word_size_in_form'])
            database_path = str(form.cleaned_data['blast_db_in_form'])

            standard_opt_dic = {'query': query_file_object_tmp, 'evalue': evalue, 'outfmt': 5, 'db': database_path,
                                'word_size': word_size}
            annotated = utils.get_annotation(database_path, BLAST_DB_NUCL_LIST)

            # none standard options:
            try:
                matrix = str(form.cleaned_data['matrix_in_form'])
                standard_opt_dic["matrix"] = matrix
            except:
                pass

            sensitivity_opt_dic = ast.literal_eval(str(form.cleaned_data['search_sensitivity_in_form']))

            blast_records__file_xml = None
            try:

                # blast search, parse results from temp file, put them into template for rendering.
                blast_records__file_xml, blast_error = utils.run_blast_commands(blast_commandline,
                                                                                **dict(standard_opt_dic,
                                                                                       **sensitivity_opt_dic))

                if len(blast_error) > 0:
                    return render(request=request, template_name=template_result,
                                  context={"blast_record": '', blast_error: BLAST_CORRECT_PARAMS})

                else:

                    # converts blast results into objects and pack into list
                    blast_records_in_object_and_list = utils.blast_records_to_object(
                        list(NCBIXML.parse(blast_records__file_xml)))

                    # user defined function to modify blast results
                    # e.g. join blast results with external database in template
                    if extra_context is not None:
                        blast_records_in_object_and_list = extra_context(blast_records_in_object_and_list)

                    return render(request=request, template_name=template_result,
                                  context={'application': blast_records_in_object_and_list[0].application,
                                           'version': blast_records_in_object_and_list[0].version,
                                           'blast_records': blast_records_in_object_and_list,
                                           'annotated': annotated})

            finally:
                # remove result - temporary file
                if blast_records__file_xml is not None:
                    os.remove(blast_records__file_xml.name)

    else:
        form = blast_form(initial={'sequence_in_form': '', 'evalue_in_form': EVALUE_BLAST_DEFAULT})

    return render(request=request, template_name=template_init,
                  context={'form': form, 'sequence_sample_in_fasta': utils.get_sample_data(sample_fasta_path),
                           "blast_max_number_seq_in_input": BLAST_MAX_NUMBER_SEQ_IN_INPUT, })


def tblastn(request, blast_form=TBlastnForm, template_init='blastplus/blast.html',
            template_result='blastplus/blast_results.html', extra_context=None):
    return blast(request, blast_form=blast_form, template_init=template_init, template_result=template_result,
                 blast_commandline=NcbitblastnCommandline, sample_fasta_path=EXAMPLE_FASTA_PROT_FILE_PATH,
                 extra_context=extra_context)


def blastn(request, blast_form=BlastForm, template_init='blastplus/blast.html',
           template_result='blastplus/blast_results.html', extra_context=None):
    return blast(request, blast_form=blast_form, template_init=template_init, template_result=template_result,
                 blast_commandline=NcbiblastnCommandline, sample_fasta_path=EXAMPLE_FASTA_NUCL_FILE_PATH,
                 extra_context=extra_context)


def blastp(request, blast_form=BlastpForm, template_init='blastplus/blast.html',
           template_result='blastplus/blast_results.html', extra_context=None):
    return blast(request, blast_form=blast_form, template_init=template_init, template_result=template_result,
                 blast_commandline=NcbiblastpCommandline, sample_fasta_path=EXAMPLE_FASTA_PROT_FILE_PATH,
                 extra_context=extra_context)


def blastx(request, blast_form=BlastxForm, template_init='blastplus/blast.html',
           template_result='blastplus/blast_results.html', extra_context=None):
    return blast(request, blast_form=blast_form, template_init=template_init, template_result=template_result,
                 blast_commandline=NcbiblastxCommandline, sample_fasta_path=EXAMPLE_FASTA_NUCL_FILE_PATH,
                 extra_context=extra_context)
