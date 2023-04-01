from InputParser import InputParser
from TextFileParser import TextFileParser
from CSVParser import CSVParser
from HateSpeechDetector import HateSpeechDetector
from LGBTQIADetector import LGBTQIADetector
from Python.TestData import TestData


class Controller:
    def __init__(self):
        self.input_parser = InputParser()
        self.txt_parser = TextFileParser()
        self.csv_parser = CSVParser()
        self.hate_speech_detector = HateSpeechDetector()
        self.LGBTQIA_detector = LGBTQIADetector()
        self.testData = TestData()
        self.text = ''
        self.cleanText = []
        self.emojis = []
        self.isHateSpeechDetector = True
        self.isLGBTQIASpeechDetector = True
        self.testResults = []

    def isHateSpeech(self):
        return self.hate_speech_detector.isHateSpeech(self.cleanText, self.emojis)

    def isLGBTQIASpeech(self):
        return self.LGBTQIA_detector.isTextRelated(self.cleanText)

    def newText(self, text):
        self.text = text
        self.cleanText = self.input_parser.get_clean_text(self.text)
        self.emojis = self.input_parser.getEmojis(self.text)

    def checkText(self, text):
        isHateSpeech = True
        isLGBTQIASpeech = True
        self.newText(text)
        if self.isHateSpeechDetector:
            isHateSpeech = self.isHateSpeech()
        if self.isLGBTQIASpeechDetector:
            isLGBTQIASpeech = self.isLGBTQIASpeech()
        if isHateSpeech and isLGBTQIASpeech:
            return True
        return False

    def checkList(self, texts):
        results = []
        for text in texts:
            results.append(self.checkText(text))
        return results
