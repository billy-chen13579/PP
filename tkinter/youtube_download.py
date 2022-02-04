import tkinter as tk
from pytube import YouTube

def click_func():
    listbox.insert(tk.END, f'..下載中')
    try:
        url = yt_url.get()
        yt = YouTube(url)
        title=yt.title
        path = yt_path.get()
        if path == '預設路徑:下載':
            path = '/Users/billychen/Downloads'
        yt.streams.get_highest_resolution().download(path)
        listbox.insert(tk.END, f'{title}\n...下載完成')
    except:
        listbox.insert(tk.END,'發生錯誤')
        
#主視窗
#更多資訊 https://docs.python.org/3/library/tkinter.html
root = tk.Tk()
root.geometry('700x600')
root.title('Youtube下載器')

#Frame 架構 
#顏色參考 https://www.toodoo.com/db/color.html
fm = tk.Frame(root, bg = '#A52A2A', width=700, height=300)
fm.pack()

#label 字樣

lb2 = tk.Label(fm, text='請輸入Youtube影片網址:',bg='#A52A2A',fg='#FFFFFF', font=('細明體',16))
lb2.place(rely=0.55,relx=0.5,anchor='center')

lb = tk.Label(fm,text='請輸入下載路徑:',bg='#A52A2A',fg='#FFFFFF', font=('細明體',16))
lb.place(rely=0.25,relx=0.5,anchor='center')

#Entry 輸入

yt_path = tk.StringVar()
yt_path.set('預設路徑:下載')
entry_path = tk.Entry(fm, textvariable=yt_path, width=40)
entry_path.place(rely=0.3,relx=0.5,anchor='center')

yt_url = tk.StringVar()
entry = tk.Entry(fm,textvariable=yt_url, width=40)
entry.place(rely=0.7,relx=0.5,anchor='center')



#Frame 下載區
dload = tk.Frame(root, width=700, height=600-300)
dload.pack()

lb2 = tk.Label(dload, text='下載狀態',fg = 'Black', font=('細明體',12))
lb.place(rely=0.1, relx=0.5, anchor='center')

listbox = tk.Listbox(dload, width=65, height = 15)
listbox.place(rely=0.5, relx=0.5,anchor='center')

sbar = tk.Scrollbar(dload)
sbar.place(rely=0.5,relx=0.91, anchor='center', relheight=0.85)

listbox.config(yscrollcommand = sbar.set)
sbar.config(command = listbox.yview)

#Button
btn = tk.Button(fm,text='下載影片', command = click_func, fg = 'Black', font=('細明體',12))
btn.place(rely=0.7, relx=0.85, anchor='center')


#啟動主視窗
root.mainloop()

