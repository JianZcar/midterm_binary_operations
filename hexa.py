def hexa_input(hexa: str = None):
    return input('Enter Hexadecimal -> ') if hexa is None else hexa


def is_hexa(hexa: str) -> bool:
    characters = "0123456789.abcdefABCDEF"
    if not any(hexa) or hexa.count('.') > 1:
        return False
    for char in hexa:
        if char not in characters:
            return False
    return True
