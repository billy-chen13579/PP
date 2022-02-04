sv=56
print(isinstance(sv, int))
#isinstance確認變數是否為特定格式，在後方輸入

for i in range(1,50,5):
    print(i)

t1 = 10, 20
# it can hold different types of data, tuple will use () to transform
t2 = 10, 'hello world'

print(type(t1))
print(t1)
print(t2)

arr1 = [1, 2, 3]
arr2 = [10, 'hello world', 8.7]
arr1[1] = [1, 2, 3]

print(type(arr1))
print(arr1)
print(arr2)

#index(索引)就是改別序列的其中一格元素，e.g. aaa[0]:(5,6,7) 也是在序列中的號碼
str1 = 'hello python'
str2 = str1
# a = a + b could be written as a += b
str2 += ' journey'
print(str2 is str1)
print(str1)
result = str2.split(' ')#將字拆散or組合(split or join)，並用'空白'(只能是這個符號''，在引號下方)隔開
print(result)
result_back = '##'.join(result)#將字拆散or組合(split or join)，並用***隔開
print(result_back)