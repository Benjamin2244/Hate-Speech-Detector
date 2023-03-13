import os
import csv

class TestData:
    def __init__(self):
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        self.project_dir = os.path.dirname(parent_dir)

    # Returns the path of the file with the name in the directory 'TestData'.
    def get_path(self, name):
        return os.path.join(self.project_dir, 'TestData', name)

    # Create 'Results.csv'.
    def create_csv_results(self, allData):
        swn = self.get_path('Results.csv')
        csv_file = open(swn, 'w')
        csv_file.truncate(0)
        writer = csv.writer(csv_file)
        counter = 0
        for row in allData:
            new_row = [str(counter), '-', '-']
            writer.writerow(new_row)
            counter += 1
        csv_file.close()

    # Returns the text.
    def get_text(self, file_name, type):
        text = self.get_path(file_name)
        csv_file = open(text, 'r')
        reader = csv.reader(csv_file)
        rows = list(reader)
        testData = []
        for row in rows:
            testData.append((row[1], type))
        csv_file.close()
        return testData

    def getTestData(self):
        testData = []
        positive_test_data = self.get_text('reddit_comments_orientation_lgbtq_processed.csv', 'LGBT_hatespeech')
        testData += positive_test_data
        return testData

    def resetResults(self):
        testData = self.getTestData()
        self.create_csv_results(testData)

    def addResults(self, targets, results, indexes):
        results_name = self.get_path('Results.csv')
        csv_file = open(results_name, 'r+')
        reader = csv.reader(csv_file)
        rows = list(reader)
        count = 0
        for row in rows:
            if len(row) > 0:
                if int(row[0]) in indexes:
                    i = indexes.index(int(row[0]))
                    newRow = [row[0], targets[i], results[i]]
                    rows[count] = newRow
                    targets.pop(i)
                    results.pop(i)
                    indexes.pop(i)
                    if len(indexes) <= 0:
                        break
            count += 1
        csv_file.close()
        results_name = self.get_path('Results.csv')
        csv_file = open(results_name, 'w')
        csv_file.truncate(0)
        writer = csv.writer(csv_file)
        for row in rows:
            if len(row) > 0:
                writer.writerow(row)
        csv_file.close()

    def getResults(self):
        text = self.get_path('Results.csv')
        csv_file = open(text, 'r')
        reader = csv.reader(csv_file)
        rows = list(reader)
        csv_file.close()
        return rows

