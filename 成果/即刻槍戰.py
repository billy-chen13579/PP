import urllib.request as req
url="https://www.gunsrush.com/gunsrush/index.php?op=a03&guns=%E6%AD%A5%E6%A7%8D"
request=req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
#print(data)

from bs4 import BeautifulSoup as by #注意BeautifulSoup 大寫的字母
con=by(data, "html.parser")
contents=con.find_all("div",class_="GUNS_NAME")

arr=[]
for content in contents:
    x=content.string
    arr.append(x)

ac=[]
cont=con.find_all("tr")
for conn in cont:
    y=conn.td.string
    ac.append(y)

arr1=[]
for i in range(1,7):
    x=ac[i]
    arr.append(x)

arr2=[]
for cot in cont:
    co=cot.find_all("div")
    arr2.append(co)

for i,o,q in zip(arr,ac,arr2):
    print(i,"-->",o,"--->",q)
