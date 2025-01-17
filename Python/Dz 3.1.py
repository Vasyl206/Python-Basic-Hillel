print("Впишіть що ви хоите зробити")
print("Додати '+'")
print("Відняти '-'")
print("Помножити '*'")
print("Розділити '/'")
action = input("Введіть вашу дію: ")
first_number = int(input("Введіть перше число: "))
second_number = int(input("Введіть друге число: "))

if action == "+":
    print(first_number + second_number)
elif action == "-":
    print(first_number - second_number)
elif action == "*":
    print(first_number * second_number)
elif action == "/":
    if first_number == 0 or second_number == 0:
        print("Не правильне введення числа(На 0 не ділеться )")
    else:
        print(first_number / second_number)
else:
    print("Невірна дія")

