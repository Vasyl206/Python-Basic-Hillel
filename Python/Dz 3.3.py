import string

print("Напишіть рядок для '#'")
wor = input(": ")

wor_1 = wor.title()

wor_2 = wor_1.replace(" ","")

wor_3 = wor_2.translate(str.maketrans("", "", string.punctuation))

wor_4 = "#" + wor_3

print(wor_4)
