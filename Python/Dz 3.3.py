import random

list_length = random.randint(3, 10)

lst = []
for _ in range(list_length):
    lst.append(random.randint(1, 100))

t1 = lst[0]
t2 = lst[2]
t3 = lst[-2]

lst_2 = [t1, t2, t3]
print(lst_2)
print(lst)
