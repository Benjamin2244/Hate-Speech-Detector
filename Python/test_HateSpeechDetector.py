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
        self.assertEqual(newValues, [1, -1, -1, 1, -1, -1])
        oldValues = [0, 1, -1, 0.8, 0.01, -0.01]
        newValues = self.detector.getAbsoluteValues(oldValues)
        self.assertNotEqual(newValues, [1, 1, -1, -1, 1, -1, -1])

    def test_addEmojiScore(self):
        emojiScore = self.detector.addEmojiScore([], ['+', '+', '-', ':('])
        self.assertEqual(emojiScore, [1, 1, 1, 1, 1, 1, -1, -1, -1])

    def test_reset_hate_speech_threshold(self):
        self.detector.HATE_SPEECH_THRESHOLD = 1000
        self.detector.reset_HATE_SPEECH_THRESHOLD()
        self.assertEqual(self.detector.HATE_SPEECH_THRESHOLD, self.detector.DEFAULT_HATE_SPEECH_THRESHOLD)

    def test_reset_positive_speech_threshold(self):
        self.detector.POSITIVE_SPEECH_THRESHOLD = 1000
        self.detector.reset_POSITIVE_SPEECH_THRESHOLD()
        self.assertEqual(self.detector.POSITIVE_SPEECH_THRESHOLD, self.detector.DEFAULT_POSITIVE_SPEECH_THRESHOLD)

    def test_change_hate_speech_threshold(self):
        self.detector.change_HATE_SPEECH_THRESHOLD(1000)
        self.assertEqual(self.detector.HATE_SPEECH_THRESHOLD, 1000)

    def test_change_positive_speech_threshold(self):
        self.detector.change_POSITIVE_SPEECH_THRESHOLD(1000)
        self.assertEqual(self.detector.POSITIVE_SPEECH_THRESHOLD, 1000)

    def test_reset_word_score_threshold(self):
        self.detector.THRESHOLD = 1000
        self.detector.reset_WORD_SCORE_THRESHOLD()
        self.assertEqual(self.detector.THRESHOLD, self.detector.DEFAULT_THRESHOLD)

    def test_change_word_score_threshold(self):
        self.detector.change_WORD_SCORE_THRESHOLD(1000)
        self.assertEqual(self.detector.THRESHOLD, 1000)

    def test_get_text_score(self):
        score = self.detector.get_text_score(['This', 'is', 'a', 'test'], ['+', '+', '+'])
        self.assertTrue(isinstance(score, float))

    def test_get_backup_average(self):
        average = self.detector.get_backup_average('happy')
        self.assertTrue(isinstance(average, float))

    def test_is_hate_speech(self):
        self.assertTrue(self.detector.isHateSpeech([], ['-', '-', '-']), True)

    def test_is_positive_speech(self):
        self.assertTrue(self.detector.isPositiveSpeech([], ['+', '+', '+']), True)
