from methods.BasicClass import BasicClass
import itertools


class PolybiusSquare(BasicClass):
    def __init__(self, alphabet, message, key):
        BasicClass.__init__(self, message, key)
        self.alphabet = alphabet
        self.dimension_of_alphabet = 6, 6
        self.alphabet = self.form_table(self.dimension_of_alphabet, alphabet)

    @staticmethod
    def transposition_for_encode(coordinates):
        one = itertools.chain(*(x for x in [coordinates[::2]]))
        two = itertools.chain(*(x for x in [coordinates[1::2]]))
        new_coordinates = list(itertools.chain(one, two))
        lst = list(zip(*[iter(new_coordinates)] * 2))
        return lst

    @staticmethod
    def transposition_for_decode(coordinates):
        lst = list(zip(*[iter(coordinates)] * (int(len(coordinates)/2))))
        lst = list(zip(lst[0], lst[1]))
        return lst

    def encode(self):
        coordinates_of_letters = self.search_coordinates_of_letters(self.alphabet, self.message)
        coordinates_of_letters = self.transposition_for_encode(coordinates_of_letters)
        encoded = self.search_letters_by_coordinates(coordinates_of_letters, self.alphabet)
        return encoded

    def decode(self, encoded_message):
        coordinates_of_letters = self.search_coordinates_of_letters(self.alphabet, encoded_message)
        coordinates_of_letters = self.transposition_for_decode(coordinates_of_letters)
        decoded = self.search_letters_by_coordinates(coordinates_of_letters, self.alphabet)
        return decoded
