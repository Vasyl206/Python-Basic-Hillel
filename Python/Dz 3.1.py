
# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True


print("Перевірка чи може цей рядок бути ім'ям змінної")
world = input("Введіть рядок: ")

if "_" in world:
    print(world, "може пути змінною")
elif "__" or "___" in world:
    print("Це слово не може бути ім'ям змінної")


