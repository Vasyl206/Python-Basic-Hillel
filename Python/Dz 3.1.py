#lst = [0, 1, 0, 12, 3]

#lst = [0]

#lst = [1, 0, 13, 0, 0, 0, 5]

#lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

if 0 in lst:
    for _ in range(lst.count(0)):
        lst.remove(0)
        lst.append(0)

print(lst)