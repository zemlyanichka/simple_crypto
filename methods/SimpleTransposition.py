from methods.BasicClass import BasicClass
import itertools


class SimpleTransposition(BasicClass):
    def __init__(self, message, key):
        BasicClass.__init__(self, message, key)
        self.key = key
        self.message = list(message.ljust(len(self.key)*6, '$'))
        self.dimension_of_alphabet = len(self.key), 6
        self.table = self.form_table(self.dimension_of_alphabet, self.message)

    def encode(self):
        pass

    def decode(self, encoded_message):
        pass
