import re
import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        text = file.read()

    text = re.sub(r'<.*?>', '', text)  # Удаляем HTML-теги
    text = '\n'.join(line for line in text.split('\n') if line.strip())  # Убираем пустые строки

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(text)

    print(f'Очищенный текст записан в {result_file}')


# Запускаем функцию для обработки draft.html
delete_html_tags('draft.html', 'cleaned.txt')
