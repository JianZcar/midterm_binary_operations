from decimal import decimal_to_binary
from binary import binary_to_decimal, make_n_bits, n_bit_spacer, binary_to_hexa


def octal_input(octal_: str = None):
    return input('Enter Octal -> ') if octal_ is None else octal_


def is_octal(octal_: str) -> bool:
    characters = "01234567."
    if not any(octal_) or octal_.count('.') > 1:
        return False
    for char in octal_:
        if char not in characters:
            return False
    return True


def octal_to_binary(octal: str = None):
    octal = octal_input(octal) if octal is None else octal

    if not is_octal(octal):
        print('Input Error')
        return None

    def inner(octal_: str):
        _bin = ''

        for oct_char in octal_:
            _bin += make_n_bits(decimal_to_binary(oct_char, False), 3)
        return _bin

    binary = [f'{inner(octal.split('.')[0])}.{inner(octal.split('.')[1])}' if '.' in octal
              else inner(octal)][0]

    return make_n_bits(binary)


def octal_to_decimal(octal: str = None):
    octal = octal_input(octal) if octal is None else octal

    if not is_octal(octal):
        print('Input Error')
        return None

    return binary_to_decimal(octal_to_binary(octal))


def octal_to_hexa(octal: str = None):
    octal = octal_input(octal) if octal is None else octal

    if not is_octal(octal):
        print('Input Error')
        return None

    return binary_to_hexa(octal_to_binary(octal))


if __name__ == '__main__':
    value = octal_input()
    print(octal_to_binary(value))
    print(octal_to_decimal(value))
    print(octal_to_hexa(value))
    