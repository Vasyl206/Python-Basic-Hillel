import string
import keyword

wor = input("Введіть ім'я змінної для перевірки: ")
wor_2 = keyword.kwlist

if "__" in wor or "___" in wor:
    print(False)
elif " " in wor:
    print(False)
elif any(char in string.punctuation and char != "_" for char in wor): # Я більше години намагався совмістить if з другим elif. Але думаю в мене вдалося
    print(False)
elif wor in wor_2:
    print(False)
if any(char.isupper() for char in wor):
    print(False)
if wor[0].isdigit():
    print(False)
else:
    print(True)


