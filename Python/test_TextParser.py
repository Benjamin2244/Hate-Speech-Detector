import unittest
from TextParser import TextParser

class TestTextParser(unittest.TestCase):
    def setUp(self):
        self.parser = TextParser()

    def test_get_word(self):
        word = self.parser.get_word('This is test text', 8, 12)
        self.assertEqual(word, 'test')
        self.assertNotEqual(word, 'text')

    def test_remove_non_letters(self):
        word = self.parser.remove_non_letters('This@That123$')
        self.assertEqual(word, 'ThisThat')

    def test_to_lowercase(self):
        text = self.parser.to_lowercase('UPPERCASE')
        self.assertEqual(text, 'uppercase')

    def test_get_clean_text(self):
        clean_text = self.parser.get_clean_text('ThiS_ iS%  1DirTY£')
        self.assertEqual(clean_text, ['this', 'is', 'dirty'])

    def test_getEmojis(self):
        text = 'Some :) emojis are :( here :o'
        results = self.parser.getEmojis(text)
        self.assertEqual(results, ['+', '-', '-'])