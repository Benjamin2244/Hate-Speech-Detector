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
            return 'LGBT_non_hatespeech'
        else:
            return 'non_hatespeech'

    def calcTestResults(self, num):
        targets = []
        results = []
        texts = []
        indexes = []
        hatespeech_count = 0
        non_hatespeech_count = 0
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
                if data[1] == 'LGBT_hatespeech':
                    if hatespeech_count < num / 2:
                        hatespeech_count += 1
                    elif non_hatespeech_count >= num / 2:
                        hatespeech_count += 1
                    else:
                        continue
                elif data[1] == 'non_hatespeech':
                    if non_hatespeech_count < num / 2:
                        non_hatespeech_count += 1
                    elif hatespeech_count >= num / 2:
                        non_hatespeech_count += 1
                    else:
                        continue
                else:
                    continue
                self.newText(data[0])
                result = self.getTestResult()
                targets.append(data[1])
                results.append(result)
                indexes.append(count)
                texts.append(self.text)
                progress += 1
                if progress < 250:
                    if progress % 10 == 0:
                        print(progress)
                else:
                    if progress % 50 == 0:
                        print(progress)
            count += 1
        if len(targets) > 0:
            self.testData.addResults(targets, results, texts, indexes)

    ### TODO Create class that contains results data
    ### Create the class with the results data passed into
    def getCorrectLGBTTestResults(self):
        correctLGBTHatespeech = 0
        correctHatespeech = 0
        correctLGBT = 0
        totalHatespeech = 0
        correctPositivespeech = 0
        totalPositivespeech = 0
        results = self.testData.getResults()
        for result in results:
            if len(result) > 0:
                if result[1] == '-' or result[2] == '-':
                    continue
                if result[1] == 'LGBT_hatespeech':
                    if result[2] == 'LGBT_hatespeech':
                        correctLGBTHatespeech += 1
                        correctLGBT += 1
                        correctHatespeech += 1
                    elif result[2] == 'hatespeech':
                        correctHatespeech += 1
                    elif result[2] == 'LGBT_non_hatespeech':
                        correctLGBT += 1
                    totalHatespeech += 1
                if result[1] == 'non_hatespeech':
                    if result[2] == 'non_hatespeech':
                        correctPositivespeech += 1
                    totalPositivespeech += 1
        print('Total LGBTQIA+ Hatespeech Tests: ' + str(totalHatespeech))

        correctLGBTHatespeechRate = 0
        if totalHatespeech > 0:
            correctLGBTHatespeechRate = (correctLGBTHatespeech / totalHatespeech) * 100
        print('Correct Hatespeech + LGBTQIA+: ' + str(correctLGBTHatespeech) + ', ' + str(correctLGBTHatespeechRate) + ' %')

        correctHatespeechRate = 0
        if totalHatespeech > 0:
            correctHatespeechRate = (correctHatespeech / totalHatespeech) * 100
        print('Correct Hatespeech: ' + str(correctHatespeech) + ', ' + str(correctHatespeechRate) + ' %')

        correctLGBTRate = 0
        if totalHatespeech > 0:
            correctLGBTRate = (correctLGBT / totalHatespeech) * 100
        print('Correct LGBTQIA+ detection: ' + str(correctLGBT) + ', ' + str(correctLGBTRate) + ' %')

        print('Total Positive Tests: ' + str(totalPositivespeech))
        correctPositivespeechRate = 0
        if totalPositivespeech > 0:
            correctPositivespeechRate = (correctPositivespeech / totalPositivespeech) * 100
        print('Correct: ' + str(correctPositivespeech) + ', ' + str(correctPositivespeechRate) + ' %')



    def resetResults(self):
        self.testData.resetResults()

Controller()