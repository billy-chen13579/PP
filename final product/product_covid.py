import requests as req 
from bs4 import BeautifulSoup as be

url = "https://www.worldometers.info/coronavirus/"

text = req.get(url).text

html = be(text, 'lxml')

content = html.find('tbody')
tr = content.find_all('tr')

datas = []
type = [
    'country: ',
    'Total Cases: ',
    'New Cases: ',
    'Total Deaths: ',
    'New Deaths: ',
    'Total Recovered: ',
    'New recovered: ',
    'Active Cases: ',
    'Serious Critical: '
]

for i in tr:
    datas_1 = []
    a = i.find('a')
    if a ==None:
        continue
    arr_data = []

    c = str(a.string)

    
    arr_data.append(c)
    
    td = i.find_all('td')
    for o in range(2,10):
        numbers = str(td[o].string)
        if numbers == 'None':
            numbers = '0'
        arr_data.append(numbers)
    
    for g in range(9):
        x = type[g]
        y = arr_data[g]
        xy = x+y
        if xy == 'Total Deaths:  ':
            xy = 'Total Deaths: 0'
        datas_1.append(xy)
    datas.append(datas_1)
print(datas)





