# Убрать знаки припинания
# Убрать пробелы
# Сдела все буквы малыми
# Проверить

import string


def is_palindrome(text):
    wor_1 = text.translate(str.maketrans("", "", string.punctuation))
    wor_2 = wor_1.replace(" ","")
    wor_3 = wor_2.lower()
    if wor_3[::-1] == wor_3:
        return True
    else:
        return False
print(is_palindrome("aurora"))
