import string

ferst_letter = input("Введіть букву: ")
sacond_letter = input("Ведіть букву: ")

letters = string.ascii_letters

letter_1 = letters.index(ferst_letter)
letter_2 = letters.index(sacond_letter)

if letter_1 <= letter_2:
    print(letters[letter_1:letter_2 + 1])
else:
    print(letters[letter_2:letter_1 + 1])

