# use inheritance method when different class has similar function
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f'I am {self.name} and I am {self.age} years old')
    
    def speak(self):
        print("I do not have my own function")
class Dog(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age) # super() is equal to the class that we inherited, which is class Pet. This line is same as self.name = name ; self.age= age
        self.color = color 
        
    def speak(self):
        print("bark")
    
    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and I am {self.color} \n')
        
class Cat(Pet):
    def speak(self):
        print("Meow")
    
class Fish(Pet):
    pass

c = Cat("bill",23)
c.speak()
c.show()
d = Dog("jill", 34, "Brown")
d.speak()
d.show()
f = Fish("sill",30)
f.speak() #the speak function here is using the one in the class Pet, because there is no indivisual speak function in class Fish
f.show()
