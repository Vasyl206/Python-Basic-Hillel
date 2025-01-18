#lst = [1, 2, 3, 4, 5, 6]

#lst = [1, 2, 3]

#lst = [1, 2, 3, 4, 5]

#lst = [1]

#lst = []

my_lst = (len(lst) + 1) // 2
my_super_lst = [lst[:my_lst], lst[my_lst:]]
print(my_super_lst)