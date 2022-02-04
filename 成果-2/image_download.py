import requests 
from bs4 import BeautifulSoup

url = 'https://statsroyale.com/cards'
page = requests.get(url)
souped = BeautifulSoup(page.content, 'html.parser')
imags = souped.find_all('img')


arr = []
for i in range(len(imags)):
    arr.append(i)

x=0
for img in imags:
    if img.attrs.get('class') != None or img.attrs.get('alt') != None:
        continue
    imglink=img.attrs.get('src')
    image = requests.get(imglink).content
    filename = '00'+str(arr[x])
    with open(filename+'.png', 'wb') as file:
        file.write(image)
    x+=1
    if x == 5:
        break