import keyword
import string


def is_valid_variable(name):
    if name in keyword.kwlist:
        return False

    if ' ' in name:
        return False

    if name[0].isdigit():
        return False

    if any(char.isupper() for char in name):
        return False

    if any(char in string.punctuation for char in name) and "_" not in name:
        return False

    if name.count('_') > 1:
        return False

    return True


name = input("Введіть ім'я змінної: ")
print(is_valid_variable(name))
