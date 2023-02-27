from InputParser import InputParser
from TextFileParser import TextFileParser
from CSVParser import CSVParser
from nltk.corpus import wordnet
import nltk
import requests

class Controller:
    def __init__(self):
        self.input_parser = InputParser()
        self.txt_parser = TextFileParser()
        self.csv_parser = CSVParser()
        self.THRESHOLD = 0.15
        self.HAS_INTERNET = False
        self.check_for_internet_connection()
        if self.HAS_INTERNET:
            self.downloads()
        list_text = ['@bellathorne If I see a picture on my iPhone that says Bella follows you will get a big smile on my lip :)',
                     'iPhone batteries are actually so fucking shitty Been without a phone all day &amp; night',
                     'I came home from practice and my mommy brought me Chipotle :-) :-) :-) :-) she so gr8',
                     'Your eyes is colorfull like #WarnaWarniGalaxy, that is why I falling in love with you :) :) cc. @Samsung_ID',
                     'Chale :( jodido iOS 7 en México #iOS7 #ios7mexico #fail #iphone4mexico',
                     'iPhone of Samsung - http://t co/501s9dBS3m',
                     'Pregnancy week to week: Pregnancy week to weekCategory: Released: 2013-04-10 04:35:01Price: 0 http://t co/KITPmwmbM9 - iPhone App'
                     ]

        # list_text = ['@bellathorne If I see a picture on my iPhone that says Bella follows you will get a big smile on my lip :)',
        #              'iPhone batteries are actually so fucking shitty Been without a phone all day &amp; night']
        self.print_intro()
        for text in list_text:
            print(text)
            # print(self.txt_parser.get_text_value(text))
            # print(self.txt_parser.get_text_valuev2(text))
            print(self.get_text_score(text))

    def createSWNcsv(self):
        allData = self.txt_parser.getAll()
        self.csv_parser.create_csv_swn(allData)

    def print_intro(self):
        print('This is the introduction page.')

    def getAverageValue(self, values):
        if len(values) == 0:
            return 0
        total = 0
        for value in values:
            total += float(value)
        return total / len(values)

    def getAbsoluteValues(self, values):
        newValues = []
        for value in values:
            if value > 0 + self.THRESHOLD:
                newValues.append(1)
            elif value < 0 - self.THRESHOLD:
                newValues.append(-1)
        return newValues

    def download_wordnet(self):
        try:
            nltk.data.find('corpora/wordnet')
        except LookupError:
            nltk.download('wordnet')

    def downloads(self):
        self.download_wordnet()

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

    def get_thesaurus_words(self, word):
        similar_words = []
        for synset in wordnet.synsets(word):
            for lemma in synset.lemmas():
                similar_words.append(lemma.name())
        return similar_words

    def get_backup_average(self, word):
        similar_words = self.get_thesaurus_words(word)
        values = []
        for similar_word in similar_words:
            values += self.csv_parser.get_values(similar_word)
        average = self.getAverageValue(values)
        return average
    def get_text_score(self, text):
        emojis = self.input_parser.getEmojis(text)
        text = self.input_parser.get_clean_text(text)
        allValues = []
        for word in text:
            values = self.csv_parser.get_values(word)
            average = self.getAverageValue(values)
            if average == 0:
                average = self.get_backup_average(word)
                if average == 0:
                    continue
            allValues.append(average)
        allValues = self.getAbsoluteValues(allValues)
        for emoji in emojis:
            if emoji == '+':
                allValues.append(1)
            elif emoji == '-':
                allValues.append(-1)
        average = self.getAverageValue(allValues)
        return average

Controller()