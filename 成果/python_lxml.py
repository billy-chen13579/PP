import urllib.request as req
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/movie/index.html'

root = req.Request(url, headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
})

with req.urlopen(root) as re:
    data = re.read().decode('utf-8')

html = BeautifulSoup(data, 'lxml')
title = html.find_all('div', class_='title')

# arr = []
# for i in range(len(title)):
#     new_title = title[i]
#     try:
#         links1 = new_title.a['href']
#         links = 'https://www.ptt.cc/' + links1
#         arr.append(links)
#     except:
#         continue

author = html.find_all('div', class_='author')

for i,o in zip(title,author):
    try:
        x = i.a.string
        links = i.a['href']
        links2 = 'https://www.ptt.cc/' + links
        print(x, '--->', o.string,'\n',links2)
    except:
        continue