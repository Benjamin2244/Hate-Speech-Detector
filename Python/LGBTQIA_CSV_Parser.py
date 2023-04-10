import os
import csv


class LGBTQIACSVParser:
    def __init__(self):
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        self.project_dir = os.path.dirname(parent_dir)

    # Returns the path of the file with the name in the directory ''lgbtqia_Terms.
    def get_path(self, name):
        return os.path.join(self.project_dir, 'LGBTQIA_Terms', name)

    # Returns True if word is in the related terms.
    # Returns False if word not in related terms.
    def isRelated(self, word):
        related = self.get_path('LGBTQIA_Terms.csv')
        csv_file = open(related, 'r')
        reader = csv.reader(csv_file)
        rows = list(reader)
        for row in rows:
            if word in row:
                csv_file.close()
                return True
            elif len(row) > 0:
                if row[0] in word:
                    csv_file.close()
                    return True
        csv_file.close()
        return False

    def getWords(self):
        related = self.get_path('LGBTQIA_Terms.csv')
        csv_file = open(related, 'r')
        reader = csv.reader(csv_file)
        rows = list(reader)
        words = []
        for word in rows:
            if len(word) > 0:
                words.append(word[0])
        csv_file.close()
        return words

    def getDefaultWords(self):
        related = self.get_path('Default_LGBTQIA_Terms.csv')
        csv_file = open(related, 'r')
        reader = csv.reader(csv_file)
        rows = list(reader)
        words = []
        for word in rows:
            if len(word) > 0:
                words.append(word[0])
        csv_file.close()
        return words

    def resetWords(self):
        words = self.getDefaultWords()
        self.saveWords(words)

    def saveWords(self, words):
        LGBTQIA_RELATED_WORDS = self.get_path('LGBTQIA_Terms.csv')
        csv_file = open(LGBTQIA_RELATED_WORDS, 'w')
        csv_file.truncate(0)
        writer = csv.writer(csv_file)
        for word in words:
            new_row = word
            writer.writerow([new_row])
        csv_file.close()

    def addWord(self, word):
        words = self.getWords()
        words.append(word)
        self.saveWords(words)

    def removeWord(self, word):
        words = self.getWords()
        while word in words:
            words.remove(word)
        self.saveWords(words)
