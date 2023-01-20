class InputParser:
    def __init__(self):
        print('Created input parser')

    def read_input(self):
        return 'Input: ABC'

    def get_word(self, text, front, back):
        word = ''
        for i in range(front, back):
            word += text[i]
        return word

    def remove_non_letters(self, dirty_text):
        clean_text = ''
        for c in dirty_text:
            if c.isalpha() or c == ' ':
                clean_text += c
        return clean_text

    def to_lowercase(self, text):
        return text.lower()

    def get_clean_text(self, dirty_text):
        clean_text = []
        front = 0
        back = 0
        dirty_text = self.remove_non_letters(dirty_text)
        dirty_text = self.to_lowercase(dirty_text)
        for c in dirty_text:
            if c == ' ':
                word = self.get_word(dirty_text, front, back)
            elif back == len(dirty_text)-1:
                word = self.get_word(dirty_text, front, back+1)
            else:
                back += 1
                continue
            back += 1
            front = back
            clean_text.append(word)
        return clean_text