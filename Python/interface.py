from controller import Controller
from ResultsManager import ResultsManager


class Interface:

    def __init__(self):
        self.controller = Controller()
        self.resultsManager = ResultsManager(self.controller)

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

    def checkTexts(self, texts):
        return self.controller.checkList(texts)

    def getTestResults(self):
        print('Correct LGBT Test Results: ')
        self.resultsManager.getCorrectLGBTTestResults()

    def calcTestResults(self, num):
        self.resultsManager.calcTestResults(num)

    def resetTestResults(self):
        self.resultsManager.resetResults()


# Examples on how to use the program.

interface = Interface()

# print(interface.checkText('This is a example of text.'))
# print(interface.checkTexts(['This is an example', 'of multiple texts', 'being tested at once.']))

# interface.resetTestResults()
# interface.calcTestResults(20)
# interface.getTestResults()


# interface.resetTestResults()
# interface.calcTestResults(100)
# interface.calcTestResults(100)
# interface.calcTestResults(100)
# interface.calcTestResults(100)
# interface.calcTestResults(100)
# interface.getTestResults()
