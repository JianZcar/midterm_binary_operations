from binary import (binary_input, n_bit_spacer, make_n_bits, twos_compliment, binary_to_decimal, binary_to_octal,
                    binary_to_hexa)
from decimal import (decimal_input, decimal_to_binary, decimal_to_octal, decimal_to_hexa)
from octal import (octal_input, octal_to_binary, octal_to_decimal, octal_to_hexa)
from hexa import (hexa_input, hexa_to_binary, hexa_to_decimal, hexa_to_octal)
from binary_operations import binary_addition, binary_subtraction, binary_multiplication


def null():
    # this does nothing, it's for the ide to not display error in the imports
    a = (binary_input, n_bit_spacer, make_n_bits, twos_compliment, binary_to_decimal, binary_to_octal, binary_to_hexa)
    b = (decimal_input, decimal_to_binary, decimal_to_octal, decimal_to_hexa)
    c = (octal_input, octal_to_binary, octal_to_decimal, octal_to_hexa)
    d = (hexa_input, hexa_to_binary, hexa_to_decimal, hexa_to_octal)
    return [a, b, c, d]


def main_menu():
    while True:
        print("\nMain Menu:")
        choices = ["Binary Operations", "Number Conversion", "Exit"]
        [print(f"{num}. {choice}") for num, choice in enumerate(choices, 1)]
        choice = int(input("--> "))
        print()
        [number_operation, number_conversion, exit][choice-1]()


def number_operation():
    while True:
        choices = ["Addition", "Subtraction", "Multiplication", "Division", "Back"]
        [print(f"{num}. {choice}") for num, choice in enumerate(choices, 1)]

        choice = int(input("--> "))

        match choice:
            case 1:
                print(n_bit_spacer(binary_addition()))
            case 2:
                print(n_bit_spacer(binary_subtraction()))
            case 3:
                print(n_bit_spacer(binary_multiplication()))
            case 4:
                pass
            case 5:
                break

        input("\nPress Enter to Continue\n")


def number_conversion():
    while True:
        choices = ["Binary Conversions", "Decimal Conversions", "Octal Conversions", "Hexa Conversions", "Back"]
        definitions, proper_names = (["binary", "decimal", "octal", "hexa"],
                                     ["Binary", "Decimal", "Octal", "Hexadecimal"])
        [print(f"{num}. {choice}") for num, choice in enumerate(choices, 1)]
        choice = int(input("--> "))

        if choices[choice-1] == 'Back':
            break

        removed_chosen, removed_proper = definitions.copy(), proper_names.copy()
        removed_chosen.pop(choice - 1), removed_proper.pop(choice - 1)
        print()
        input_num = eval(f"{definitions[choice-1]}_input")()
        outputs = [(eval(f"{definitions[choice-1]}_to_{system}")(input_num), system) for system in removed_chosen]

        [print(f"{removed_proper[index]}: {n_bit_spacer(output[0])}") if removed_proper[index] == "Binary"
         else print(f"{removed_proper[index]}: {output[0]}") for index, output in enumerate(outputs)]
        input("\nPress Enter to Continue\n")


main_menu()
