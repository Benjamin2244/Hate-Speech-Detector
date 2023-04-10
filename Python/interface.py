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

    def resetPositiveSpeechThreshold(self):
        self.controller.reset_POSITIVE_SPEECH_THRESHOLD()

    def resetHateSpeechThreshold(self):
        self.controller.reset_HATE_SPEECH_THRESHOLD()

    # Number must be between 0 and 1.
    # Larger the threshold will classify more extreme texts.
    def change_HATE_SPEECH_THRESHOLD(self, num):
        self.controller.change_HATE_SPEECH_THRESHOLD(num)

    # Number must be between 0 and 1.
    # Larger the threshold will classify more extreme texts.
    def change_POSITIVE_SPEECH_THRESHOLD(self, num):
        self.controller.change_POSITIVE_SPEECH_THRESHOLD(num)

    def reset_WORD_SCORE_THRESHOLD(self):
        self.controller.reset_WORD_SCORE_THRESHOLD()

    # Number must be between 0 and 1.
    # Larger the threshold will only consider more extreme words.
    def change_WORD_SCORE_THRESHOLD(self, num):
        self.controller.change_WORD_SCORE_THRESHOLD(num)

    def get_LGBTQIA_WORDS(self):
        return self.controller.get_LGBTQIA_Words()

    def reset_LGBTQIA_WORDS(self):
        self.controller.reset_LGBTQIA_Words()

    def add_LGBTQIA_Word(self, word):
        self.controller.add_LGBTQIA_Word(word)

    def remove_LGBTQIA_Word(self, word):
        self.controller.remove_LGBTQIA_Word(word)

    # Returns a list of synsets.
    # Each synset is a list with the first element being the value,
    # and the remaining elements are the words.
    def get_SWN_WORDS(self):
        return self.controller.get_SWN_Words()

    def reset_SWN_WORDS(self):
        self.controller.reset_SWN_Words()

    # Give the word to add and the value for the word.
    # Values are between -1 and 1.
    def add_SWN_Word(self, word, score):
        self.controller.add_SWN_Word(word, score)

    def remove_SWN_Word(self, word):
        self.controller.remove_SWN_Word(word)

    def checkText(self, text):
        return self.controller.checkText(text)

    def checkTexts(self, texts):
        return self.controller.checkList(texts)

    def getTestResults(self):
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




# print(interface.checkText('trying to figure this thing out'))
# interface.resetTestResults()
# interface.calcTestResults(10)
interface.getTestResults()
