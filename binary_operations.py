from binary import make_n_bits, binary_input, is_binary


def dot_adder(binary1: str, binary2: str):
    binary1 += '.' if '.' in binary2 and '.' not in binary1 else ''
    binary2 += '.' if '.' in binary1 and '.' not in binary2 else ''
    return binary1, binary2


def binary_operations(binary1: str, binary2: str, operation: int):
    mode = ['add', 'sub', 'mult', 'div'][operation]
    max_bits = 36
    binary1, binary2 = dot_adder(binary1, binary2)
    if operation <= 1:
        binary1, binary2 = make_n_bits(binary1), make_n_bits(binary2)

    has_fraction = True if '.' in binary1 else False
    dot = len(binary1.split('.')[0]) if has_fraction else None

    if '.' in binary1 and '.' in binary2:
        binary1, binary2 = binary1.replace('.', ''), binary2.replace('.', '')

    max_len = max(len(binary1), len(binary2))
    result = ''
    carry = 0
    for i in range(max_len - 1, -1, -1):
        bit1 = 1 if binary1[i] == '1' else 0
        bit2 = 1 if binary2[i] == '1' else 0

        if operation <= 1:
            result, carry = eval(f'{mode}_bin')(bit1, bit2, carry, result)
        elif operation == 2:
            result = mult_bin(binary1, binary2, max_bits)

    if len(result) >= 72 and has_fraction:
        result = result[-(max_bits*2):]
    elif len(result) >= 36 and not has_fraction:
        result = result[-max_bits:]

    result = f'{result[:dot]}.{result[dot:]}' if has_fraction else result
    result = [result.split('.')[0] if '1' not in result.split('.')[1] else result][0] if has_fraction else result
    return result


def add_bin(bit1, bit2, carry, result):
    temp = carry + bit1 + bit2
    carry = 1 if temp >= 2 else 0
    result = ('1' if temp % 2 == 1 else '0') + result
    return result, carry


def sub_bin(bit1, bit2, carry, result):
    bit2 += carry
    if bit1 < bit2:
        bit1 += 2
        carry = 1
    else:
        carry = 0
    result = ('1' if bit1 - bit2 == 1 else '0') + result
    return result, carry


def mult_bin(binary1, binary2, max_bits):
    result = '0'
    for o in range(len(binary2) - 1, -1, -1):
        if binary2[o] == '1':
            result = binary_addition(result, (binary1 + '0' * (len(binary2) - 1 - o))[-max_bits:])
    if not result:
        result = '0'
    return result


def binary_addition(binary1: str = None, binary2: str = None):
    binary1, binary2 = binary_input(binary1), binary_input(binary2)

    if not is_binary(binary1) and is_binary(binary2):
        print('Input Error')
        return None

    return binary_operations(binary1, binary2, 0)


def binary_subtraction(binary1: str = None, binary2: str = None):
    binary1, binary2 = binary_input(binary1), binary_input(binary2)

    if not is_binary(binary1) and is_binary(binary2):
        print('Input Error')
        return None
    return binary_operations(binary1, binary2, 1)


def binary_multiplication(binary1: str = None, binary2: str = None):
    binary1, binary2 = binary_input(binary1), binary_input(binary2)

    if not is_binary(binary1) and is_binary(binary2):
        print('Input Error')
        return None

    binary1, binary2 = dot_adder(binary1, binary2)
    bin_split1, bin_split2 = [binary1.split('.'), binary2.split('.')] if '.' in binary1 else [None, None]
    max_fraction = max(len(bin_split1[1]), len(bin_split2[1])) if '.' in binary1 else None
    if '.' in binary1:
        binary1, binary2 = [f'{bin_split1[0]}{bin_split1[1][::-1].zfill(max_fraction)[::-1]}',
                            f'{bin_split2[0]}{bin_split2[1][::-1].zfill(max_fraction)[::-1]}']
    result = binary_operations(binary1, binary2, 2)
    result = f'{result[:-max_fraction*2]}.{result[-max_fraction*2:]}' if max_fraction is not None else result
    if max_fraction is not None:
        result = [result.split('.')[0] if '1' not in result.split('.')[1] else result][0]
    return result
