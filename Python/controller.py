from InputParser import InputParser
from TextReader import TextReader


class Controller:
    def __init__(self):
        input_parser = InputParser()
        txt_reader = TextReader()
        word = 'angry'
        print (word)
        print(txt_reader.get_value(word))
        self.print_intro()

    def print_intro(self):
        print('This is the introduction page.')

Controller()