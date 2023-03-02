from InputParser import InputParser
from TextFileParser import TextFileParser
from CSVParser import CSVParser
from HateSpeechDetector import HateSpeechDetector
from nltk.corpus import wordnet
import nltk
import requests

class Controller:
    def __init__(self):
        self.input_parser = InputParser()
        self.txt_parser = TextFileParser()
        self.csv_parser = CSVParser()
        self.hate_speech_detector = HateSpeechDetector()
        list_text = ['@bellathorne If I see a picture on my iPhone that says Bella follows you will get a big smile on my lip :)',
                     'iPhone batteries are actually so fucking shitty Been without a phone all day &amp; night',
                     'I came home from practice and my mommy brought me Chipotle :-) :-) :-) :-) she so gr8',
                     'Your eyes is colorfull like #WarnaWarniGalaxy, that is why I falling in love with you :) :) cc. @Samsung_ID',
                     'Chale :( jodido iOS 7 en México #iOS7 #ios7mexico #fail #iphone4mexico',
                     'iPhone of Samsung - http://t co/501s9dBS3m',
                     'Pregnancy week to week: Pregnancy week to weekCategory: Released: 2013-04-10 04:35:01Price: 0 http://t co/KITPmwmbM9 - iPhone App'
                     ]

        list_text = ['@bellathorne If I see a picture on my iPhone that says Bella follows you will get a big smile on my lip :)',
                     'iPhone batteries are actually so fucking shitty Been without a phone all day &amp; night']
        for text in list_text:
            print(text)
            print(self.hate_speech_detector.get_text_score(text))


Controller()