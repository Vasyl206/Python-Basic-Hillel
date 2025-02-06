number = int(input("Введіть 4-значне число: "))

a = number // 1000
b = number % 1000 // 100
c = number % 100 // 10
d = number % 10 // 1

print(a)
print(b)
print(c)
print(d)