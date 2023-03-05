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
        csv_file.close()
        return False


