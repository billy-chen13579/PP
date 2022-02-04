#changing html
import urllib.request as req
from bs4 import BeautifulSoup as be

url = "https://kueishan.follettdestiny.com/common/servlet/presenthomeform.do?l2m=Home&tm=Home&l2m=Home"

root = req.Request(url, headers = {
    "Cookie": "JSESSIONID=rbnBDs4Eq5RT2o1FcgJRdujtQj5vdQCpkVALGXAE.pgrwcdstnyapp04; contextCookie=saas904_8512098; siteIDCookie=100",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
})
with req.urlopen(root) as r:
    data = r.read().decode("utf-8")

with open("kss.html", "w") as a:
    a.write(data)

with open("kss.html", "r") as r:
    data = be(r, "html.parser")
    
infos = data.find_all('a', target = '_window')
for info in infos:
    ii = info.string
    info.string = "information -- "+str(ii)
    
with open('kss.html','w') as w:
    w.write(str(data))