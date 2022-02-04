#儲存檔案
#開啟檔案：檔案物件=open(檔案路徑,mode=開啟模式)
#開啟模式:讀取-r, 寫入-w, 讀寫-r+
#寫入檔案
#檔案物件.write
#關閉檔案
#檔案物件.close()
file=open("data.txt", mode="w", encoding="utf-8") #開啟 #會創造一個新的檔案
file.write('''Helloworld\nsecond\n這裡可以打中文，因為有加"utf-8"\n所以可以打中文''') #操作
file.close()

#如果要用中文，記得加上encoding="utf-8"

#最佳實務
#with open(檔案路徑,mode=開啟模式) as 檔案物件:
with open("121.txt",mode="w") as a:
    a.write("5\n3 ")
 
#讀取檔案
#檔案物件.read 
with open("data.txt", mode="r") as g: #不會創造新的檔案
    rog=g.read() #將g.read()放到變數rog之中
print(rog) 

print("\n *** \n")
#各行分別取：用for迴圈
#算 "121.txt" 每一行之中的數字相加
sum=0
with open("121.txt", mode="r") as a:
    for line in a: #將a內的每一行個別分開
        sum=sum+int(line)  
print(sum)


#使用Json格式讀取，複製檔案
#import json
#讀取到的資料＝json.load(檔案物件)


#寫入json資料
#json.dump(要寫入的資料(參數一),檔案物件(參數二))


