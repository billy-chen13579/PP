
arr1 = [2, 4, 6, 8, 10]
str1 = 'hello python'

x=[]
for i in range(10):
    x.append(i)
print(x)
print('***\n')

y=[]
for i in range(len(arr1)):
    y.append(arr1[i])
print(y) #print(arr1[index]) 以index的順序印出容器中的數字
print('***\n')

d=[]
for i in arr1:
    d.insert(0,i) #不能用append，因爲型態不符合
d.reverse() 
print(d)
print('***\n')

#要集結成List的話概念和前一個一樣
for i in str1:
    print(i)
print('***\n')

for i in arr1:
    i += 1
print(arr1) #會印出arr1，因為不是印i
print(i) #i=11，因為跑完迴圈後最後的i是10+1，也就是11

arr2=[]
h=(1,2,3,4,5,6)
arr2.append(h)
print(arr2)
