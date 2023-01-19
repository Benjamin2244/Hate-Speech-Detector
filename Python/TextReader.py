import os

class TextReader:
    def __init__(self):
        print('Created text reader')
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        self.project_dir = os.path.dirname(parent_dir)

    def read_file(self, file_loc):
        file = open(file_loc, 'r')
        text = file.readlines()
        file.close()
        return text

    def get_path(self, name):
        # return os.path.join(self.project_dir, '...', name)
        return os.path.join(self.project_dir, 'SentiWordNet_3.0.0', name)

    def remove_pos(self, text):
        return text[2:]

    def remove_id(self, text):
        pointer = 0
        on_id = False
        while pointer < len(text):
            if on_id:
                if not text[pointer].isnumeric():
                    return text[pointer+1:]
            else:
                if text[pointer].isnumeric():
                    on_id = True
            pointer += 1
        return text

    def get_values(self, text):
        pointer = 0
        while pointer < len(text):
            if text[pointer] == '.' or text[pointer].isnumeric() or text[pointer].isspace():
                pass
            else:
                return text[:pointer-1]
            pointer += 1
        return 0

    def get_non_values(self, text):
        pointer = 0
        while pointer < len(text):
            if text[pointer] == '.' or text[pointer].isnumeric() or text[pointer].isspace():
                pass
            else:
                return text[pointer:]
            pointer += 1
        return 0

    def get_pos(self, text):
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
                return text[:len(text)-2]
        else:
            first = text.index('.')
            second = text.index('.', first+1)
            return text[:second-2]

    def get_neg(self, text):
        count = 0
        try:
            for c in text:
                if c == '.':
                    count += 1
        except:
            return 0
        if count == 0:
            return text[len(text)-1]
        elif count == 1:
            first = text.index('.')
            if first == 1:
                return text[len(text)-1]
            else:
                return text[first-1:]
        else:
            first = text.index('.')
            second = text.index('.', first+1)
            return text[second-1:]

    def remove_neutral(self, text):
        values = self.get_values(text)
        non_values = self.get_non_values(text)
        pos = self.get_pos(values)
        neg = self.get_neg(values)
        overall = float(pos) - float(neg)
        if overall == 0:
            return ''
        return str(overall) + ' ' + non_values

    def clean_swn_row(self, row):
        pointer = len(row) - 1
        clean_row = ''
        while pointer >= 0:
            if row[pointer] == '#':
                clean_row = row[:pointer + 2]
                break
            pointer -= 1
        pointer = len(clean_row)-1
        while pointer >= 0:
            c = clean_row[pointer]
            if c == '#':
                clean_row = clean_row[:pointer] + clean_row[pointer+2:]
            pointer -= 1
        clean_row = self.remove_pos(clean_row)
        clean_row = self.remove_id(clean_row)
        clean_row = self.remove_neutral(clean_row)
        return clean_row

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