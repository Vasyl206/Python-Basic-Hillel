number = int(input("Введіть 5-значне число: "))

a = number // 10000
b = number % 10000 // 1000
c = number % 1000 // 100
d = number % 100 // 10
e = number % 10 // 1

print(e * 10000 + d * 1000 + c * 100 + b * 10 + a)
