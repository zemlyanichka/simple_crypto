from methods.SimpleTransposition import SimpleTransposition
from methods.BasicClass import BasicClass
import numpy


class AdfgvxEncode(SimpleTransposition, BasicClass):
    def __init__(self, alphabet, message, key):
        SimpleTransposition.__init__(self, message, key)
        BasicClass.__init__(self, message, key)
        self.key = key
        if len(self.message) % len(self.key) != 0:
           self.message = self.message.ljust((len(self.key)*len(self.message)), ' ')
        dimension_of_alphabet = 6, 6
        self.unsigned_table = self.form_table(dimension_of_alphabet, alphabet)
        table = self.search_coordinates_of_letters(self.unsigned_table, self.message)
        table = list(zip(*[iter(table)] * len(self.key)))
        self.table = numpy.array(table, dtype=numpy.int)

    def encoding(self):
        """цифры вместо адфгвх, не думаю что беда"""
        encoded = self.encode()
        return encoded

    #  TODO fixing VisibleDeprecationWarning
    def decoding(self, encoded_message):
        decoded = self.decode(encoded_message)
        decoded =  list(zip(*[iter(decoded)] * 2))
        decoded = self.search_letters_by_coordinates(decoded, self.unsigned_table)
        return decoded