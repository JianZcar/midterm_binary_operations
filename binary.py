def is_binary(binary: str = '') -> bool:
    characters = "01."
    if not any(binary) or binary.count('.') > 1:
        return False
    for char in binary:
        if char not in characters:
            return False
    return True


def binary_to_decimal(binary: str = ''):
    binary = input('Enter Binary -> ') if binary == '' else binary

    if not is_binary(binary):
        print('Input Error')
        return None

    def inner(bin_in: str, power: int, add: bool, reverse: bool):
        out, bin_in = 0, bin_in[::-1] if reverse else bin_in
        for bit in bin_in:
            out += int(bit) * (2**power)
            power += 1 if add else -1
        return out

    if binary.count('.') == 1:
        left, right = binary.split('.')
        decimal = inner(left, 0, True, True)
        decimal += inner(right, -1, False, False)

    else:
        decimal = inner(binary, 0, True, True)

    print(binary)
    return binary


def twos_compliment(binary: str = ''):
    binary = input('Enter Binary -> ') if binary == '' else binary

    if not is_binary(binary):
        print('Input Error')
        return None

    # Reverse the bits
    binary = ''.join('1' if bit == '0' else '0' for bit in binary)

    # Add 1 to the result
    binary = bin(int(binary, 2) + 1)[2:]

    print(binary)
    return binary


def four_bit_spacer(binary: str = ''):
    binary = input('Enter Binary -> ') if binary == '' else binary

    if not is_binary(binary):
        print('Input Error')
        return None

    # Add a space every four bits
    binary = ' '.join([binary[i:i+4] for i in range(0, len(binary), 4)])

    return binary


def make_16_bits(binary: str = ''):
    binary = input('Enter Binary -> ') if binary == '' else binary

    if not is_binary(binary):
        print('Input Error')
        return None

    if len(binary) > 16:
        print('Input binary is more than 16 bits')
        return None

    # Pad with leading zeros
    binary = binary.zfill(16)
    binary = four_bit_spacer(binary)

    print(binary)
    return binary


make_16_bits()
