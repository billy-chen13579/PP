# F string
name = "Billy"
print(F'Hello {name} {[1,2,3]}')
x=F'''Hello {name}{' Billy'}'''
print(x)

# unpacking (work in any collection, such as the things below)
tup = (1,2,3,4,5)

list= [1,2,3,4,5]

string = "hello"

dic = {"a":1,"b":2}

coords = [4,5]

a,b,c,d,e = tup
print(a,b,c,d,e)

x=dic.keys()
y=dic.values()
print(x)
print(y)


# multiple assignment
width, height = 500,400
width, height = height, width # replace the new number
print(width, height)

#comprehensions
x=[x for x in range(100) if x %5 == 0]
print(x)
sentence = "hello my name is billy"
x = {char: sentence.count(char) for char in set(sentence)} # use set comprehensions
print(x)

#Ternary Conditions
x = 1 if 2 >3 else 0
print(x)

#For & While Else
search=[1,2,3,4,5,6,7]
target = 8
for element in search:
    if element == target:
        print('I found it!')
        break
else: # the else will run when the for loops doesn;t break 
    print("I didn;t find it!")

#Sort By Key
lst = [[1,2],[3,4],[4,2],[-1,3],[4,5],[2,3]]
lst.sort()
print(lst)
lst.sort(key=lambda x: x[0]+x[1]) # it will sorted by the order of the addition of list
print(lst)
o=[]
for i in range(len(lst)):
    y=lst[i][0]+lst[i][1]
    o.append(y)
print(o)
d = [3,5,2,6,12,35,2,6,3,5]
d=sorted(d)
print(d)

