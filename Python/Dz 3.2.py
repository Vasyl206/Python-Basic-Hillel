# lst = [12, 3, 4, 10]
# my_lst = [lst[-1]] + lst[:-1]
# print(my_lst)
# lst = [1]
# my_lst = [lst[-1]] + lst[:-1]
# print(my_lst)
lst = []
my_lst = [lst[-1]] + lst[:-1]
print(my_lst)
# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10