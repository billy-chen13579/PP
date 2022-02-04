#上
# 1. 利用類別定義產生實體物件 (Instance Objects)
# 1.1 建立初始化函式、使用 self
# 1.2 建立實體物件
# 1.3 在初始化函式中，代入參數

# 2. 操作實體物件屬性
# 2.1 基本語法：實體物件.實體屬性名稱
# 2.2 相同類別定義下，不同的實體物件操作

# class Point:
#     def __init__(self): #固定語法
#         self.x=4
#         self.y=5
# p1=Point()
# print(p1.x,p1.y)

class Person:
    def __init__(self, name, age, hobby, sport, game):
        self.name=name
        self.age=age
        self.hobby=hobby
        self.sport=sport
        self.game=game

a=Person("Billy",15,"Code","basketball","clash royal") #輸入物件資料
print(a.name, a.age) #取得特定的物件資料

b=Person("Tom",30,"sleep","none","osu")
print(b.name, b.game, b.sport)


#下
# 1. 利用類別定義產生實體物件 (Instance Objects)
# 1.1 建立初始化函式、使用 self
# 1.2 建立實體物件、建立實體屬性
# 1.3 建立實體方法 / 函式、使用 self

# 2. 操作實體方法
# 2.1 基本語法：實體物件.實體方法名稱(參數資料)
# 2.2 相同類別定義下，不同的實體物件操作

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    #實體方法
    def show(self):
        print(self.x,self.y)
    def distance(self, x2, y2):
        return (((self.x-x2)**2)+((self.y-y2)**2))**0.5
        #print((((self.x-x2)**2)+((self.y-y2)**2))**0.5) 也可以

p=Point(3,4) #設定x和y
p.show() #呼叫函示，函式內容用前面的p
result=p.distance(5,8)
print(result)