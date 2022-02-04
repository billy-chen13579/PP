#方法一：
arr1=[x for x in range(20) if x%2==1]
#同arr1 = [i for i in range(1, 21, 2)]

arr2=[x for x in range(1,21) if x%2==0]
#同arr2 = [i for i in range(2, 21, 2)]

#zip 函式： 將兩個容器以index分開，並將兩容器中同樣index的元素以(x,y)組合再一起
#如果其中一個容器的index比較多，以少的為主
for i,o in zip(arr1,arr2):
    print(i, "<--->", o)

print("*"*10)

#方法二：
arr1 = [i for i in range(1, 21, 2)]
arr2 = [i for i in range(2, 21, 2)]

for oi in range(len(arr1)): #以oi取代元素的長度，再以index[oi]的形式印出每一個容器的index個數
    print(arr1[oi], '<--->', arr2[oi])
