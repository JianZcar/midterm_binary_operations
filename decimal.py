from binary import (twos_compliment as binary_twos_compliment, four_bit_spacer as binary_four_bit_spacer,
                    make_16_bits as binary_make_16_bits)


def decimal_input(decimal: str = None):
    return input('Enter Decimal -> ') if decimal is None else decimal


def is_decimal(decimal: str):
    try:
        if '.' in decimal:
            float(decimal)
        else:
            int(decimal)
        return True
    except ValueError:
        return False


def decimal_to_binary(decimal: str = None):
    decimal = decimal_input(decimal)
    negative = False

    if not is_decimal(decimal):
        print('Input Error')
        return None

    def inner(decimal_in, divisor: int or float, is_fraction: bool, max_cap: int = None):
        out = ''
        i = 0

        while True:
            i += 1
            bit = (decimal_in % divisor if not is_fraction else (1 if decimal_in / divisor >= 1 else 0))
            decimal_in = decimal_in // 2 if not is_fraction else (decimal_in / divisor) - bit
            out += str(bit)

            if decimal_in == 0:
                break
            if max_cap is not None and i == max_cap:
                break

        out = out[::-1] if not is_fraction else out
        return out

    if '-' in decimal:
        decimal = decimal.replace('-', '')
        negative = True

    whole, fraction = (int(decimal.split('.')[0]) if '.' in decimal else int(decimal),
                       float(f'0.{decimal.split('.')[1]}' if '.' in decimal else '0.0'))
    binary = inner(whole, 2, False)

    if fraction != 0.0:
        binary += f'.{inner(fraction, 0.5, True, 10)}'

    binary = binary_twos_compliment(binary) if negative else binary_make_16_bits(binary)
    return binary


if __name__ == '__main__':
    value = decimal_input()
    print(binary_four_bit_spacer(decimal_to_binary(value)))
    print(decimal_to_binary(value))
