from tkinter import *

root = Tk()
root.geometry('500x500')
def func1():
    print('successful click button1')
    
def func2():
    print('successful click button2')
    
def func3():
    print('successful click button3')
    
def func4():
    print('successful click button4')
    
button1 = Button(root, text = 'click1', command=func1)
button2 = Button(root, text = 'click2', command=func2)
button3 = Button(root, text = 'click3', command=func3)
button4 = Button(root, text = 'click4', command=func4)

#row = horizontal, column = vertical
button1.grid(row=0,column=0,padx = 30, pady = 20)
button2.grid(row=0,column=1,padx = 30, pady = 20)
button3.grid(row=1,column=0,padx = 30, pady = 20)
button4.grid(row=1,column=1,padx = 30, pady = 20)
root.mainloop()