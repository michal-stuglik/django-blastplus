from django.test import TestCase
from django_webtest import WebTest

from blastplus import settings


class BlastTestCase(TestCase):
    def test_blastn(self):
        resp = self.client.get('/blastn/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('form' in resp.context)
        self.assertIsNotNone(resp.context['form'])
        self.assertTrue('sequence_sample_in_fasta' in resp.context)

    def test_tblastn(self):
        resp = self.client.get('/tblastn/')
        self.assertEqual(resp.status_code, 200)

    def test_blastp(self):
        resp = self.client.get('/blastp/')
        self.assertEqual(resp.status_code, 200)

    def test_blastx(self):
        resp = self.client.get('/blastx/')
        self.assertEqual(resp.status_code, 200)


class BlastnCase(WebTest):
    def test_blastn_initials(self):
        form = self.app.get('/blastn/').form
        self.assertEqual(form['blast_db_in_form'].value, settings.BLAST_DB_NUCL_CHOICE[0][0])
        self.assertEqual(form['search_sensitivity_in_form'].value, settings.NUCLEOTIDE_SEARCH_SENSITIVE_CHOICE[0][0])
        self.assertEqual(form['word_size_in_form'].value, u'%s' % settings.BLASTN_SETS.default_word_size)
        self.assertEqual(form['evalue_in_form'].value, u'%s' % settings.EVALUE_BLAST_DEFAULT)
        self.assertEqual(form['sequence_in_form'].value, u'')

    def test_blastn_behave(self):
        req = self.app.post('/blastn/')
        self.assertIsNotNone(req)
        self.assertIsNotNone(req.context['form'])
