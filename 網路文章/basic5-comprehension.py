ar1=[]
for x in range(10):
    ar1.append(x)
print(ar1) #不能在迴圈裡面，不然每跑一次迴圈就會印出一次

#list comprehension
arr1=[i for i in range(10)] #用list括號
print(arr1)

# in-place construction
arr1 = [i for i in range(10)]

# you can use if to filter the elements
arr2 = [x for x in arr1 if x % 2 == 0]

# you can use as many conditions as you want!
arr3 = [x for x in arr1 if x >= 3 and x % 2==0]

# use nested for loops to make everyone dizzy XD
arr4 = [(x, y) for x in range(3) for y in range(4)]

print(arr1)
print(arr2)
print(arr3)
print(arr4)