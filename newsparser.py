import requests
from bs4 import BeautifulSoup
import pprint

domain = 'https://www.antibiotic.ru'
url = f'{domain}/news'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


data = []
text = []
data_news = soup.find_all('div',class_="news__date")
# print(data_news[2].text)
# print(len(data_news))
text_news = soup.find_all('div',class_="b-editor")
for i in range(len(data_news)):
    data.append(data_news[i].text)
for j in range(len(text_news)):
    text.append(text_news[j].text)
# print(data)
# print(text)
result = dict(zip(data, text))
pprint.pprint(result)




