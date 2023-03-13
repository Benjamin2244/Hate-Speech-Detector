from InputParser import InputParser
from CSVParser import CSVParser
from nltk.corpus import wordnet
import nltk
import requests

class HateSpeechDetector:

    def __init__(self):
        self.input_parser = InputParser()
        self.csv_parser = CSVParser()
        self.THRESHOLD = 0.15
        self.HATE_SPEECH_THRESHOLD = 0.15
        self.POSITIVE_SPEECH_THRESHOLD = 0.15
        self.HAS_INTERNET = False
        self.check_for_internet_connection()
        if self.HAS_INTERNET:
            self.downloads()

    # Downloads wordnet.
    def download_wordnet(self):
        try:
            nltk.data.find('corpora/wordnet')
        except LookupError:
            nltk.download('wordnet', quiet=True)

    # Downloads all the resources needed.
    def downloads(self):
        self.download_wordnet()

    # Changes the HAS_INTERNET variable depending on the internet connection.
    def check_for_internet_connection(self):
        urls = ["https://www.google.co.uk",
                "https://www.amazon.co.uk",
                "https://www.microsoft.com"]
        for url in urls:
            try:
                response = requests.get(url)
                status_code = response.status_code
            except(Exception):
                continue
            if status_code == 200:
                self.HAS_INTERNET = True
                return
            self.HAS_INTERNET = False

    # Returns the average value from the values.
    def getAverageValue(self, values):
        if len(values) == 0:
            return 0
        total = 0
        for value in values:
            total += float(value)
        return total / len(values)

    # Returns the list of values '1' or '-1' corresponding to the given values that reach the threshold past neural.
    def getAbsoluteValues(self, values):
        newValues = []
        for value in values:
            if value > 0 + self.THRESHOLD:
                newValues.append(1)
            elif value < 0 - self.THRESHOLD:
                newValues.append(-1)
        return newValues

    # Returns the synonyms for the word.
    def get_thesaurus_words(self, word):
        similar_words = []
        for synset in wordnet.synsets(word):
            for lemma in synset.lemmas():
                similar_words.append(lemma.name())
        return similar_words

    # Returns the average value for the synonym's of the word.
    def get_backup_average(self, word):
        similar_words = self.get_thesaurus_words(word)
        values = []
        for similar_word in similar_words:
            values += self.csv_parser.get_values(similar_word)
        average = self.getAverageValue(values)
        return average

    # Returns the overall score for the text.
    def get_text_score(self, text, emojis):
        allValues = []
        for word in text:
            values = self.csv_parser.get_values(word)
            average = self.getAverageValue(values)
            if average == 0 and len(values) != 0: # Improve performance by only getting the backup values for words that had a value but they were too neutral.
                average = self.get_backup_average(word)
                if average == 0:
                    continue
            allValues.append(average)
        allValues = self.getAbsoluteValues(allValues)
        allValues = self.addEmojiScore(allValues, emojis)
        average = self.getAverageValue(allValues)
        return average

    def addEmojiScore(self, allValues, emojis):
        for emoji in emojis:
            if emoji == '+':
                allValues.append(1)
            elif emoji == '-':
                allValues.append(-1)
        return allValues

    def isHateSpeech(self, text, emojis):
        score = self.get_text_score(text, emojis)
        return score <= (1 - self.HATE_SPEECH_THRESHOLD)

    def isPositiveSpeech(self, text, emojis):
        score = self.get_text_score(text, emojis)
        return score >= self.POSITIVE_SPEECH_THRESHOLD
