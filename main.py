from methods.PolybiusSquare import PolybiusSquare
from methods.SimpleTransposition import SimpleTransposition
from methods.GammaСode import GammaСode
from methods.AdfgvxEncode import AdfgvxEncode
from random import sample

if __name__ == '__main__':
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е',
                'ё', 'ж', 'з', 'и', 'й', 'к',
                'л', 'м', 'н', 'о', 'п', 'р',
                'с', 'т', 'у', 'ф', 'х', 'ц',
                'ч', 'ш', 'щ', 'ъ', 'ы', 'ь',
                'э', 'ю', 'я', ' ', ',', '.']
    #  TODO flags
    message = input()
    key = "хуитаж"
    message = message.lower()
    alphabet2 = sample(alphabet, len(alphabet))
    print(alphabet2)
    adfgvx = AdfgvxEncode(alphabet2, message, key)
    encoded = adfgvx.encode()
    print(encoded)
    decoded = adfgvx.decode(encoded)
    print(decoded)
