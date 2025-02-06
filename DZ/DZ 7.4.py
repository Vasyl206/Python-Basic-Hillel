def common_elements():
    multiples_of_3 = {x for x in range(100) if x % 3 == 0}  # Числа, кратні 3
    multiples_of_5 = {x for x in range(100) if x % 5 == 0}  # Числа, кратні 5

    return multiples_of_3 & multiples_of_5

print(common_elements())