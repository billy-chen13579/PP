#有序可變動列表 list
grade=[50,60,75,83,25]
grade[0]=55 #把編號0的位置改成55
grade=grade+[12,33] #列表串接，加上最後的數列
print(grade) #映出最後指令
length=len(grade)
print(length) #加上length，可以算出列表的長度
data=[[3,4,5],[6,7,8]] #雙列表
print(data) 
data[0][1]=[6,7,8] #列表層次
print(data)
#有序不可變動列表 tuple 
#tuple=(3,4,5)
#tuple不可更新數字編號
#tuple[0]=1 #錯誤：tuple（小括號）的資料不可變動，所以跑不出來
#print(tuple)
