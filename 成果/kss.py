import urllib.request as req
url = "https://kueishan.follettdestiny.com/common/servlet/presenthomeform.do?l2m=Home&tm=Home&l2m=Home"
root = req.Request(url, headers = {
    "cookie":"JSESSIONID=EC99g0oQpiK__RtdnV89nBek9zZPdAFDOBgtmaC0.pgrwcdstnyapp04; contextCookie=saas904_8512098; siteIDCookie=100",
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36"
})
with req.urlopen(root) as re:
    data = re.read().decode("utf-8")

from bs4 import BeautifulSoup as be

kss = be(data, "html.parser")
names = kss.find_all("a", target="_window")
arr = []
arr1 = []
for name in names:
    x = name.string
    link = kss.find('a',string=str(x))
    urls = 'https://kueishan.follettdestiny.com/' + link['href']
    arr1.append(urls)
    arr.append(x)
# for i in range(len(urls)):
#     print(f'{arr[i]}\t{arr1[i]}')

cats = kss.find_all('td', class_="TableHeading2 tdAlignLeft")
for cat in cats:
    cat = str(cat)
    x = cat.split(">")
    y = x[3].split("\r")
    z = y[0].split("\xa0")
    print(z[1])