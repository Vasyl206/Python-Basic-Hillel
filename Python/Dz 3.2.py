#lst = [0, 1, 7, 2, 4, 8]

#lst = [1, 3, 5]

#lst = [6]

#lst = []

if sum(lst) == 0:
    print(sum(lst))
else:
    my_lst = lst[::2]
    uno = sum(my_lst) * lst[-1]
    print(uno)
