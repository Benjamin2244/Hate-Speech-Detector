import unittest
from CSVParser import CSVParser

class TestCSVParser(unittest.TestCase):

    def setUp(self):
        self.parser = CSVParser()

    def test_get_values(self):
        values = self.parser.get_values('unhappy')
        self.assertEqual(values, ['-0.75', '-0.5', '-0.75', '-0.75'])
        values = self.parser.get_values('unhappy')
        self.assertNotEqual(values, ['-0.75', '-0.5', '-0.75', '-0.75', '0.5'])

    def test_get_words(self):
        words = self.parser.getWords()
        self.assertTrue(len(words) >= 0)

    def test_add_and_remove_words(self):
        before = len(self.parser.getWords())
        self.parser.addWord('TestWord', 0)
        after = len(self.parser.getWords())
        self.assertTrue(after > before)
        before = after
        self.parser.removeWord('TestWord')
        after = len(self.parser.getWords())
        self.assertTrue(after < before)
