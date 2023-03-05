import unittest
from CSVParser import CSVParser

class TestCSVParser(unittest.TestCase):

    def test_get_values(self):
        parser = CSVParser()
        values = parser.get_values('unhappy')
        self.assertEqual(values, ['-0.75', '-0.5', '-0.75', '-0.75'])
        values = parser.get_values('unhappy')
        self.assertNotEqual(values, ['-0.75', '-0.5', '-0.75', '-0.75', '0.5'])



