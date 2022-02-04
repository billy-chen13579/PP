import tkinter as tk

root = tk.Tk()
root.geometry('1000x600')
root.title('pages')

def tab1():
    def tab2():
        fm.destroy()
        fm2 = tk.Frame(root, bg = '#A52A2A', width=500, height=600-300)
        fm2.pack()
        label2 = tk.Label(fm2, text='this is second page')
        label2.pack()
        
        def back():
            fm2.destroy()
            tab1()
        
        button2 = tk.Button(fm2, text="back",command=back)
        button2.pack(side=tk.BOTTOM)
    
    fm = tk.Frame(root, bg = '#A52A2A', width=500, height=300)
    fm.pack()   
    label1 = tk.Label(fm, text='this os the first tab')
    label1.pack()

    button1 = tk.Button(fm, text = 'next', command=tab2)
    button1.pack(side=tk.BOTTOM)

tab1()

root.mainloop()