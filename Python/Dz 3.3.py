
def second_index(text, some_str):
    first = text.find(some_str)
    if first == -1:
        return None

    second = text.find(some_str, first + 1)
    return second if second != -1 else None
print(second_index("find the river", "e"))
