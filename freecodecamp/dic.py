#find the largest number
x=[3,5,7,9,23,5,2,4]
d=None
for i in x:
    if d is None or i > d:
        d=i
print(d)

#find the smallest number
d=None
for i in x:
    if d is None or i < d:
        d=i
print(d)

#dictionary
count=dict()
#print(count) #{}
co={"apple":2 , "banana":3, "orange":5, "rice":7}
for i in co:
    print(i) #print: apple, banana, orange, rice

for c,a in co.items():
    for i in range(a+1):
        x="-"*i
    print(f'{c} : {x}')

print(co.get("apple",0)) #get (apple) key 的 value. 如果沒有的話就回傳0


#word count
x=input("please")
count=dict()
x=x.split()
for word in x:
    count[word]=count.get(word,0)+1
q=0
for z,f in count.items():
    q+=f
print("words count:",q)
print(count)
