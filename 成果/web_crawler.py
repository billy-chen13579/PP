#擷取ppt電影版的網頁原始碼(HTML)
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
request=req.Request(url, headers={
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
# print(data) #印處程式碼

#解析原始碼，取得每篇文章的標題
#兩種寫法
#import bs4
#fin=bs4.Beautifulsoup(data, "html.parser")
from bs4 import BeautifulSoup as by 
fin=by(data, "html.parser") #(資料(data), 格式型態(html))
print(fin.title.string) #運用beautifulsoup4 套件來從資料中讀取特地標籤(title)中的內容(string) #需要先了解html格式
print("\n***")

# content=fin.find("div", class_="title") #透過bs4模組的find功能，尋找class="title"的div標籤  #要學會看html格式的標籤
# print(content.a.string) #在html中，div裡有a，印出a之中的文字 #只會印出第一個
# print("\n***")

contents=fin.find_all("div", class_="title") #透過bs4模組的find功能，尋找class="title"的div標籤  #要學會看html格式的標籤
#print(contents) #在html中，div裡有a，印出a之中的文字 #會印出所有的，因為有find_all #這裏不能用.a.string，因為有一些例外（被刪除的文章)
#contents是以列表型態印處

#將被刪除的標題過濾
for con in contents: #因為contents是一個列表
    if con.a != None: #因為被刪除的文章會沒有a標籤，所以只要有a標前的就印出來，這樣就能擷取我們要的資料
        print(con.a.string)

#將爬取到的資料印在一個新的檔案上
with open("web.txt", mode="w", encoding="utf-8") as a:
    for con in contents: 
        if con.a != None: 
            x=con.a.string
            a.write(x)
            a.write("\n") 