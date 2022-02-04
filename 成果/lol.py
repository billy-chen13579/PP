import urllib.request as req
url="https://na.op.gg/ranking/ladder/"
lol=req.Request(url, headers={
    "cookie":"_gid=GA1.2.176684151.1634878995; _clck=wit357|1|evs|0; wcs_bt=55c48ac9e22bec:1634879151; Hm_lvt_29884b6641f1b5709cc89a8ce5a99366=1634878994,1634879047,1634879151; Hm_lpvt_29884b6641f1b5709cc89a8ce5a99366=1634879151; _ga_HKZFKE5JEL=GS1.1.1634878994.1.1.1634879151.0; _ga=GA1.2.1288126061.1634878994; _ga_37HQ1LKWBE=GS1.1.1634878994.1.1.1634879153.0; _clsk=lrrv88|1634879153341|3|0|g.clarity.ms/collect"
})
with req.urlopen(lol) as opgg:
    data=opgg.read().decode("utf-8")
# print(data)

from bs4 import BeautifulSoup as by
root=by(data, "html.parser")
contents=root.find_all("a", class_="ranking-highest__name")
for content in contents:
    print(content.string)
