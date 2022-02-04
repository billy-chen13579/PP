from bs4 import BeautifulSoup
import requests

key_words = input('what do you want to search for?')

url = f'https://ecshweb.pchome.com.tw/search/v3.3/?q={key_words}&scope=all'


data = requests.get(url).text

html = BeautifulSoup(data,'lxml')

product_names = html.find_all('h5', class_='prod_name')

for i in product_names:
    print(i)
    break