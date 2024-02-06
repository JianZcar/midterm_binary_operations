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
    decimal = input('Enter Decimal -> ') if decimal is None else decimal

    if not is_decimal(decimal):
        print('Input Error')
        return None

    def inner(decimal_in, divisor: int or float, is_fraction: bool, max_cap: int = None):
        out = ''
        i = 0
        while True:
            i += 1
            bit = decimal_in % divisor if not is_fraction else (1 if decimal_in / divisor >= 1 else 0)
            decimal_in = decimal_in // 2 if not is_fraction else (decimal_in / divisor) - bit
            out += str(bit)
            if decimal_in == 0:
                break
            if max_cap is not None and i == max_cap:
                break
        out = out[::-1] if not is_fraction else out
        return out

    whole, fraction = (int(decimal.split('.')[0]) if '.' in decimal else int(decimal),
                       float(f'0.{decimal.split('.')[1]}' if '.' in decimal else None))

    binary = inner(whole, 2, False)
    if fraction is not None:
        binary += f'.{inner(fraction, 0.5, True, 10)}'

    print(binary)


decimal_to_binary()
# def decimal_to_binary(decimal: int = None):
#     decimal = int(input('Enter Decimal -> ')) if decimal is None else decimal
#     binary = ''
#     while True:
#         bit, decimal = [decimal % 2, decimal // 2]
#         binary += str(bit)
#
#         if decimal == 0:
#             break
#     binary = binary[::-1]
#     print(binary)
#     pass
