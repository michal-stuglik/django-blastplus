import os
import tempfile

from Bio.Blast import NCBIXML
from django.test import TestCase

from blastplus import utils
from blastplus.features import record
from blastplus.settings import SAMPLE_DIR


class UtilsTestCase(TestCase):
    def setUp(self):
        self.fastfile = tempfile.NamedTemporaryFile(mode="w+", delete=False)

        self.fastfile.write(">seq1\n")
        self.fastfile.write("AAACCCGGG\n")
        self.fastfile.close()

        self.blast_out = os.path.join(SAMPLE_DIR, 'blast.xml')

    def tearDown(self):
        os.unlink(self.fastfile.name)

    def test_get_sample_data(self):
        with open(self.fastfile.name) as f:
            self.assertEquals(utils.get_sample_data(self.fastfile.name), f.read())

    def test_blast_records_to_object(self):
        brs = utils.blast_records_to_object(list(NCBIXML.parse(open(self.blast_out))))
        self.assertTrue(len(brs) == 1)


class FeatureRecordTestCase(TestCase):
    def setUp(self):
        self.hsp = record.Hsp(
            **dict(sbjct_end=203, sbjct=u'TTTGGAGCCTGAGCAGGA', bits=35.5503, frame=(1, -1),
                   query_end=19, score=38.0, gaps=0, expect=0.0122843, str='Score 38 (35 bits), expectation 1.2e-02',
                   positives=19, sbjct_start=221, query=u'TTTGGAGCCTGAGCAGGA',
                   align_length=19, num_alignments=None, identities=19,
                   query_start=1, strand=(None, None), match=u'||||||||||||||||||'))
        self.limit_length = 9

        self.alignment = record.Alignment(
            **dict(hit_def='hit_def', title='title', length=self.hsp.align_length))
        self.alignment.hsp_list.append(self.hsp)

    def tearDown(self):
        del self.hsp
        del self.alignment

    def test_hsp(self):
        self.assertIsInstance(self.hsp, record.Hsp)
        self.assertTrue(self.hsp.chop_sequence("AACC", 2), ['AA', 'CC'])
        self.assertTrue(self.hsp.chop_query(), ['TTTGGAGCC', 'TGAGCAGGA'])

    def test_alignment(self):
        self.assertIsInstance(self.alignment, record.Alignment)
        self.assertEqual(self.alignment.best_evalue(), self.hsp.expect)
        self.assertEqual(self.alignment.best_identities(), 100.0)
