import requests
from bs4 import BeautifulSoup
import pprint
 #сначала первая страница новостей
domain = 'https://www.antibiotic.ru/news/'

url = f'{domain}'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
#получаем ссылки на следующие страницы
links = soup.find_all('div',class_="b-pageline")
link_list = links[0].find_all('a')
print(len(link_list))

#список адресов следующих страниц
href_list = []
for link in link_list:
    href = link.get('href')
    href_list.append(href)
print(href_list)

#почему то там повторения, убираем их
href_list = href_list[1:4]
print(href_list)

#парсим первую страницу
data = []
title = []
text = []
data_news = soup.find_all('div', class_="news__date")
title_news = soup.find_all('div', class_='news__title')
text_news = soup.find_all('div', class_="b-editor")
for j in range(len(data_news)):
    data.append(data_news[j].text)
for k in range(len(title_news)):
    title.append(title_news[k].a.text)
for m in range(len(text_news)):
    text.append(text_news[m].text)
# print(data)
# print(title)
# print(text)
#проходим по адресам последующих страниц и повторяем процедуру с каждой
domain1 = 'https://www.antibiotic.ru'
for i in range(len(href_list)):
    url1 = f'{domain1}{href_list[i]}'

    response = requests.get(url1)
#
    soup = BeautifulSoup(response.text, 'html.parser')
    data_news = soup.find_all('div', class_="news__date")
    title_news = soup.find_all('div', class_='news__title')
    text_news = soup.find_all('div', class_="b-editor")
    for j in range(len(data_news)):
         data.append(data_news[j].text)
    for k in range(len(title_news)):
        title.append(title_news[k].a.text)
    for m in range(len(text_news)):
        text.append(text_news[m].text)

#собранные списки данных помещаем в словарь, из него потом можно что-то сделать
result = {}
result['data'] = data
result['title'] = title
result['text'] = text
key_text = 'ВОЗ'

response = []
for i in range(len(result['data'])):
    if key_text.lower() in result['title'][i].lower() or key_text.lower() in result['text'][i].lower():
        newsdata = result['data'][i]
        newstitle = result['title'][i]
        newstext = result['text'][i]
        reply = f'{newsdata}. {newstitle}. {newstext}'
        response.append(reply)
print(response)
        # print(result['data'][i], result['title'][i], result['text'][i])




