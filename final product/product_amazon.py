from bs4 import BeautifulSoup as be
import requests as req
try:
    text = input(':')
    text = text.replace(' ', '+')
    URL = f'https://www.amazon.com/s?k={text}&dc&language=zh_TW&crid=2WOL9MPEXS5MO&sprefix={text}%2Caps%2C265&ref=a9_sc_1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = req.get(URL, headers=headers)

    soup1 = be(page.content, "html.parser")

    soup2 = be(soup1.prettify(), "html.parser")

    titles = soup2.find_all('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
    for i in titles:
        print(str(i.span.string))
        x = 'https://www.amazon.com' + i['href']
        print(x)
        
        new_content = req.get(x, headers = headers)
        
        new_page = be(new_content.content,'html.parser')
        try:
            price = new_page.find('td', class_='a-span12')
            price = price.find('span', class_='a-offscreen')
            print(str(price.string))
        except:
            print('沒貨')
        
        question = int(input('要看更多資訊嗎(1=yes, 2=no):'))
        
        if question == 1:
            arr_tree1 = []
            arr_info = []
            info = new_page.find('table', class_='a-normal a-spacing-micro')
            tree = info.find_all('tr')

            for i in tree:
                td_tree = i.find_all('td')
                arr_tree1.append([])
                length = len(arr_tree1)-1
                for i in td_tree:
                    x = str(i.span.string)
                    arr_tree1[length].append(x)
            
            for i in arr_tree1:
                x = str(i[0])
                y = str(i[1])
                xy = x+": "+y
                arr_info.append(xy)
        
            for i in arr_info:
                print(i)
        else:
            pass
        
        question2 = int(input("關於此商品的資訊((1=yes, 2==no)):"))
        if question2 == 1:
            arr_tree1 = []
            
            info = '關於此商品'
            arr_tree1.append(info)
            
            more_info = new_page.find('ul', class_='a-unordered-list a-vertical a-spacing-mini')
            span = more_info.find_all('span', class_='a-list-item')
            for i in span:
                x = str(i.string)
                if x == 'None':
                    continue
                x = '->'+x
                arr_tree1.append(x)
            
            for i in arr_tree1:
                print(i)
            
        break
except:
    print('error')