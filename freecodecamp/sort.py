d={
    "a":10,
    "b":1,
    "c":22
}
print(d.items()) #dict_items([('a', 10), ('b', 1), ('c', 22)])
data=sorted(d.items()) #follow alphbatic order based on the "key"
print(data)

for k,v in data:
    print(k,v)

temp=[]
for key,val in d.items():
    temp.append((val,key))
print(temp)

x=sorted(temp,reverse=True) #first sort it by the number order, then reverse the key
print(x)

#show the top 10 uses words in the article
hand=input("start:")
count={}
words=hand.split()
for word in words:
    count[word]=count.get(word,0)+1
lst=[]
for k,v in count.items():
    newup=(v,k) #把key跟value調換，這樣才能sort數字，得到單字對應的數字
    lst.append(newup)
lst=sorted(lst,reverse=True) #先從小排到大，在調換順序，從最大排到小
for val,key in lst[:10]: #取出lst中的前十項
    print(key,val) #將key跟value的對應變回正常模式