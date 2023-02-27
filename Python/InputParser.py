class InputParser:
    def __init__(self):
        self.POSITIVE_EMOJIS = [':)', ':-)', ': )', ':D', '=)', ':-D', 'o:)-', '8-)', ':$']
        self.NEGATIVE_EMOJIS = [':(', ':-(', ': (', ":'(", ':o', '>(', '(@)', 'X|']

    # Returns the word between the two indexes.
    def get_word(self, text, front, back):
        word = ''
        for i in range(front, back):
            word += text[i]
        return word

    # Remove all the non letters in the text.
    def remove_non_letters(self, dirty_text):
        clean_text = ''
        for c in dirty_text:
            if c.isalpha() or c == ' ':
                clean_text += c
        return clean_text

    # Returns text as lowercase.
    def to_lowercase(self, text):
        return text.lower()

    # Returns clean version of text.
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
            if word == '':
                continue
            clean_text.append(word)
        return clean_text

    # Returns a list of '+' and '-' that indicates the positive and negative emojis within the text.
    def getEmojis(self, text):
        emojis = []
        for emoji in self.POSITIVE_EMOJIS:
            if emoji in text:
                emojis.append('+')
        for emoji in self.NEGATIVE_EMOJIS:
            if emoji in text:
                emojis.append('-')
        return emojis