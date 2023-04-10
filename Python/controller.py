from TextParser import TextParser
from CSVParser import CSVParser
from HateSpeechDetector import HateSpeechDetector
from LGBTQIADetector import LGBTQIADetector
from LGBTQIA_CSV_Parser import LGBTQIACSVParser


class Controller:
    def __init__(self):
        self.input_parser = TextParser()
        self.csv_parser = CSVParser()
        self.lgbtqia_parser = LGBTQIACSVParser()
        self.hate_speech_detector = HateSpeechDetector()
        self.LGBTQIA_detector = LGBTQIADetector()
        self.text = ''
        self.cleanText = []
        self.emojis = []
        self.isHateSpeechDetector = True
        self.isLGBTQIASpeechDetector = True

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

    def reset_POSITIVE_SPEECH_THRESHOLD(self):
        self.hate_speech_detector.reset_POSITIVE_SPEECH_THRESHOLD()

    def reset_HATE_SPEECH_THRESHOLD(self):
        self.hate_speech_detector.reset_HATE_SPEECH_THRESHOLD()

    def change_HATE_SPEECH_THRESHOLD(self, num):
        self.hate_speech_detector.change_HATE_SPEECH_THRESHOLD(num)

    def change_POSITIVE_SPEECH_THRESHOLD(self, num):
        self.hate_speech_detector.change_POSITIVE_SPEECH_THRESHOLD(num)

    def reset_WORD_SCORE_THRESHOLD(self):
        self.hate_speech_detector.reset_WORD_SCORE_THRESHOLD()

    def change_WORD_SCORE_THRESHOLD(self, num):
        self.hate_speech_detector.change_WORD_SCORE_THRESHOLD(num)

    def get_LGBTQIA_Words(self):
        return self.lgbtqia_parser.getWords()

    def reset_LGBTQIA_Words(self):
        self.lgbtqia_parser.resetWords()

    def add_LGBTQIA_Word(self, word):
        self.lgbtqia_parser.addWord(word)

    def remove_LGBTQIA_Word(self, word):
        self.lgbtqia_parser.removeWord(word)

    def get_SWN_Words(self):
        return self.csv_parser.getWords()

    def reset_SWN_Words(self):
        self.csv_parser.resetWords()

    def add_SWN_Word(self, word, score):
        self.csv_parser.addWord(word, score)

    def remove_SWN_Word(self, word):
        self.csv_parser.removeWord(word)

