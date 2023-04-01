from LGBTQIA_CSV_Parser import LGBTQIACSVParser


class LGBTQIADetector:

    def __init__(self):
        self.related_words = LGBTQIACSVParser()

    def isWordRelated(self, word):
        return self.related_words.isRelated(word)

    def isTextRelated(self, text):
        for word in text:
            if self.isWordRelated(word):
                return True
        return False
