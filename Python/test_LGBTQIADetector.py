import unittest
from LGBTQIADetector import LGBTQIADetector

class TestLGBTQIADetector(unittest.TestCase):

    def setUp(self):
        self.detector = LGBTQIADetector()

    def test_isWordRelated(self):
        word = 'lgbtqia'
        result = self.detector.isWordRelated(word)
        self.assertEqual(result, True)
        word = 'thisisarandomword'
        result = self.detector.isWordRelated(word)
        self.assertEqual(result, False)

    def test_isTextRelated(self):
        text = ['This', 'is', 'related', 'lgbtqia']
        result = self.detector.isTextRelated(text)
        self.assertEqual(result, True)
        text = ['This', 'is', 'not', 'related']
        result = self.detector.isTextRelated(text)
        self.assertEqual(result, False)
