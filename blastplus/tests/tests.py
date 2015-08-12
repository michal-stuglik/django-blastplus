from django.test import TestCase

import tempfile
import os
from blastplus import utils
from blastplus.settings import SAMPLE_DIR
from Bio.Blast import NCBIXML


class UtilsTestCase(TestCase):
    def setUp(self):
        self.fastfile = tempfile.NamedTemporaryFile(delete=False)

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
        self.assertTrue(len(brs) > 0)

        # TODO: more tests on blast__record
