# File 實體物件的設計：包裝檔案讀取的程式
#記得呼叫時要加()
#使用類別將複雜的步驟綁近一個函示，在呼叫函示，就能輕鬆重複服在的動做
class File:
    def __init__(self,name):
        self.name=name
        self.file=None
    def open(self):
        self.file=open(self.name,mode="r",encoding="utf-8") #檔案位置用self.name，可以輸入不同檔案
    def read(self):
        return self.file.read()
#讀取第一個檔案
# f1=File("data.txt") #將name綁到"data.txt"上，在傳道self.name和實體方法
# f1.open()
# data=f1.read()
# print(data)

# print("***\n")
# #讀取第二個檔案
# f2=File("121.txt")
# f2.open()
# data2=f2.read()
# print(data2)

x=int(input("how many files:"))

for i in range(1,x+1):
    f3=File(str(input("choose a file:")))
    f3.open()
    data3=f3.read()
    print(data3)