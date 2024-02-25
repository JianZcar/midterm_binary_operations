from binary import make_n_bits


# def binary_addition(binary1: str, binary2: str):
#     max_bits = 36
#     binary1 += '.' if '.' in binary2 else ''
#     binary2 += '.' if '.' in binary1 else ''
#     has_fraction = True if '.' in binary1 else False
#     binary1, binary2 = make_n_bits(binary1), make_n_bits(binary2)
#     dot = len(binary1.split('.')[0]) if has_fraction else None
#     result = ''
#     carry = 0
#     binary1, binary2 = binary1.replace('.', ''), binary2.replace('.', '')
#     max_len = max(len(binary1), len(binary2))
#     for i in range(max_len - 1, -1, -1):
#         temp = carry
#         temp += 1 if binary1[i] == '1' else 0
#         temp += 1 if binary2[i] == '1' else 0
#         carry = 1 if temp >= 2 else 0
#         result = ('1' if temp % 2 == 1 else '0') + result
#     if carry != 0:
#         result = '1' + result
#     if len(result) >= 72 and has_fraction:
#         result = result[-(max_bits*2):]
#     elif len(result) >= 36 and not has_fraction:
#         result = result[-max_bits:]
#     result = f'{result[:dot]}.{result[dot:]}' if has_fraction else result
#     if has_fraction:
#         result = result.split('.')[0] if '1' not in result.split('.')[1] else result
#     return result


# print(binary_addition('111111111111111111111111111111101010.0', '000000000000000000000000000000101100.1'))
