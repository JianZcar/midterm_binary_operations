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
        out, bin_in = [0, bin_in[::-1] if reverse else bin_in]
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

    print(decimal)


def decimal_to_binary(decimal: int = None):
    decimal = int(input('Enter Decimal -> ')) if decimal is None else decimal
    binary = ''
    while True:
        bit, decimal = [decimal % 2, decimal // 2]
        binary += str(bit)

        if decimal == 0:
            break
    binary = binary[::-1]
    print(binary)
    pass


binary_to_decimal()
