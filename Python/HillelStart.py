from collections import Counter

text = "hello world hello python world python hello"
words = text.split()  # Разбиваем текст на слова
word_count = Counter(words)

print(word_count)