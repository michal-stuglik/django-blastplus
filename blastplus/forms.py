"""
Module with forms to blastplus search and validation functions.
"""

import tempfile

from Bio import SeqIO
from Bio.Alphabet.IUPAC import IUPACAmbiguousDNA
from Bio.Alphabet.IUPAC import IUPACProtein
from django import forms

from blastplus import settings as blast_settings

ALLOWED_NUCL = set(IUPACAmbiguousDNA.letters)
ALLOWED_AMINOACIDS = set(IUPACProtein.letters)


class BlastForm(forms.Form):
    """Form used for blastn search following validation input sequence.  """

    sequence_in_form = forms.CharField(widget=forms.Textarea(blast_settings.BLAST_FORM_ATTRS), label="sequence")
    evalue_in_form = forms.ChoiceField(widget=forms.Select, choices=blast_settings.EVALUE_CHOICE_LIST, label="e-value")
    word_size_in_form = forms.CharField(widget=forms.TextInput(blast_settings.BLAST_FORM_INPUTTEXT_ATTRS),
                                        initial=blast_settings.BLASTN_SETS.default_word_size, label="word size")
    search_sensitivity_in_form = forms.ChoiceField(widget=forms.Select,
                                                   choices=blast_settings.NUCLEOTIDE_SEARCH_SENSITIVE_CHOICE,
                                                   label="sensitivity")
    blast_db_in_form = forms.ChoiceField(widget=forms.Select, choices=blast_settings.BLAST_DB_NUCL_CHOICE,
                                         label="Database")

    def clean_sequence_in_form(self):
        sequence_in_form = self.cleaned_data['sequence_in_form']

        return validate_sequence(sequence_in_form, sequence_is_as_nucleotide=True)

    def clean_word_size_in_form(self):
        word_size_in_form = self.cleaned_data['word_size_in_form']
        return validate_word_size(word_size_in_form, blast_settings.BLASTN_SETS)


class TBlastnForm(forms.Form):
    """Form used for tblastn search following validation input sequence.  """

    sequence_in_form = forms.CharField(widget=forms.Textarea(blast_settings.BLAST_FORM_ATTRS), label="sequence")
    evalue_in_form = forms.ChoiceField(widget=forms.Select, choices=blast_settings.EVALUE_CHOICE_LIST, label="e-value")
    matrix_in_form = forms.ChoiceField(widget=forms.Select, choices=blast_settings.MATRIX_CHOICE_LIST,
                                       initial=blast_settings.MATRIX_DEFAULT, label="matrix")
    word_size_in_form = forms.CharField(widget=forms.TextInput(blast_settings.BLAST_FORM_INPUTTEXT_ATTRS),
                                        initial=blast_settings.TBLASTN_SETS.default_word_size, label="word size")
    search_sensitivity_in_form = forms.ChoiceField(widget=forms.Select,
                                                   choices=blast_settings.PROTEIN_SEARCH_SENSITIVE_CHOICE,
                                                   label="sensitivity")
    blast_db_in_form = forms.ChoiceField(widget=forms.Select, choices=blast_settings.BLAST_DB_NUCL_CHOICE,
                                         label="Database")

    def clean_sequence_in_form(self):
        sequence_in_form = self.cleaned_data['sequence_in_form']
        return validate_sequence(sequence_in_form, sequence_is_as_nucleotide=False)

    def clean_word_size_in_form(self):
        word_size_in_form = self.cleaned_data['word_size_in_form']
        return validate_word_size(word_size_in_form, blast_settings.TBLASTN_SETS)


class BlastpForm(forms.Form):
    """Form used for blastp search following validation input sequence.  """

    sequence_in_form = forms.CharField(widget=forms.Textarea(blast_settings.BLAST_FORM_ATTRS), label="sequence")
    evalue_in_form = forms.ChoiceField(widget=forms.Select, choices=blast_settings.EVALUE_CHOICE_LIST, label="e-value")
    matrix_in_form = forms.ChoiceField(widget=forms.Select, choices=blast_settings.MATRIX_CHOICE_LIST,
                                       initial=blast_settings.MATRIX_DEFAULT, label="matrix")
    word_size_in_form = forms.CharField(widget=forms.TextInput(blast_settings.BLAST_FORM_INPUTTEXT_ATTRS),
                                        initial=blast_settings.BLASTP_SETS.default_word_size, label="word size")
    search_sensitivity_in_form = forms.ChoiceField(widget=forms.Select,
                                                   choices=blast_settings.PROTEIN_SEARCH_SENSITIVE_CHOICE,
                                                   label="sensitivity")
    blast_db_in_form = forms.ChoiceField(widget=forms.Select, choices=blast_settings.BLAST_DB_PROT_CHOICE,
                                         label="Database")

    def clean_sequence_in_form(self):
        sequence_in_form = self.cleaned_data['sequence_in_form']
        return validate_sequence(sequence_in_form, sequence_is_as_nucleotide=False)

    def clean_word_size_in_form(self):
        word_size_in_form = self.cleaned_data['word_size_in_form']
        return validate_word_size(word_size_in_form, blast_settings.BLASTP_SETS)


class BlastxForm(forms.Form):
    """Form used for blastx search following validation input sequence.  """

    sequence_in_form = forms.CharField(widget=forms.Textarea(blast_settings.BLAST_FORM_ATTRS), label="sequence")
    evalue_in_form = forms.ChoiceField(widget=forms.Select, choices=blast_settings.EVALUE_CHOICE_LIST, label="e-value")
    matrix_in_form = forms.ChoiceField(widget=forms.Select, choices=blast_settings.MATRIX_CHOICE_LIST,
                                       initial=blast_settings.MATRIX_DEFAULT, label="matrix")
    word_size_in_form = forms.CharField(widget=forms.TextInput(blast_settings.BLAST_FORM_INPUTTEXT_ATTRS),
                                        initial=blast_settings.BLASTX_SETS.default_word_size, label="word size")
    search_sensitivity_in_form = forms.ChoiceField(widget=forms.Select,
                                                   choices=blast_settings.PROTEIN_SEARCH_SENSITIVE_CHOICE,
                                                   label="sensitivity")
    blast_db_in_form = forms.ChoiceField(widget=forms.Select, choices=blast_settings.BLAST_DB_PROT_CHOICE,
                                         label="Database")

    def clean_sequence_in_form(self):
        sequence_in_form = self.cleaned_data['sequence_in_form']
        return validate_sequence(sequence_in_form, sequence_is_as_nucleotide=True)

    def clean_word_size_in_form(self):
        word_size_in_form = self.cleaned_data['word_size_in_form']
        return validate_word_size(word_size_in_form, blast_settings.BLASTX_SETS)


def validate_word_size(word_size, BLAST_SETS):
    """Validate word size in blast/tblastn form.  """

    blast_min_int_word_size = BLAST_SETS.min_word_size
    blast_max_int_word_size = BLAST_SETS.max_word_size
    blast_word_size_error = BLAST_SETS.get_word_size_error()

    try:
        if len(word_size) <= 0:
            raise forms.ValidationError(blast_word_size_error)

        int_word_size = int(word_size)

        if int_word_size < blast_min_int_word_size:
            raise forms.ValidationError(blast_word_size_error)

        if int_word_size >= blast_max_int_word_size:
            raise forms.ValidationError(blast_word_size_error)

    except:
        raise forms.ValidationError(blast_word_size_error)

    return int_word_size


def validate_sequence(sequence: str, sequence_is_as_nucleotide=True):
    """Validate sequence in blast/tblastn form.  """

    tmp_seq = tempfile.NamedTemporaryFile(mode="wb+", delete=False)

    if len(str(sequence).strip()) == 0:
        raise forms.ValidationError(blast_settings.BLAST_CORRECT_SEQ_ERROR_MSG)

    if str(sequence).strip()[0] != ">":
        tmp_seq.write(">seq1\n".encode())

    tmp_seq.write(sequence.encode())
    tmp_seq.close()

    records = SeqIO.index(tmp_seq.name, "fasta")
    record_count = len(records)

    if record_count == 0:
        raise forms.ValidationError(blast_settings.BLAST_CORRECT_SEQ_ERROR_MSG)

    if record_count > blast_settings.BLAST_MAX_NUMBER_SEQ_IN_INPUT:
        raise forms.ValidationError(blast_settings.BLAST_CORRECT_SEQ_MAX_SEQ_NUMB_ERROR_MSG)

    # read query sequence from temporary file
    first_sequence_list_in_file = SeqIO.parse(tmp_seq.name, "fasta")

    for sequence in first_sequence_list_in_file:

        if len(sequence.seq) <= 10:
            raise forms.ValidationError(blast_settings.BLAST_CORRECT_SEQ_TOO_SHORT_ERROR_MSG)

        if sequence_is_as_nucleotide:
            check_allowed_letters(str(sequence.seq), ALLOWED_NUCL)
        else:
            check_allowed_letters(str(sequence.seq), ALLOWED_AMINOACIDS)

    return tmp_seq


def check_allowed_letters(seq, allowed_letters_as_set):
    """Validate sequence: Rise an error if sequence contains undesirable letters.  """

    # set of unique letters in sequence
    seq_set = set(seq)

    not_allowed_letters_in_seq = [x for x in seq_set if str(x).upper() not in allowed_letters_as_set]

    if len(not_allowed_letters_in_seq) > 0:
        raise forms.ValidationError(
            "This sequence type cannot contain letters: " + ", ".join(not_allowed_letters_in_seq))
