import unittest
from TextFileParser import TextFileParser
class TestTextFileParser(unittest.TestCase):

    def setUp(self):
        self.parser = TextFileParser()
        self.text = """a	00001740	0.125	0	able#1	(usually followed by `to') having the necessary means or skill or know-how or authority to do something; "able to swim"; "she was able to program her computer"; "we were at last able to buy a car"; "able to get a grant for the project"""""
        self.cleanText = """0.125 able#1	(usually followed by `to') having the necessary means or skill or know-how or authority to do something; "able to swim"; "she was able to program her computer"; "we were at last able to buy a car"; "able to get a grant for the project"""""

    def test_clean_text(self):
        cleanText = self.parser.remove_pos(self.text)
        self.assertEqual(cleanText,
                         """00001740	0.125	0	able#1	(usually followed by `to') having the necessary means or skill or know-how or authority to do something; "able to swim"; "she was able to program her computer"; "we were at last able to buy a car"; "able to get a grant for the project""""")

    def test_remove_id(self):
        cleanText = self.parser.remove_pos(self.text)
        cleanText = self.parser.remove_id(cleanText)
        self.assertEqual(cleanText,
                         """0.125	0	able#1	(usually followed by `to') having the necessary means or skill or know-how or authority to do something; "able to swim"; "she was able to program her computer"; "we were at last able to buy a car"; "able to get a grant for the project""""")

    def test_remove_neutral(self):
        cleanText = self.parser.remove_pos(self.text)
        cleanText = self.parser.remove_id(cleanText)
        cleanText = self.parser.remove_neutral(cleanText)
        self.assertEqual(cleanText,
                         """0.125 able#1	(usually followed by `to') having the necessary means or skill or know-how or authority to do something; "able to swim"; "she was able to program her computer"; "we were at last able to buy a car"; "able to get a grant for the project""""")
        cleanText = """0	0	able#1	(usually followed by `to') having the necessary means or skill or know-how or authority to do something; "able to swim"; "she was able to program her computer"; "we were at last able to buy a car"; "able to get a grant for the project"""""
        cleanText = self.parser.remove_neutral(cleanText)
        self.assertEqual(cleanText, "")

    def test_get_values(self):
        value = self.parser.get_values(self.cleanText)
        self.assertEqual(value, '0.125')

    def test_get_non_values(self):
        non_value = self.parser.get_non_values(self.cleanText)
        self.assertEqual(non_value, """able#1	(usually followed by `to') having the necessary means or skill or know-how or authority to do something; "able to swim"; "she was able to program her computer"; "we were at last able to buy a car"; "able to get a grant for the project""""")

    def test_get_positive(self):
        cleanText = self.parser.remove_pos(self.text)
        cleanText = self.parser.remove_id(cleanText)
        values = self.parser.get_values(cleanText)
        value = self.parser.get_positive(values)
        self.assertEqual(value, '0.125')

    def test_get_negative(self):
        cleanText = self.parser.remove_pos(self.text)
        cleanText = self.parser.remove_id(cleanText)
        values = self.parser.get_values(cleanText)
        value = self.parser.get_negative(values)
        self.assertEqual(value, '0')

    def test_clean_swn_row(self):
        clean_row = self.parser.clean_swn_row(self.text)
        self.assertEqual(clean_row, '0.125 able')
        clean_row = self.parser.clean_swn_row("""# 0343791 0.125 0 This is random text""")
        self.assertEqual(clean_row, '')


