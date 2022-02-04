#print(type(1))
class Dog:
    def __init__(self, name, num):
        self.name = name
        self.num = num
    
    def bark(self):
        print("bark")
    
    def func(self):
        x = self.name
        arr=[]
        for i in x:
            g = i.lower()
            arr.append(g)
        arr1=[]
        for i in range(len(arr)):
            if i == 0:
                x = arr[i].upper()
                arr1.append(x)
            else:
                arr1.append(arr[i])
        string=str()
        for i in arr1:
            string += i
        return string
    
    def number_sort(self):
        arr=[]
        x = self.num
        for i in str(x):
            arr.append(i)
        arr.sort()
        string = ""
        for i in arr:
            string += i
        string = int(string)
        return string

# d = Dog("billy", 15)
# print(d.func())
# print(d.number())

dog_name = ["tim","billy"]
dog_num = [513545343, 2543653345]
for i,o, in zip(dog_name,dog_num):
    x = dog_name.index(i)
    d1= Dog(i,o)
    print(d1.func(), d1.number_sort ())
