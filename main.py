from InputParser import InputParser


class Introduction:
    def __init__(self):
        input_parser = InputParser()
        text = input_parser.getText()
        print(text)
        self.print_intro()

    def print_intro(self):
        print('This is the introduction page.')

Introduction()