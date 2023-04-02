import unittest
from LGBTQIA_CSV_Parser import LGBTQIACSVParser

class TestLGBTQIACSVParser(unittest.TestCase):

    def setUp(self):
        self.parser = LGBTQIACSVParser()

    def test_isRelated(self):
        result = self.parser.isRelated('thisisarandomword')
        self.assertEqual(result, False)
        result = self.parser.isRelated('lgbtqia')
        self.assertEqual(result, True)

    def test_get_words(self):
        words = self.parser.getWords()
        self.assertTrue(len(words) >= 0)

    def test_get_default_words(self):
        words = self.parser.getDefaultWords()
        self.assertTrue(len(words) >= 0)

    def test_add_and_remove_words(self):
        before = len(self.parser.getWords())
        self.parser.addWord('TestWord')
        after = len(self.parser.getWords())
        self.assertTrue(after > before)
        before = after
        self.parser.removeWord('TestWord')
        after = len(self.parser.getWords())
        self.assertTrue(after < before)
