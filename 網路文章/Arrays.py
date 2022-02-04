# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

a=[1,2,3,4,5,6,7,8]
a.append(3)
print(a)

# a.clear()
# print(a)

x=a.count(4) #print out how many "x" is in the list
print(x)

po=["BMW","Benz","Audi"]
a.extend(po) #原列表.extend.要追加的列表
print(a)

e=a.index(3) #print the index of the "x"
print("index:",e)

a.sort 
print(a)