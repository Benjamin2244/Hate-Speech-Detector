import os
import csv

class CSVParser:
    def __init__(self):
        print('Created csv parser')
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        self.project_dir = os.path.dirname(parent_dir)

    def get_path(self, name):
        # return os.path.join(self.project_dir, '...', name)
        return os.path.join(self.project_dir, 'SentiWordNet_3.0.0', name)

    def create_csv_swn(self, allData):
        swn = self.get_path('SentiWordNet_3.0.0.csv')
        csv_file = open(swn, 'w')
        csv_file.truncate(0)
        writer = csv.writer(csv_file)
        for row in allData:
            writer.writerow(row)
        csv_file.close()

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

