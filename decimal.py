from binary import (twos_compliment as binary_twos_compliment, n_bit_spacer as binary_n_bit_spacer,
                    make_n_bits as binary_make_n_bits)

from binary import binary_to_octal, binary_to_hexa


def decimal_input(decimal: str = None):
    return input('Enter Decimal -> ') if decimal is None else decimal


def is_decimal(decimal: str):
    try:
        float(decimal)
        return True
    except ValueError:
        return False


def decimal_to_binary(decimal: str = None, make_n_bits: bool = True):
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
        decimal = decimal.replace('-',
                                  '')
        negative = True

    whole, fraction = (int(decimal.split('.')[0]) if '.' in decimal else int(decimal),
                       float(f'0.{decimal.split('.')[1]}' if '.' in decimal else '0.0'))
    binary = inner(whole, 2, False)

    if fraction != 0.0:
        binary += f'.{inner(fraction, 0.5, True, 10)}'

    if not make_n_bits:
        return binary

    binary = binary_twos_compliment(binary) if negative else binary_make_n_bits(binary)
    return binary


def decimal_to_octal(decimal: str = None):
    decimal = decimal_input(decimal)

    if not is_decimal(decimal):
        print('Input Error')
        return None

    return binary_to_octal(decimal_to_binary(decimal))


def decimal_to_hexa(decimal: str = None):
    decimal = decimal_input(decimal)

    if not is_decimal(decimal):
        print('Input Error')
        return None

    return binary_to_hexa(decimal_to_binary(decimal))


if __name__ == '__main__':
    value = decimal_input()
    print(binary_n_bit_spacer(decimal_to_binary(value)))
    print(decimal_to_binary(value))
    print(decimal_to_octal(value))
    print(decimal_to_hexa(value))
