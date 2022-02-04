from bs4 import BeautifulSoup
import requests 
import re

search_term= input('what product do you want to seach for?')

url = f'https://www.newegg.com/p/pl?d={search_term}&Order=6'

page = requests.get(url).text

doc = BeautifulSoup(page, 'html.parser')    

page_text = doc.find('span', class_="list-tool-pagination-text")
real = int(str(page_text.strong).split('</')[-2].split('-->')[-1])
items_found = dict()

for p in range(1, real+1):
    url = f'https://www.newegg.com/p/pl?d={search_term}&Order=6'
    page = requests.get(url).text 
    doc = BeautifulSoup(page, 'html.parser')
    
    div = doc.find(class_='item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell')
    
    results = div.find_all(text = re.compile(search_term))
    for result in results:
        parent = result.parent
        if parent.name != 'a':
            continue
        link = parent['href']
        
        gpu_results = parent.parent
        container = gpu_results.parent
        prices = container.find('li', class_= 'price-current').strong.text
        
        items_found[str(result)] = {'price':'$' + str(prices), 'link': str(link)} #making a dictionary with another dictionary
        
sorted_item = sorted(items_found.items(), key = lambda x: x[1]['price'])

count = 0
for item in sorted_item:
    print(item[0])
    print(f'''${item[1]['price']}''')
    print(item[1]['link'])
    print('----------------------------')
    count+=1
    if count > 20:
        break