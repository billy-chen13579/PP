#list comprehension VS 一般
import time
#測試用一般方式所算出來的時間
arr1 = []
s = time.time()
for i in range(int(5e+6)):
    arr1.append(i)
print("took {} secs".format(round(time.time() - s, 3)))

#測試用list comprehension 所算出來的時間
s = time.time()
arr2 = [i for i in range(int(5e+6))]
print("took {} secs".format(round(time.time() - s, 3)))
