#定義類別，與類別屬性(封裝在類別中的變數和函示)
# 1. 定義類別
# 1.1 使用 class 建立類別
# 1.2 建立類別的屬性 ( 封裝在類別中的變數或函式 )
class i: #建立類別
    url=["website","name","creator"] #建立類別的內容
    def web(ur): #在類別內建立函式
        if ur not in i.url:
            print("not supported")
        else:
            print("this is the",ur) 

# 2. 使用類別的基本語法：類別名稱.屬性名稱
#使用類別
print(i.url)
i.web("website") #呼叫類別內的函式
i.web("internet") #呼叫函式內的if...else函式
