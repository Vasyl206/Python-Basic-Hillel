num = int(input("Введіть число: "))

while num > 9:
    product = 1
    for digit in str(num):  # Розбиваємо число на цифри
        product *= int(digit)  # Перемножуємо всі цифри
    num = product  # Оновлюємо число новим значенням

print(num)  # Виводимо остаточний результат

