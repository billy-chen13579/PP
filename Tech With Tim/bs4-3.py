from bs4 import BeautifulSoup as beau
import requests

url = 'https://coinmarketcap.com/'

result = requests.get(url).text
doc = beau(result, 'html.parser')

name = doc.find_all(text = 'Bitcoin')
x = name[0].parent
print(list(x.parent))

#12/14 完成自動搜尋貨幣名城並得到其資訊