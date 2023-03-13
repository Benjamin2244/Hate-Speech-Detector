from InputParser import InputParser
from TextFileParser import TextFileParser
from CSVParser import CSVParser
from HateSpeechDetector import HateSpeechDetector
from LGBTQIADetector import LGBTQIADetector
from Python.TestData import TestData
from nltk.corpus import wordnet
import nltk
import requests

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

    def checkList(self, list):
        results = []
        for text in list:
            results.append(self.checkText(text))
        return results

    def getTestResult(self):
        isHateSpeechBool = self.isHateSpeech()
        isLGBTQIASpeechBool = self.isLGBTQIASpeech()
        if isHateSpeechBool and isLGBTQIASpeechBool:
            return 'LGBT_hatespeech'
        elif isHateSpeechBool:
            return 'hatespeech'
        elif isLGBTQIASpeechBool:
            return 'LGBT'
        else:
            return 'none'

    def calcTestResults(self, num):
        targets = []
        results = []
        indexes = []
        testData = self.testData.getTestData()

        totalCount = 0
        testResults = self.testData.getResults()
        for result in testResults:
            if len(result) > 0:
                if result[1] == '-' or result[2] == '-':
                    break
                totalCount += 1
        print(totalCount)
        count = 0
        progress = 0
        min = totalCount
        max = totalCount + num
        for data in testData:
            if count >= min and count < max:
                self.newText(data[0])
                result = self.getTestResult()
                targets.append(data[1])
                results.append(result)
                indexes.append(count)
                progress += 1
                if progress < 250:
                    if progress % 10 == 0:
                        print(progress)
                else:
                    if progress % 50 == 0:
                        print(progress)
            count += 1
        if len(targets) > 0:
            self.testData.addResults(targets, results, indexes)

    def getCorrectLGBTTestResults(self):
        correctCount = 0
        semiCorrectCount = 0
        totalCount = 0
        results = self.testData.getResults()
        for result in results:
            if len(result) > 0:
                if result[1] == '-' or result[2] == '-':
                    continue
                if result[1] == 'LGBT_hatespeech':
                    if result[2] == 'LGBT_hatespeech':
                        correctCount += 1
                        semiCorrectCount += 1
                    elif result[2] == 'hatespeech':
                        semiCorrectCount += 1
                    totalCount += 1
        print('Total: ' + str(totalCount))
        print('Correct: ' + str(correctCount))
        print(correctCount / totalCount)
        print('Semi Correct: ' + str(semiCorrectCount))
        print(semiCorrectCount / totalCount)

    def resetResults(self):
        self.testData.resetResults()

Controller()