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

    # def calcTestResults(self, num):
    #     targets = []
    #     results = []
    #     indexes = []
    #     testData = self.testData.getTestData()
    #
    #     totalCount = 0
    #     testResults = self.testData.getResults()
    #     for result in testResults:
    #         if len(result) > 0:
    #             if result[1] == '-' or result[2] == '-':
    #                 break
    #             totalCount += 1
    #     print(totalCount)
    #     count = 0
    #     progress = 0
    #     min = totalCount
    #     max = totalCount + num
    #     for data in testData:
    #         if count >= min and count < max:
    #             self.newText(data[0])
    #             result = self.getTestResult()
    #             targets.append(data[1])
    #             results.append(result)
    #             indexes.append(count)
    #             progress += 1
    #             if progress < 250:
    #                 if progress % 10 == 0:
    #                     print(progress)
    #             else:
    #                 if progress % 50 == 0:
    #                     print(progress)
    #         count += 1
    #     if len(targets) > 0:
    #         self.testData.addResults(targets, results, indexes)

    def calcNonHateSpeechResults(self, num):
        targets = []
        results = []
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
                    if hatespeech_count < num/2:
                        hatespeech_count += 1
                    elif non_hatespeech_count >= num/2:
                        hatespeech_count += 1
                elif data[1] == 'non_hatespeech':
                    if non_hatespeech_count < num/2:
                        non_hatespeech_count += 1
                    elif hatespeech_count >= num/2:
                        non_hatespeech_count += 1
                else:
                    continue
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
        correctLGBTHatespeech = 0
        correctHatespeech = 0
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
                        correctHatespeech += 1
                    elif result[2] == 'hatespeech':
                        correctHatespeech += 1
                    totalHatespeech += 1
                if result[1] == 'non_hatespeech':
                    if result[2] == 'non_hatespeech':
                        correctPositivespeech += 1
                    totalPositivespeech += 1
        print('Total LGBTQIA+ Hatespeech Tests: ' + str(totalHatespeech))
        print('Correct Hatespeech + LGBTQIA+: ' + str(correctLGBTHatespeech))
        if totalHatespeech > 0:
            print(correctLGBTHatespeech / totalHatespeech)
        else:
            print('0')
        print('Correct Hatespeech: ' + str(correctHatespeech))
        if totalHatespeech > 0:
            print(correctHatespeech / totalHatespeech)
        else:
            print('0')
        print('Total Positive Tests: ' + str(totalPositivespeech))
        print('Correct: ' + str(correctPositivespeech))
        if totalPositivespeech > 0:
            print(correctPositivespeech / totalPositivespeech)
        else:
            print('0')


    def resetResults(self):
        self.testData.resetResults()

Controller()