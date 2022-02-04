import urllib.request as req
url="https://www.ptt.cc/bbs/Olympics_ISG/index.html"
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
})
with req.urlopen(request) as re:
    dat=re.read().decode("utf-8")
from bs4 import BeautifulSoup as be
oly=be(dat,"html.parser")
roots=oly.find_all("div", class_="title")
for root in roots:
    if root.a != None:
        print(root.a.string)