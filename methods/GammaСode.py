from methods.BasicClass import BasicClass


class GammaСode(BasicClass):
    def __init__(self, alphabet, message, key):
        BasicClass.__init__(self, message, key)
        self.message = message
        self.dimension_of_alphabet = len(alphabet)
        self.alphabet = self.form_table(self.dimension_of_alphabet, alphabet)

    @staticmethod
    def correct_gamma_length(message, gamma):
        """need more faster realization"""
        len_of_message = len(message)
        len_of_gamma = len(gamma)
        if len_of_gamma < len_of_message:
            for i in gamma:
                while len(gamma) < len(message):
                    gamma += i
        elif len_of_gamma > len_of_message:
            gamma = gamma[:len_of_message:]
        return gamma

    def encode(self):
        gamma = self.correct_gamma_length(self.message, self.key)
        t = self.search_coordinates_of_letters(self.alphabet, self.message)
        g = self.search_coordinates_of_letters(self.alphabet, gamma)
        t_plus_g_mod_n = (t + g) % len(self.alphabet)
        for i, j in enumerate(t_plus_g_mod_n):
            if j==0:
                t_plus_g_mod_n[i] += len(self.alphabet)
        encoded = self.search_letters_by_coordinates(t_plus_g_mod_n, self.alphabet)
        return encoded

    def decode(self, encoded_message, key):
        gamma = self.correct_gamma_length(encoded_message, key)
        c = self.search_coordinates_of_letters(self.alphabet, encoded_message)
        g = self.search_coordinates_of_letters(self.alphabet, gamma)
        c_minus_g_mod_n = (c - g) % len(self.alphabet)
        for i, j in enumerate(c_minus_g_mod_n):
            if j==0:
                c_minus_g_mod_n[i] += len(self.alphabet)
        decoded = self.search_letters_by_coordinates(c_minus_g_mod_n, self.alphabet)
        return decoded
