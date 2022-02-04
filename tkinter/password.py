import tkinter as tk

root = tk.Tk()
root.geometry('500x600')
root.title('password')
def check():
    if tkstr.get() == 'billychen0803':
        msgvar.set('驗證成功')
    else:
        msgvar.set('驗證失敗')
        
tkla = tk.Label(root, text = '輸入密碼')
tkla.pack()

tkstr = tk.StringVar()
entry = tk.Entry(root, width=15, textvariable=tkstr,show='*')
entry.pack()
        
btn = tk.Button(root, text='驗證', command=check)
btn.pack()

msgvar = tk.StringVar()
lb = tk.Label(root, textvariable= msgvar)
lb.pack()
root.mainloop()