import urllib.request as req
url="http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2023"
root=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
})
with req.urlopen(root) as re:
    data=re.read()

from bs4 import BeautifulSoup as be
espn=be(data, "html.parser")
es=espn.find_all("div", class_="name")

arr=[]
arr1=[]
arr2=[]
short=[]
tall=[]
for i in es:
    x=i.strong.string
    arr2.append(x) #contain name
    links=i.find_all("a")
    for link in links:
        arr.append(link) #contain "a"
q=len(arr)
for i in range(q): #過濾多餘的連結
    if i<31 and i%3==0:
            arr1.append(arr[i])
    if i>33 and i%3==1:
        arr1.append(arr[i])
arr3=[]
for ih in arr1:
    yz=ih["href"]
    arr3.append(yz) #只取用"href"連結
k=len(arr3)
for u in range(60):
    g=arr3[u]    #第二層爬蟲
    ro=req.Request(g, headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
    })
    with req.urlopen(ro) as ry:
        da=ry.read()
    player=be(da,"html.parser")
    pl=player.find("div", class_="bio")
    r=pl.p.string
    d=r.split()
    h=arr2[u]
    f=d[0]
    q=f.split("-")
    o=q[0]
    o=int(o)*30.48
    e=q[1]
    e=e.split(",")
    e=e[0]
    e=int(e)*2.54
    f=o+e
    if f<=200:
        short.append(h)
    elif f>200:
        tall.append(h)
    g=d[1]
    if g=='|':
        g="none"
        b=g
    else:
        g=int(g)
        b=g*0.454
    print(h,": has the height:",f, "and the weight:",b)
print("player under 200cm:",short,"\n")
print("player over 200cm:",tall)

#11/2進度
#11/3：用網址做二次爬蟲，爬取到球員名字，體重和身高
#11/4:分類不同球員的資料，將身高體重的單位轉換為公分和公斤
#11/5:整理編碼








