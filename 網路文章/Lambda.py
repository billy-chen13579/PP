x=lambda a:a**2
print(x(5))  #lambda function, the x input will run the lambda function

x=lambda a,b,c:(a+b)*c
print(x(2,3,4)) 

#two functions
def myfunc(n):
  return lambda a : a * n  #mydoubler=lambda a:a*n
#a is the input of lambda function, and n is the input of def function

mydoubler = myfunc(2) #state: n==2, but a is still unknown

print(mydoubler(11)) #state: a==11


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2) #output=a*2, which "a" equal to mydoubler(x) input
mytripler = myfunc(3) #output=a*3, which "a" equal to mytripler(x) input

print(mydoubler(11))
print(mytripler(11))