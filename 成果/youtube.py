#using format function
from selenium import webdriver as web
from bs4 import BeautifulSoup as be
urls = int(input("how many channel do you want to scrape:"))

#https://www.youtube.com/channel/UCaO6VoaYJv4kS-TQO_M-N_g/videos?view=0&sort=p&flow=grid
#https://www.youtube.com/c/HOOKsan/videos?view=0&sort=p&flow=grid
#https://www.youtube.com/channel/UCpmx8TiMv9yR1ncyldGyyVA/videos?view=0&sort=p&flow=grid

path ="/Users/billychen/Desktop/chromedriver"

uu = []
for i in range(urls):
        i+=1
        url = input(f"your youtube channel {i}:")
        uu.append(url)
        
def main():
    for u in uu:
        driver = web.Chrome(path)
        driver.get(f'{u}')
        content = driver.page_source.encode('utf-8').strip()
        root = be(content, 'lxml')
        counts = root.find('yt-formatted-string',id="subscriber-count")
        for count in counts:
            string = count.string
        names = root.find('yt-formatted-string',class_="style-scope ytd-channel-name")
        for name in names:
            x = name.string
        print(f'Channel: {x} Subscriber: {string} \n')
        titles = root.find_all('a', id='video-title')
        arr4 = []
        for i in titles:
            x = "https://www.youtube.com" + i['href']
            arr4.append(x)
            
        arr1 = []
        for title in titles:
            arr1.append(title.string)
        views = root.find_all('span',class_="style-scope ytd-grid-video-renderer")
        arr = []
        for view in views:
            arr.append(view.string)
        arr2 = []
        arr3 = []
        for i in range(len(arr)):
            if i == 0 or i&2 == 0:
                arr2.append(arr[i])
            if i%2 == 1:
                arr3.append(arr[i])
        for x,y,z,q in zip(arr1,arr2,arr3,arr4):
            print(f'Video Title: {x} ---> Video Views: {y} ---> Video Data: {z} ---> Video Links: {q} \n')
main()