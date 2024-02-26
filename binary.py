def binary_input(binary: str = None):
    return input('Enter Binary -> ').replace(' ', '') if binary is None else binary


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


def make_n_bits(binary: str = None, bits: int = 36):
    """Make into 36 bits"""
    binary = binary.replace(' ', '')
    if '.' in binary:
        binary = f'{make_n_bits(binary.split('.')[0])}.{make_n_bits(binary.split('.')[1][::-1])[::-1]}'

    elif len(binary) > bits:
        print(f'Input binary is more than {bits} bits')
        return None

    binary = binary.zfill(bits)
    return binary


def binary_to_decimal(binary: str = None):
    binary = binary_input(binary)

    if not is_binary(binary):
        print('Input Error')
        return None

    binary = make_n_bits(binary)
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

    if not is_binary(binary):
        print('Input Error')
        return None
    once = True
    result = ''
    binary = make_n_bits(binary)
    for bit in binary[::-1]:
        if once is True and bit == '1':
            result = f'{bit}{result}'
            once = False
        elif bit == '.':
            result = f'{bit}{result}'
        elif once is not True:
            result = f'1{result}' if bit == '0' else f'0{result}'
        else:
            result = f'{bit}{result}'
    return result


def binary_to_hexa(binary: str = None):
    binary = binary_input(binary)

    if not is_binary(binary):
        print('Input Error')
        return None

    binary = make_n_bits(binary)
    hexa_characters = ['A', 'B', 'C', 'D', 'E', 'F']
    binary_array = [n_bit_spacer(binary.split('.')[0]).split() if '.' in binary
                    else n_bit_spacer(binary).split(),
                    n_bit_spacer(binary.split('.')[1]).split() if '.' in binary
                    else None]

    def inner(b_array: list):
        hexa = ''
        for f_bit in b_array:
            decimal = binary_to_decimal(f_bit)
            hexa += f'{decimal}' if decimal < 10 else hexa_characters[decimal-10]
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

    binary = make_n_bits(binary)

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
    print(n_bit_spacer(make_n_bits(value)))
    print(binary_to_decimal(value))
    print(binary_to_hexa(value))
    print(binary_to_octal(value))
