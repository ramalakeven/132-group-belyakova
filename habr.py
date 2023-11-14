
import requests
from bs4 import BeautifulSoup

link = "https://habr.com/ru/articles/top/weekly/"

response = requests.get(link)
html_code = response.text

soup = BeautifulSoup(html_code, 'html.parser')
h2_tags = soup.find_all('h2')
article_links = [tag.a['href'] for tag in h2_tags if tag.a]


for link in article_links:
    article_response = requests.get("https://habr.com" + link)
    article_html_code = article_response.text
    with open(link.split('/')[-2] + '.html', 'w', encoding="utf-8") as file:
        file.write(article_html_code)