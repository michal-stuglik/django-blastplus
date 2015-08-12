from django.test import TestCase
from blastplus import settings
from django_webtest import WebTest


class BlastTestCase(TestCase):

    def test_blast(self):
        resp = self.client.get('/blastn/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('form' in resp.context)
        self.assertIsNotNone(resp.context['form'])
        self.assertTrue('sequence_sample_in_fasta' in resp.context)


class BlastnCase(WebTest):

    def test_blastn_initials(self):
        form = self.app.get('/blastn/').form
        self.assertEqual(form['blast_db_in_form'].value, settings.BLAST_DB_NUCL_CHOICE[0][0])
        self.assertEqual(form['search_sensitivity_in_form'].value, settings.NUCLEOTIDE_SEARCH_SENSITIVE_CHOICE[0][0])
        self.assertEqual(form['word_size_in_form'].value, u'%s' % settings.BLASTN_SETS.default_word_size)
        self.assertEqual(form['evalue_in_form'].value, u'%s' % settings.EVALUE_BLAST_DEFAULT)
        self.assertEqual(form['sequence_in_form'].value, u'')
