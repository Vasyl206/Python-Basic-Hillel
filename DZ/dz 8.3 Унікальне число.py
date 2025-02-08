

def find_unique_value(some_list):
    unique_numbers = [num for num in some_list if some_list.count(num) == 1]
    return unique_numbers

print(find_unique_value([5, 5, 5, 2, 2, 0.5]))

