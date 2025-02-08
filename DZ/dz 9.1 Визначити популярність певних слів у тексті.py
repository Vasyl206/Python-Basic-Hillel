
#popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
# ['i', 'was', 'three', 'near'])
# { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }

# Сделать все слова в lower
# Если слово не найдено нужно его вернуть с 0 значением
# Посчитать каждое слово

from collections import Counter


def popular_words (text, words):
    text_1 = text.lower()
    text_2 = text_1.split() #разбивает строку на список слов, используя пробел как разделитель
    text_count = Counter(text_2) #считает каждое слово
    return {word: text_count.get(word, 0) for word in words}

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')








