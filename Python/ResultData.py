import os
import csv


class ResultData:
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
        for _ in allData:
            new_row = [str(counter), '-', '-']
            writer.writerow(new_row)
            counter += 1
        csv_file.close()

    # Returns the text.
    def get_text(self, file_name, file_type):
        text = self.get_path(file_name)
        csv_file = open(text, 'r')
        reader = csv.reader(csv_file)
        rows = list(reader)
        testData = []
        for row in rows:
            if len(row) > 0:
                testData.append((row[1], file_type))
        csv_file.close()
        return testData

    def getTestData(self):
        testData = []
        LGBT_hate_speech_test_data = self.get_text(
            'reddit_comments_orientation_lgbtq_processed.csv', 'LGBT_hate_speech')
        not_hate_speech_test_data = self.get_text(
            'not_hate_speech.csv', 'non_hate_speech')
        testData += LGBT_hate_speech_test_data
        testData += not_hate_speech_test_data
        return testData

    def resetResults(self):
        testData = self.getTestData()
        self.create_csv_results(testData)

    def addResults(self, targets, results, texts, indexes):
        results_name = self.get_path('Results.csv')
        csv_file = open(results_name, 'r+')
        reader = csv.reader(csv_file)
        rows = list(reader)
        count = 0
        for row in rows:
            if len(row) > 0:
                if int(row[0]) in indexes:
                    i = indexes.index(int(row[0]))
                    newRow = [row[0], targets[i], results[i], texts[i]]
                    rows[count] = newRow
                    targets.pop(i)
                    results.pop(i)
                    texts.pop(i)
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

    # Had to remove 'training.1600000.processed.noemoticon.csv' due to ot being too large for git.
    # def cleanSentiment140Results(self):
    #     text = self.get_path('training.1600000.processed.noemoticon.csv')
    #     csv_file = open(text, 'r')
    #     reader = csv.reader(csv_file)
    #     rows = list(reader)
    #     positiveRows = []
    #     for row in rows:
    #         if len(row) > 0:
    #             if row[0] == '4':
    #                 positiveRows.append(row)
    #     if len(positiveRows) > 10000:
    #         positiveRows = positiveRows[:10000]
    #     csv_file.close()
    #     return positiveRows

    # Had to remove 'training.1600000.processed.noemoticon.csv' due to ot being too large for git.
    # def create_clean_sentiment140(self):
    #     nhs = self.get_path('not_hate_speech.csv')
    #     csv_file = open(nhs, 'w')
    #     csv_file.truncate(0)
    #     writer = csv.writer(csv_file)
    #     rows = self.cleanSentiment140Results()
    #     for row in rows:
    #         if len(row) > 0:
    #             text = row[5]
    #             writer.writerow(['', str(text)])
    #     csv_file.close()
