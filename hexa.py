from decimal import decimal_to_binary
from binary import binary_to_decimal, make_n_bits, n_bit_spacer, binary_to_octal


def hexa_input(hexa: str = None):
    return input('Enter Hexadecimal -> ') if hexa is None else hexa


def is_hexa(hexa: str) -> bool:
    characters = "0123456789.abcdefABCDEF"
    if not any(hexa) or hexa.count('.') > 1:
        return False
    for char in hexa:
        if char not in characters:
            return False
    return True


def hexa_to_binary(hexadecimal: str = None):
    hexadecimal = hexa_input(hexadecimal) if hexadecimal is None else hexadecimal

    if not is_hexa(hexadecimal):
        print('Input Error')
        return None

    hexa_characters = ['A', 'B', 'C', 'D', 'E', 'F']
    hexadecimal = hexadecimal.upper()

    def inner(hexa: str):
        _bin = ''
        num = '0123456789'
        for hexa_char in hexa:
            _bin += [make_n_bits(decimal_to_binary(hexa_char, False), 4) if hexa_char in num
                     else
                     make_n_bits(decimal_to_binary(f'{hexa_characters.index(hexa_char) + 10}', False), 4)][0]
        return _bin

    binary = [f'{inner(hexadecimal.split('.')[0])}.{inner(hexadecimal.split('.')[1])}' if '.' in hexadecimal
              else inner(hexadecimal)][0]
    return make_n_bits(binary)


def hexa_to_decimal(hexadecimal: str = None):
    hexadecimal = hexa_input(hexadecimal) if hexadecimal is None else hexadecimal

    if not is_hexa(hexadecimal):
        print('Input Error')
        return None

    return binary_to_decimal(hexa_to_binary(hexadecimal))


def hexa_to_octal(hexadecimal: str = None):
    hexadecimal = hexa_input(hexadecimal) if hexadecimal is None else hexadecimal

    if not is_hexa(hexadecimal):
        print('Input Error')
        return None

    return binary_to_octal(hexa_to_binary(hexadecimal))


if __name__ == '__main__':
    value = hexa_input()
    print(n_bit_spacer(hexa_to_binary(value)))
    print(hexa_to_binary(value))
    print(hexa_to_decimal(value))
    print(hexa_to_octal(value))
