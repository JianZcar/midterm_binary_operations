def binary_input(binary: str = None):
    return input('Enter Binary -> ') if binary is None else binary


def is_binary(binary: str) -> bool:
    characters = "01."
    if not any(binary) or binary.count('.') > 1:
        return False
    for char in binary:
        if char not in characters:
            return False
    return True


def n_bit_spacer(binary: str = None, bit: int = 4):
    binary_array = [binary, None] if '.' not in binary else binary.split('.')
    binary = ' '.join([binary_array[0][max(i-bit, 0):i] for i in range(len(binary_array[0]), 0, -bit)][::-1])

    if binary_array[1] is not None:
        binary = f'{binary}.{' '.join([binary_array[1][i:i+bit] for i in range(0, len(binary_array[1]), bit)])}'
    return binary


def make_32_bits(binary: str = None):
    """Make into 36 bits"""
    bits = 36
    if '.' in binary:
        binary = f'{make_32_bits(binary.split('.')[0])}.{make_32_bits(binary.split('.')[1][::-1])[::-1]}'

    elif len(binary.replace(' ', '')) > bits:
        print(f'Input binary is more than {bits} bits')
        return None

    binary = binary.zfill(bits)
    return binary


def binary_to_decimal(binary: str = None):
    binary = binary_input(binary)

    if not is_binary(binary):
        print('Input Error')
        return None

    binary = make_32_bits(binary)
    binary_array = [binary, None] if '.' not in binary else binary.split('.')

    def inner(bin_in: str, power: int, add: bool, reverse: bool):
        out, bin_in = 0, bin_in[::-1] if reverse else bin_in

        for index, bit in enumerate(bin_in):
            out += int(bit) * (-1 * (2**power)) if add and index == len(bin_in) - 1 else int(bit) * (2**power)
            power += 1 if add else -1
        return out

    decimal = inner(binary_array[0], 0, True, True)
    decimal += inner(binary_array[1], -1, False, False) if binary_array[1] is not None else 0
    return decimal


def twos_compliment(binary: str = None):
    binary = binary_input(binary)
    dot = None

    if not is_binary(binary):
        print('Input Error')
        return None

    has_fraction = True if '.' in binary else False

    if '1' not in binary:
        return make_32_bits('0')

    binary = make_32_bits(binary)

    if has_fraction:
        dot = len(binary.split('.')[0])
        binary = binary.replace('.', '')

    binary = ''.join('1' if bit == '0' else '0' for bit in binary)
    binary = bin(int(binary, 2) + 1)[2:]
    binary = f'{binary[:dot]}.{binary[dot:]}' if has_fraction else binary
    return binary


def binary_to_hexa(binary: str = None):
    binary = binary_input(binary)

    if not is_binary(binary):
        print('Input Error')
        return None

    binary = make_32_bits(binary)
    hexa_character = ['A', 'B', 'C', 'D', 'E', 'F']
    binary_array = [n_bit_spacer(binary.split('.')[0]).split() if '.' in binary
                    else n_bit_spacer(binary).split(),
                    n_bit_spacer(binary.split('.')[1]).split() if '.' in binary
                    else None]

    def inner(b_array: list):
        hexa = ''
        for f_bit in b_array:
            decimal = binary_to_decimal(f_bit)
            hexa += f'{decimal}' if decimal < 10 else hexa_character[decimal-10]
        return hexa
    hexadecimal = inner(binary_array[0])

    if binary_array[1] is not None:
        hexadecimal += f'.{inner(binary_array[1])}'
    return hexadecimal


def binary_to_octal(binary: str = None):
    binary = binary_input(binary)

    if not is_binary(binary):
        print('Input Error')
        return None

    binary = make_32_bits(binary)

    binary_array = [n_bit_spacer(binary.split('.')[0], 3).split() if '.' in binary
                    else n_bit_spacer(binary, 3).split(),
                    n_bit_spacer(binary.split('.')[1], 3).split() if '.' in binary
                    else None]

    def inner(b_array: list):
        octal_ = ''
        for th_bit in b_array:
            decimal = binary_to_decimal(th_bit)
            octal_ += f'{decimal}'
        return octal_
    octal = inner(binary_array[0])

    if binary_array[1] is not None:
        octal += f'.{inner(binary_array[1])}'
    return octal


if __name__ == '__main__':
    value = binary_input()
    print(n_bit_spacer(make_32_bits(value)))
    print(binary_to_decimal(value))
    print(binary_to_hexa(value))
    print(binary_to_octal(value))
