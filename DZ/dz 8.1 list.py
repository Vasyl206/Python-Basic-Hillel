# assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
# assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
# assert add_one([0]) == [1], 'Test3'
# assert add_one([9]) == [1, 0], 'Test4'


def add_one(some_list):
    wor = int("".join(map(str, some_list)))
    firstre_1 = int(wor)
    sakond_2 = firstre_1 + 1
    tree = str(sakond_2)
    tree_1 = list(tree)
    return tree_1

print(add_one([9]))
