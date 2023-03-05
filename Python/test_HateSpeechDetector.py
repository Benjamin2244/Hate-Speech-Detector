import unittest
from HateSpeechDetector import HateSpeechDetector

class TestHateSpeechDetector(unittest.TestCase):

    def setUp(self):
        self.detector = HateSpeechDetector()

    def test_getAverageValue(self):
        values = []
        average = self.detector.getAverageValue(values)
        self.assertEqual(average, 0)
        values = ['1', '1']
        average = self.detector.getAverageValue(values)
        self.assertEqual(average, 1)
        values = ['-1', '1']
        average = self.detector.getAverageValue(values)
        self.assertEqual(average, 0)
        values = ['-1', '1', '1']
        average = self.detector.getAverageValue(values)
        self.assertAlmostEqual(average, 0.333, 3)

    def test_getAbsoluteValues(self):
        oldValues = [0, 1, -1, 0.8, -0.8, 0.01, -0.01]
        newValues = self.detector.getAbsoluteValues(oldValues)
        self.assertEqual(newValues, [1, -1, 1, -1])
        oldValues = [0, 1, -1, 0.8, 0.01, -0.01]
        newValues = self.detector.getAbsoluteValues(oldValues)
        self.assertNotEqual(newValues, [1, 1, -1, 1, -1])

    def test_addEmojiScore(self):
        emojiScore = self.detector.addEmojiScore([], ['+', '+', '-', ':('])
        self.assertEqual(emojiScore, [1, 1, -1])