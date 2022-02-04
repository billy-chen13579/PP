from tkinter import *

root = Tk()
root.title('menus')
root.geometry('500x500')

def show():
    mylabel = Label(root, text=clicked.get())
    mylabel.pack()
    
options = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday'
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked,*options)
drop.pack()

mybutton = Button(root, text='show', command=show)
mybutton.pack()

root.mainloop()