def welcome_message():
    print("Welcome to DigitDazzle")

def binary_operations_menu():
    print("\nBINARY OPERATIONS\n")
    print("[1] Division")
    print("[2] Multiplication")
    print("[3] Subtraction")
    print("[4] Addition")
    print("[5] Negative (2's Complement)")
    print("[6] Back")

def conversion_menu():
    print("\nCONVERSION\n")
    print("[1] Binary to X")
    print("[2] Decimal to X")
    print("[3] Octal to X")
    print("[4] Hexa to X")
    print("[5] Back")

def main_menu():
    welcome_message()

    while True:
        print("\nMAIN MENU\n")
        print("[1] Binary Operations")
        print("[2] Number System Conversion")
        print("[3] Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            binary_operations()
        elif choice == '2':
            number_system_conversion()
        elif choice == '3':
            print("DigitDazzle is exiting....")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def binary_operations():
    while True:
        binary_operations_menu()
        operation_choice = input("Enter your selected option: ")

        if operation_choice == '1':
            # Perform Division
            perform_binary_operation(binary_division)
        elif operation_choice == '2':
            # Perform Multiplication
            perform_binary_operation(binary_multiplication)
        elif operation_choice == '3':
            # Perform Subtraction
            perform_binary_operation(binary_subtraction)
        elif operation_choice == '4':
            # Perform Addition
            perform_binary_operation(binary_addition)
        elif operation_choice == '5':
            # Perform Negative (2's Complement)
            perform_binary_operation(twos_complement)
        elif operation_choice == '6':
            break
        else:
            print("Invalid. Please enter a valid option.")

def perform_binary_operation(operation_function):
    binary_input_value = binary_input()
    print(n_bit_spacer(make_32_bits(binary_input_value)))
    print(operation_function(binary_input_value))

def number_system_conversion():
    while True:
        conversion_menu()
        conversion_choice = input("Enter your selected option: ")

        try:
            if conversion_choice == '1':
                perform_conversion(binary_to_decimal, "Decimal")
            elif conversion_choice == '2':
                perform_conversion(decimal_to_binary, "Binary")
            elif conversion_choice == '3':
                perform_conversion(binary_to_octal, "Octal")
            elif conversion_choice == '4':
                perform_conversion(binary_to_hexa, "Hexadecimal")
            elif conversion_choice == '5':
                break
            else:
                print("Invalid option. Please enter a valid choice.")
        except (ValueError, TypeError):
            print("Invalid input. Please enter valid numbers.")

def perform_conversion(conversion_function, output_label):
    binary_input_value = binary_input()
    print(n_bit_spacer(make_32_bits(binary_input_value)))
    result = conversion_function(binary_input_value)
    print(f"The {output_label} equivalent of {binary_input_value} is: {result}")

# Include these functions for conversion
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    return n_bit_spacer(make_32_bits(binary))

# Replace these functions with the provided ones
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

def twos_complement(binary: str = None):
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
    main_menu()