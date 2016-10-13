from methods.BasicClass import BasicClass
import itertools
import numpy


class AdfgvxEncode(BasicClass):
    def __init__(self, alphabet, message, key):
        BasicClass.__init__(self, message, key)
        self.key = key
        dimension_of_alphabet = 6, 6
        self.alphabet = self.form_table(dimension_of_alphabet, alphabet)
        print(self.alphabet)

    def transpose_table_for_encode(self, table):
        table = list(itertools.zip_longest(*[iter(table)] * len(self.key)))
        table = numpy.array(table)
        table = table.swapaxes(0, 1)
        return table

    def transpose_to_decode(self, table):
        len_of_table = len(table)
        while len_of_table % len(self.key) != 0:
            len_of_table += 1
        table = list(itertools.zip_longest(*[iter(table)] * (len_of_table//len(self.key))))
        return table

    def encode(self):
        coordinates_of_letters = self.search_coordinates_of_letters(self.alphabet, self.message)
        table = self.transpose_table_for_encode(coordinates_of_letters)
        """вместо букв - индексы, будет надо заменю, но смысла не вижу"""
        dict_out = {}
        for x, y in zip(list(self.key), table):
            dict_out[x] = y
        encoded = numpy.array([], dtype=numpy.int)
        for i in sorted(dict_out):
                encoded = numpy.append(encoded, list(dict_out[i]))
        encoded = list(filter(None.__ne__, encoded))
        encoded = "".join(str(x) for x in encoded)
        return encoded

    def decode(self, encoded_message):
        table = numpy.array(list(encoded_message))
        table = self.transpose_to_decode(table)
        dict_out = {}
        for x, y in zip(list(sorted(self.key)), table):
            dict_out[x] = y
        decoded = numpy.array([], dtype=numpy.int)
        for j in self.key:
            for key, value in dict_out.items():
                if key == j:
                    decoded = numpy.append(decoded, value)
        decoded = list(itertools.zip_longest(*[iter(decoded)] * (len(decoded)//len(self.key))))
        decoded = numpy.array(decoded)
        decoded = decoded.swapaxes(0, 1)
        decoded = numpy.ravel(decoded)
        decoded = list(zip(*[iter(decoded)] * 2))
        decoded = self.search_letters_by_coordinates(decoded, self.alphabet)
        return decoded