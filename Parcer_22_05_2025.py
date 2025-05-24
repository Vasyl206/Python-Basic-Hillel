import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin
from fake_useragent import UserAgent


url = 'https://books.toscrape.com/'
books_data = []
ua = UserAgent()

page_num = 1

while url:
    headers = {"User-Agent": ua.random}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Парсим
    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        prices = book.find('p', class_='price_color').text
        rating_tag = book.find('p', class_="star-rating")
        rating_class = rating_tag['class']
        rating = rating_class[1]
        link = book.h3.a['href']
        link_url = urljoin(url, link)


        books_data.append({
            "Title": title,
            "Price": prices,
            "Rating_star": rating,
            "Link": link_url
        })
    print(f"✅ Страница {page_num} обработана: {url}")
    page_num += 1
    # Находим ссылку на следующую страницу
    next_tag = soup.find('li', class_='next')
    if next_tag:
        next_href = next_tag.select_one('a')['href']
        url = urljoin(url, next_href)
    else:
        url = None

#Сохранение в таблицу
df = pd.DataFrame(books_data)
df.to_csv("books.csv", index=False, encoding="utf-8-sig", sep=';')
print("Good")

