#先載入模組
#import urllib.request
#with request.urlopen(網址) as response:
#data=response.read()

#載網路上找資料，並將它轉持適合的格式
#大部分都適用json

#網路連線 (原始碼) #將網頁原始碼連線至程式
#import urllib.request as ur 
#uur="https://kueishan.managebac.com/student" #將網址綁在變數身上
#with ur.urlopen(uur) as response:   #標準語法
#    data=response.read().decode("utf-8")   #decode("utf-8")：解碼，加中文亂碼改成中文
#print(data) #取得的是網頁原始碼
 
#串接，擷取公開資料 用json格式的資料
import urllib.request as request
import json
lru="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(lru) as response:
    gov=json.load(response)  #用讀取json格式的方式

#擷取資料，取得公司名稱
#用檔案存取將資料寫在另一個檔案中
clist=gov["result"]["results"] #gov["result"]["results"]來自網址的json格式的key，呼叫key可以得到value
with open("公開資料.txt", mode="w", encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"--->"+company["公司地址"]+"\n") #這些key是來自於網站上寫的

