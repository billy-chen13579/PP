#亂數模組
import random #先引入random模組
#隨機取得亂數
data=random.choice([1,2,3,4,6,7,9,4]) #隨機選取一個數,機率相同
print(data)
#隨機取得多個亂數
dat=random.sample([1,2,3,4,6,7,9,4],3) #隨機選取「三個數」,機率相同
print(dat)
#隨機打亂，洗牌
dta=[1,2,3,4,6,7]
random.shuffle(dta) #將dta容器，隨機調換順序，就像洗牌,容器一定要是單存的list
print(dta)
#隨機取得隨機取得0~1之間的亂數
x=random.random() #機率相同
print(x)
#隨機取得隨機取得x~y之間的亂數，可決定開頭，結尾
y=random.uniform(0.0,2.5) #機率相同
print(y)
#取得常態分配亂數
z=random.normalvariate(200,10) #random.normalvariate(平均值，間格差)
print(z)

#統計模組
import statistics as stat
#取得平均數
rog=stat.mean([1,2,3,4,5,6,7])
print(rog)
#取得中位數，跟平均很像，但是會排除極端的狀況
msi=stat.median([1,97,98,99,100,101,102,103,20000])
print("mis=",msi)
#標準差 #stardart deviation
razer=stat.stdev([1,2,3,4,5,8,10])
print(razer)

#平均數，中位數，標準差，常態分配