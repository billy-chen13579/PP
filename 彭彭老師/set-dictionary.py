#集合的運算
s1={3,4,5}
print(10 not in s1) #用in % not in 來確認資料是否在集合中
s1={3,4,5}
s2={4,5,6,7}
s3=s1&s2 #交集(&)，取兩個集合中相同的部分
print(s3)
s3=s1|s2 #聯集（符號為enter上方的直線），代表綜合兩個集合，但不重複取
print(s3)
s3=s1-s2 #差集，從s1中，減去和s2重疊的部分
print(s3)
s3=s1^s2 #反交集，取兩個集合中，不重疊的部分(不相同的部分)
print(s3)
s=set("hello") #set(字串)(拆解字串)(不取重複)
print(s)
print("a" in s) #可以看單字是否在字串之中
#字典的運算 key-value的配對
dic={"apple":"蘋果","me":"我","love":"愛"}
print(dic["apple"]) #讀取字典的語法： 字典名稱["任何一個key"]
print(dic["me"])
print(dic["love"])
dic["love"]="喜歡" #變更字典中的翻譯
print(dic["love"])
print("apple"in dic) #判斷單字是否在字典裡using in & not in #識別key
del dic["apple"] #刪除字典中的單字
print(dic)
dic={x:x*2 for x in [3,4,5]} #同樣的語法，以列表中的資料當基礎做運算
print(dic)
get={x:x**2 for x in (3,4)}
print(get)