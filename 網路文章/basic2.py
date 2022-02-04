s=[2,3,4,3,5,6,7] #s容器
x=3 #x元素
print(x in s) #確認元素是否在容器當中
print(x not in s) #確認元素是否(不)在容器當中

t=[1,2] #容器
print(t+s) #容器的內容相加，有順序性

print(len(s)) #檢查s容器中有幾個元素
print(min(s)) #選出s容器中的最小值
print(max(s)) #選出s容器中的最大值

dec=s.index(x) #s容器必須為可動列表[]
print(dec) #尋找x元素在s容器中的索引值（號碼）

print(s.count(x)) #寫出x元素在s容器中出現幾次
