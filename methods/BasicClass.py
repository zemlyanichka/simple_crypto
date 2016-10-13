import numpy


class BasicClass:
    def __init__(self, message, key):
        self.message = message
        self.key = key

    def form_table(self, dimension_of_alphabet, alphabet):
        alphabet = numpy.array(alphabet)
        alphabet = alphabet.reshape(dimension_of_alphabet)
        return alphabet

    @staticmethod
    def search_coordinates_of_letters(table, message):
        coordinates_of_letters = numpy.array([], numpy.int)
        for i in message:
            item_index = numpy.where(table == i)
            coordinates_of_letters = numpy.append(coordinates_of_letters, item_index)
        return coordinates_of_letters

    @staticmethod
    def search_letters_by_coordinates(coordinates, table):
        letters = ""
        for i in coordinates:
            letters += table[i]
        return letters
