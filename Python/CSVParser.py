import os
import csv
from TextFileParser import TextFileParser


class CSVParser:
    def __init__(self):
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        self.project_dir = os.path.dirname(parent_dir)
        self.txt_parser = TextFileParser()

    # Returns the path of the file with the name in the directory 'SentiWordNet_3.0.0'.
    def get_path(self, name):
        return os.path.join(self.project_dir, 'SentiWordNet_3.0.0', name)

    # Create 'SentiWordNet_3.0.0.csv'.
    def create_csv_swn(self, allData):
        swn = self.get_path('SentiWordNet_3.0.0.csv')
        csv_file = open(swn, 'w')
        csv_file.truncate(0)
        writer = csv.writer(csv_file)
        for row in allData:
            writer.writerow(row)
        csv_file.close()

    # Returns the values corresponding to the word.
    def get_values(self, word):
        swn = self.get_path('SentiWordNet_3.0.0.csv')
        csv_file = open(swn, 'r')
        reader = csv.reader(csv_file)
        rows = list(reader)
        values = []
        for row in rows:
            if word in row:
                values.append(row[0])
        csv_file.close()
        return values

    def getWords(self):
        swn = self.get_path('SentiWordNet_3.0.0.csv')
        csv_file = open(swn, 'r')
        reader = csv.reader(csv_file)
        rows = list(reader)
        words = []
        for row in rows:
            if len(row) > 0:
                words.append(row)
        csv_file.close()
        return words

    def resetWords(self):
        words = self.txt_parser.getAll()
        self.create_csv_swn(words)

    def saveWords(self, words):
        self.create_csv_swn(words)

    def addWord(self, word, score):
        words = self.getWords()
        words.append([score, word])
        self.saveWords(words)

    def removeWord(self, word):
        words = self.getWords()
        new_words = []
        for row in words:
            if word in row:
                row.remove(word)
            if len(row) > 1:
                new_words.append(row)
        self.saveWords(new_words)
