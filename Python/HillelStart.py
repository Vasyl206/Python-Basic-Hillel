
def add_one(some_list):
    wor = "".join(map(str, some_list))  # Преобразуем числа в строку
    firstre_1 = int(wor)  # Преобразуем строку в число
    sakond_2 = firstre_1 + 1  # Добавляем 1
    tree = list(str(sakond_2))  # Преобразуем результат обратно в строку, потом в список
    return tree

print(add_one([1, 2, 3, 4]))