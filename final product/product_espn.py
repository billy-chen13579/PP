from bs4 import BeautifulSoup as be
import requests as req

text = input('which year?')

url = f'http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/{text}/order/true'

content = req.get(url).content

html = be(content, 'lxml') 
names = html.find_all('div', class_='name')

x=1
for name in names:
    print(x, '-->', name.a.strong.string)
    player = name.a['href']
    
    player_content = req.get(player).content
    player_html = be(player_content, 'lxml')
    
    bio = player_html.find('div', class_='bio')
    bio = bio.p.string
    
    print(bio)
    
    rate = player_html.find('ul',class_='mod-rating')
    rates = rate.find_all('li')
    
    z = 0
    for i in rates:
        if z==0:
            print('rate:', i.string)
        elif z==1:
            star = i.attrs.get('class')
            print(star[1])
        z+=1
    
    bio = player_html.find('div', class_='bio')
    infos = bio.find('ul')
    infos = infos.find_all('li')
    
    for info in infos:
        try:
            print(info.span.string, ":", info.a.string)
        except:
            pass
    
    x+=1
