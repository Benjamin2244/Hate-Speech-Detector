import os


class TextFileParser:
    def __init__(self):
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        self.project_dir = os.path.dirname(parent_dir)

    # Returns the content of a given file.
    def read_file(self, file_loc):
        file = open(file_loc, 'r')
        text = file.readlines()
        file.close()
        return text

    # Returns the path of the file with the name in the directory 'SentiWordNet_3.0.0'.
    def get_path(self, name):
        return os.path.join(self.project_dir, 'SentiWordNet_3.0.0', name)

    # Remove the POS column from the text.
    def remove_pos(self, text):
        return text[2:]

    # Remove the ID column from the text.
    def remove_id(self, text):
        pointer = 0
        on_id = False
        while pointer < len(text):
            if on_id:
                if not text[pointer].isnumeric():
                    return text[pointer + 1:]
            else:
                if text[pointer].isnumeric():
                    on_id = True
            pointer += 1
        return text

    # Returns the values in the text.
    def get_values(self, text):
        pointer = 0
        while pointer < len(text):
            if text[pointer] == '.' or text[pointer].isnumeric() or text[pointer].isspace():
                pass
            else:
                return text[:pointer - 1]
            pointer += 1
        return 0

    # Returns the text that is located past the values in the text.
    def get_non_values(self, text):
        pointer = 0
        while pointer < len(text):
            if text[pointer] == '.' or text[pointer].isnumeric() or text[pointer].isspace():
                pass
            else:
                return text[pointer:]
            pointer += 1
        return 0

    # Returns the positive value from the text.
    def get_positive(self, text):
        count = 0
        try:
            for c in text:
                if c == '.':
                    count += 1
        except:
            return 0
        if count == 0:
            return text[0]
        elif count == 1:
            first = text.index('.')
            if first > 1:
                return text[0]
            else:
                return text[:len(text) - 2]
        else:
            first = text.index('.')
            second = text.index('.', first + 1)
            return text[:second - 2]

    # Returns the negative value from the text.
    def get_negative(self, text):
        count = 0
        try:
            for c in text:
                if c == '.':
                    count += 1
        except:
            return 0
        if count == 0:
            return text[len(text) - 1]
        elif count == 1:
            first = text.index('.')
            if first == 1:
                return text[len(text) - 1]
            else:
                return text[first - 1:]
        else:
            first = text.index('.')
            second = text.index('.', first + 1)
            return text[second - 1:]

    # Remove the row if the positive and negative values are the same.
    def remove_neutral(self, text):
        values = self.get_values(text)
        non_values = self.get_non_values(text)
        pos = self.get_positive(values)
        neg = self.get_negative(values)
        overall = float(pos) - float(neg)
        if overall == 0:
            return ''
        return str(overall) + ' ' + non_values

    # Clean the SentiWordNet row.
    def clean_swn_row(self, row):
        pointer = len(row) - 1
        clean_row = ''
        while pointer >= 0:
            if row[pointer] == '#':
                clean_row = row[:pointer + 2]
                break
            pointer -= 1
        pointer = len(clean_row) - 1
        while pointer >= 0:
            c = clean_row[pointer]
            if c == '#':
                clean_row = clean_row[:pointer] + clean_row[pointer + 2:]
            pointer -= 1
        clean_row = self.remove_pos(clean_row)
        clean_row = self.remove_id(clean_row)
        clean_row = self.remove_neutral(clean_row)
        return clean_row

    # Clean the 'SentiWordNet_3.0.0.txt' and write the changes into 'CleanSentiWordNet_3.0.0.txt'.
    def create_clean_swn(self):
        original = self.get_path('SentiWordNet_3.0.0.txt')
        clean = self.get_path('CleanSentiWordNet_3.0.0.txt')
        text = self.read_file(original)
        clean_file = open(clean, 'w')
        clean_file.truncate(0)
        for row in text:
            if row[0] != '#':
                clean_row = self.clean_swn_row(row)
                if len(clean_row) == 0:
                    continue
                clean_file.writelines(clean_row + '\n')
        clean_file.close()

    # Returns all the data in 'CleanSentiWordNet_3.0.0.txt' as a list of Strings.
    def getAll(self):
        allData = []
        swn = self.get_path('CleanSentiWordNet_3.0.0.txt')
        text = self.read_file(swn)
        for row in text:
            allData.append(row.split())
        return allData

