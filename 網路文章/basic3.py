s=[1,2,3,4,5,6,7,8,9,10]
print(s)

s[0]=3
print(s)

s[0:3]=4,5,6,7
print(s)

del s[0:2]
print(s)

del s[0:6:2] #s[0(起):6(終):2(間隔)]
print(s)

s.append(5) #後面的元素只能有一個，或是用代數表示
print(s)

#s.clear() #全刪除
#print(s) #只剩下()

s.copy() #重新印製一次
print(s)

s+=[5,6,7]
print(s)

are=s[:]
print(are)
print(are is s)

s.insert(5,4) #在S容器index為i的位置將X插入，原有的元素(們)將會往後移 #s.insert(i,x)
print(s)

s.pop(4) #將index為i的元素取出，並將其移出容器
print(s)

s.remove(7) #刪除第一個找到的X，這個x是數字不是index
print(s)

s.reverse() #讓容器的內容順序顛倒
print(s)

x = [1,2,3,4,5]
print(x.index(4))