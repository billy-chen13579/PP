#*args **kwargs
# def func(*args,**kwargs):
#     print(args)
#     print(kwargs)
#     print("hello")
# func("abc",123,[1,2,3,4],billy=123)

# def f2(**kwargs):
#     print("hello",kwargs)
# f2(key="value")

# def f3(x,*args):
#     print(x)
#     print("hello",args)
# f3(4,5,6)

def f4(abc=None,**kwargs):
    print(abc)
    print(kwargs)
    print("hello")
f4(123,key=123)
