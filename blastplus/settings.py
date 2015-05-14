"""
user defined blastplus app settings file
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# path to nucleotide blastplus database
# BLAST_DB_NUCL = os.path.join(BASE_DIR, 'blastplus/sampledata/sample_db')

# tuple of databases -  to select in form
BLAST_DB_NUCL_CHOICE = ((os.path.join(BASE_DIR, 'blastplus/sampledata/sample_db1/sample_db'), "Sample database 1", ),
                        (os.path.join(BASE_DIR, 'blastplus/sampledata/sample_db2/sample_db2'), "Sample database 2", ),)

# path to example files
EXAMPLE_FASTA_NUCL_FILE_PATH = os.path.join(BASE_DIR, 'blastplus/sampledata/sample_nucl.fasta')
EXAMPLE_FASTA_PROT_FILE_PATH = os.path.join(BASE_DIR, 'blastplus/sampledata/sample_prot.fasta')

# maximum number of query sequences in from
BLAST_MAX_NUMBER_SEQ_IN_INPUT = 10

# forms styling provided from css
BLAST_FORM_ATTRS = {'class': 'blastplus_input_seq_form'}
BLAST_FORM_INPUTTEXT_ATTRS = {'class': 'blastplus_input_textfield_form'}

# scoring Matrix sets
MATRIX_LIST = ['BLOSUM45', 'BLOSUM62', 'BLOSUM80', 'PAM30', 'PAM70']
MATRIX_CHOICE_LIST = list((x, x,) for x in MATRIX_LIST)
MATRIX_DEFAULT = 'BLOSUM62'

# e-value sets
EVALUE_LIST = [1, 0.001, 1e-5, 1e-6, 1e-10, 1e-30, 1e-50, 1e-100]
EVALUE_CHOICE_LIST = list((x, str(x),) for x in list(EVALUE_LIST))
EVALUE_BLAST_DEFAULT = 0.001

# parameters for sensitive blastn search
NUCLEOTIDE_SEARCH_SENSITIVE_CHOICE = (("{'gapopen': 5, 'gapextend': 2, 'penalty': -3, 'reward': 2}", "NORMAL", ),
                                      ("{'penalty': -1, 'word_size': 9,'gapopen': 2, 'gapextend': 1,  'reward': 1, }",
                                       "DISTANT", ),)

# parameters for sensitive tblastn search
PROTEIN_SEARCH_SENSITIVE_CHOICE = (("{'gapopen': 11, 'gapextend': 1}", "NORMAL", ),
                                   ("{'gapopen': 14, 'gapextend': 2, 'matrix': 'BLOSUM45'}", "DISTANT", ),)

# blastn defaults and limits
BLASTN_DEFAULT_INT_WORD_SIZE = 11
BLASTN_MIN_INT_WORD_SIZE = 7
BLASTN_MAX_INT_WORD_SIZE = 50
BLASTN_WORD_SIZE_ERROR = "word size should be between {} and {}".format(BLASTN_MIN_INT_WORD_SIZE,
                                                                        BLASTN_MAX_INT_WORD_SIZE - 1)
# tblastn defaults and limits
TBLASTN_DEFAULT_INT_WORD_SIZE = 3
TBLASTN_MIN_INT_WORD_SIZE = 2
TBLASTN_MAX_INT_WORD_SIZE = 8
TBLASTN_WORD_SIZE_ERROR = "word size should be between {} and {}".format(TBLASTN_MIN_INT_WORD_SIZE,
                                                                         TBLASTN_MAX_INT_WORD_SIZE - 1)

# ERROR massages
BLAST_CORRECT_SEQ_ERROR_MSG = "Please put correct sequence!"
BLAST_CORRECT_SEQ_MAX_SEQ_NUMB_ERROR_MSG = "Too many sequences, maximum is {}".format(BLAST_MAX_NUMBER_SEQ_IN_INPUT)
BLAST_CORRECT_SEQ_TOO_SHORT_ERROR_MSG = "Too short sequence!"
