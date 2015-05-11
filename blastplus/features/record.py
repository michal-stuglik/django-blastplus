"""
Module with biopython-like classes to keep & process results from blast analysis.
"""


class Hsp(object):
    """Store and process HSP object from blast local search.  """

    def __init__(self, *args, **kwargs):
        self.limit_length = 80

        self.align_length = kwargs['align_length']
        self.bits = round(kwargs['bits'], 1)
        self.expect = kwargs['expect']
        self.frame = kwargs['frame']
        self.gaps = kwargs['gaps']
        self.identities = kwargs['identities']
        self.match = kwargs['match']
        self.num_alignments = kwargs['num_alignments']
        self.positives = kwargs['positives']
        self.query = kwargs['query']
        self.query_end = kwargs['query_end']
        self.query_start = kwargs['query_start']
        self.sbjct = kwargs['sbjct']
        self.sbjct_end = kwargs['sbjct_end']
        self.sbjct_start = kwargs['sbjct_start']
        self.score = kwargs['score']
        self.strand = kwargs['strand']
        self.str = kwargs['str']

    @staticmethod
    def chop_sequence(sequence, limit_length):
        """Input sequence is divided on smaller non-overlapping sequences with set length.  """
        return [sequence[i:i + limit_length] for i in range(0, len(sequence), limit_length)]

    def chop_query(self):
        """Query sequence is divided on smaller non-overlapping sequences with set length.  """
        return self.chop_sequence(self.query, self.limit_length)

    def chop_match(self):
        """Match sequence is divided on smaller non-overlapping sequences with set length.  """
        return self.chop_sequence(self.match, self.limit_length)

    def chop_sbjct(self):
        """Subject sequence is divided on smaller non-overlapping sequences with set length.  """
        return self.chop_sequence(self.sbjct, self.limit_length)


class Alignment(object):
    """Store and process alignment object from blast local search.  """

    def __init__(self, **kwargs):
        self.hit_def = kwargs['hit_def']
        self.title = kwargs['title']
        self.length = kwargs['length']
        self.hsp_list = []
        self.hit_url = ""
        self.hit_protein_name = ""

    def best_evalue(self):
        """Returns e-value of the best HSP in alignment.  """
        if len(self.hsp_list) > 0:
            return self.hsp_list[0].expect

    def best_score(self):
        """Returns score of the best HSP in alignment.  """
        if len(self.hsp_list) > 0:
            return self.hsp_list[0].score

    def best_identities(self):
        """Returns identities of the best HSP in alignment.  """
        if len(self.hsp_list) > 0:
            return round(float(self.hsp_list[0].identities) / float(self.hsp_list[0].align_length) * 100, 1)

    def get_id(self):
        """Returns unique id of an alignment.  """
        return hash(str(self.title) + str(self.best_score()) + str(self.hit_def))


class BlastRecord(object):
    """Store a single blast record from blast local search.  """

    def __init__(self, **kwargs):
        self.query = kwargs['query']
        self.version = kwargs['version']
        self.expect = kwargs['expect']
        self.application = kwargs['application']
        self.reference = kwargs['reference']
        self.alignments = []
