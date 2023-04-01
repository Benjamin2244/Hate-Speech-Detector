from TextFileParser import TextFileParser
from CSVParser import CSVParser


class Initializer:

    def __init__(self):
        self.txt_parser = TextFileParser()
        self.csv_parser = CSVParser()

    def initialise(self):
        self.createCleanSWN()
        self.createSWNcsv()

    # Create 'CleanSentiWordNet_3.0.0.txt'.
    def createCleanSWN(self):
        self.txt_parser.create_clean_swn()

    # Create 'SentiWordNet_3.0.0.csv'.
    def createSWNcsv(self):
        allData = self.txt_parser.getAll()
        self.csv_parser.create_csv_swn(allData)
