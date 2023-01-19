from InputParser import InputParser
from TextReader import TextReader


class Controller:
    def __init__(self):
        input_parser = InputParser()
        txt_reader = TextReader()
        self.print_intro()

    def print_intro(self):
        print('This is the introduction page.')

Controller()