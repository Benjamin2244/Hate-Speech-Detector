from InputParser import InputParser
from TextFileParser import TextFileParser
from CSVParser import CSVParser


class Controller:
    def __init__(self):
        self.input_parser = InputParser()
        self.txt_parser = TextFileParser()
        self.csv_parser = CSVParser()
        self.THRESHOLD = 0.15
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

    def get_text_score(self, text):
        emojis = self.input_parser.getEmojis(text)
        text = self.input_parser.get_clean_text(text)
        allValues = []
        for word in text:
            values = self.csv_parser.get_values(word)
            average = self.getAverageValue(values)
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
        print(allValues)
        return average

Controller()