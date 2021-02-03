import pandas as pd
import requests
from bs4 import BeautifulSoup

source = requests.get("https://www.bookdepository.com/bestsellers").text
soup = BeautifulSoup(source, "html.parser")
hotKeys = soup.find_all("div", class_="item-info")

metaURL = "https://www.bookdepository.com"

index = 0
result = []
for key in hotKeys:
    index += 1
    title = key.h3.a.text.strip()
    author = key.find("p", class_="author").text.strip()
    try:
        price = key.find("p", class_="price").text.split('\n')[1].strip()
    except AttributeError:
        price = "not found"

    line = [index, title, author, price]
    result.append(line)
    if index > 19:
        break

result = pd.DataFrame(result, columns=['index', 'title', 'author', 'price'])
result.to_csv('210203_bookCsv.csv', index=False, encoding='utf-8')

##test
