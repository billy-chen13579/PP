import urllib.request as req

search = input('What do yoy want to search for?')
url = f'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={search}&page=1&sort=sale/dc'

root = req.Request(url, headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
})

with req.urlopen(root) as re:
    data = re.read().decode('utf-8')
    
import json
data = json.loads(data)

product = data['prods']
for i in range(1,20):
    p1 = product[i]
    print(p1['name'],"--->", p1['originPrice'], '\n')