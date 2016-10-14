from methods.BasicClass import BasicClass
import numpy


class SimpleTransposition(BasicClass):
    def __init__(self, message, key):
        BasicClass.__init__(self, message, key)
        self.key = key
        message = list(message.ljust(len(self.key)*6, '$'))
        self.dimension_of_alphabet = 6, len(self.key)
        self.table = self.form_table(self.dimension_of_alphabet, message)

    @staticmethod
    def transpose_table(table):
        table = table.swapaxes(0, 1)
        return table

    def encode(self):
        dict_out = {}
        table = self.transpose_table(self.table)
        for x, y in zip(self.key, table):
            dict_out[x] = y
        encoded = numpy.array([], dtype=numpy.int)
        for i in sorted(dict_out):
                encoded = numpy.append(encoded, list(dict_out[i]))
        encoded = "".join(str(x) for x in encoded)
        return encoded

    def decode(self, encoded_message):
        table = list(encoded_message)
        table = list(zip(*[iter(table)] *(len(table)//len(self.key))))
        dict_out = {}
        for x, y in zip(list(sorted(self.key)), table):
            dict_out[x] = y
        decoded = numpy.array([], dtype=numpy.int)
        for j in self.key:
            for key, value in dict_out.items():
                if key == j:
                    decoded = numpy.append(decoded, list(value))
        decoded = list(zip(*[iter(decoded)] *(len(decoded)//len(self.key))))
        decoded = numpy.array(decoded)
        decoded = decoded.swapaxes(0, 1)
        decoded = decoded.ravel()
        decoded = list(filter('$'.__ne__, decoded))
        decoded = "".join(str(x) for x in decoded)
        return decoded