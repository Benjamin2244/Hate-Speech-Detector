from controller import Controller
from ResultsManager import ResultsManager


class Interface:

    def __init__(self):
        self.controller = Controller()
        self.resultsManager = ResultsManager(self.controller)
        list_text = [
            '@bellathorne If I see a picture on my iPhone that says Bella follows you will a big smile on my lip :)',
            'iPhone batteries are actually so fucking shitty Been without a phone all day &amp; night',
            'I came home from practice and my mommy brought me Chipotle :-) :-) :-) :-) she so gr8',
            'Your eyes is colorfull like #WarnaWarniGalaxy, that is I falling in love with you :) :) cc. @Samsung_ID',
            'Chale :( jodido iOS 7 en México #iOS7 #ios7mexico #fail #iphone4mexico',
            'iPhone of Samsung - http://t co/501s9dBS3m',
            'Pregnancy : Pregnancy week to weekCategory: Released: Price: 0 http://t co/KITPmwmbM9 - iPhone App'
            ]

        # list_text = [' If I see a picture on my iPhone that says Bella follows you will a big smile on my lip :)',
        #              'iPhone batteries are actually so fucking shitty Been without a BI phone all day &amp; night']

    def activateHateSpeechDetection(self):
        self.controller.isHateSpeechDetector = True

    def deactivateHateSpeechDetection(self):
        self.controller.isHateSpeechDetector = False

    def activateLGBTQIASpeechDetection(self):
        self.controller.isHateSpeechDetector = True

    def deactivateLGBTQIASpeechDetection(self):
        self.controller.isHateSpeechDetector = False

    def checkText(self, text):
        return self.controller.checkText(text)

    def checkList(self, list):
        return self.controller.checkList(list)

    def getTestResults(self):
        print('Correct LGBT Test Results: ')
        self.resultsManager.getCorrectLGBTTestResults()

    def calcTestResults(self, num):
        self.resultsManager.calcTestResults(num)

    def resetTestResults(self):
        self.resultsManager.resetResults()

intereface = Interface()
intereface.resetTestResults()
intereface.calcTestResults(10)
# intereface.calcTestResults(100)
# intereface.calcTestResults(100)
# intereface.calcTestResults(100)
# intereface.calcTestResults(100)
intereface.getTestResults()
# intereface.controller.testData.create_clean_sentiment140()