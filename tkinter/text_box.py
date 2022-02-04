from tkinter import *
import webbrowser
root = Tk()
root.title('textbox')
root.geometry('500x500')




mt_text = Text(root, width=60, height=20, font=('Helvetica',16))
mt_text.pack()

button_frame = Frame(root)
button_frame.pack()

def clear():
    mt_text.delete(1.0, END)

clear_button = Button(button_frame, text='Clear All', command=clear)
clear_button.grid(row=0, column=0)

def get():
    my_label.config(text=mt_text.get(1.0, END))

get_text = Button(button_frame, text='get text', command=get)
get_text.grid(row=0,column=1,padx=20)

def open():
    webbrowser.open('https://kueishan.managebac.com/student')
url_button = Button(button_frame, text='click me', command=open).grid(row=0,column=2,padx=20)

my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()