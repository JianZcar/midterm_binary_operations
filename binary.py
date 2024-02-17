def binary_input(binary: str = None):
    return input('Enter Binary -> ') if binary is None else binary


def is_binary(binary: str) -> bool:
    characters = "01. "
    if not any(binary) or binary.count('.') > 1:
        return False
    for char in binary:
        if char not in characters:
            return False
    return True


def four_bit_spacer(binary: str = None):
    binary = binary_input(binary)

    if not is_binary(binary):
        print('Input Error')
        return None

    if '.' in binary:
        whole, fraction = binary.split('.')
        whole = ' '.join([whole[max(i-4, 0):i] for i in range(len(whole), 0, -4)][::-1])
        fraction = ' '.join([fraction[i:i+4] for i in range(0, len(fraction), 4)])
        binary = whole + '.' + fraction
    else:
        binary = ' '.join([binary[max(i-4, 0):i] for i in range(len(binary), 0, -4)][::-1])

    return binary


def make_16_bits(binary: str = None):
    binary = binary_input(binary)

    if not is_binary(binary):
        print('Input Error')
        return None

    if '.' in binary:
        binary = f'{make_16_bits(binary.split('.')[0])}.{make_16_bits(binary.split('.')[1][::-1])[::-1]}'

    elif len(binary.replace(' ', '')) > 16:
        print('Input binary is more than 16 bits')
        return None

    binary = binary.zfill(16)

    return binary


def binary_to_decimal(binary: str = None):
    binary = binary_input(binary)

    if not is_binary(binary):
        print('Input Error')
        return None

    binary = make_16_bits(binary)

    def inner(bin_in: str, power: int, add: bool, reverse: bool):
        out, bin_in = 0, bin_in[::-1] if reverse else bin_in
        for index, bit in enumerate(bin_in):
            if add and index == len(bin_in) - 1:
                out += int(bit) * (-1 * (2**power))
            else:
                out += int(bit) * (2**power)
            power += 1 if add else -1
        return out

    if binary.count('.') == 1:
        whole, fraction = binary.split('.')
        decimal = inner(whole, 0, True, True)
        decimal += inner(fraction, -1, False, False)

    else:
        decimal = inner(binary, 0, True, True)

    return decimal


def twos_compliment(binary: str = ''):
    binary = binary_input(binary)
    dot = None

    if not is_binary(binary):
        print('Input Error')
        return None

    has_fraction = True if '.' in binary else False

    if '1' not in binary:
        print('Cannot complement a 0 value')

    binary = make_16_bits(binary)

    if has_fraction:
        dot = len(binary.split('.')[0])
        binary = binary.replace('.', '')

    binary = ''.join('1' if bit == '0' else '0' for bit in binary)
    binary = bin(int(binary, 2) + 1)[2:]
    binary = f'{binary[:dot]}.{binary[dot:]}' if has_fraction else binary

    return binary


if __name__ == '__main__':
    value = binary_input()
    print(binary_to_decimal(value))
