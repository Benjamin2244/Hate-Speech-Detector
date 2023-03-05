import unittest
from LGBTQIA_CSV_Parser import LGBTQIACSVParser

class TestLGBTQIACSVParser(unittest.TestCase):

    def test_isRelated(self):
        parser = LGBTQIACSVParser()
        result = parser.isRelated('thisisarandomword')
        self.assertEqual(result, False)
        result = parser.isRelated('lgbtqia')
        self.assertEqual(result, True)
