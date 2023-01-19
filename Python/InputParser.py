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

    def get_text(self):
        clean_text = []
        dirty_text = self.read_input()
        front = 0
        back = 0
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