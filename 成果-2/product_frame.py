import tkinter as tk
from pytube import YouTube

root = tk.Tk()
root.geometry('1000x600')
root.title('爬蟲軟體')

#page 1
def tab1():
    
    fm1_tab1 = tk.Frame(root, bg='#000080', width=1000, height=200)
    fm1_tab1.pack()
    
    intro = tk.Label(fm1_tab1, text= "This is a web scraping aoftware that can help you extract data from the internet and automate computers.\n The link shows how to use this software. \n https://www.youtube.com/watch?v=VEQ4UBfLbdc", bg='#000080', fg='#FFFFFF', font=('Times New Roman', 20))
    intro.place(relx=0.5, rely=0.5,anchor='center')
    
    fm2_tab1 = tk.Frame(root, bg='#FFFFFF', width=1000, height=600-200)
    fm2_tab1.pack()
    
    def mb_func():
        fm1_tab1.destroy()
        fm2_tab1.destroy()
        
        fm1_tab2 = tk.Frame(root,bg='#FFFFFF', width=1000, height=200)
        fm1_tab2.pack()
        mb_label = tk.Label(fm1_tab2, text = 'this is for managebac')
        mb_label.pack()
        
        def back():
            fm1_tab2.destroy()
            tab1()
        
        mb_button = tk.Button(fm1_tab2, text='home', command=back)
        mb_button.pack()
    
    def amazon_func():
        fm1_tab1.destroy() 
        fm2_tab1.destroy()
        
        fm1_tab2 = tk.Frame(root,bg='#FFFFFF', width=1000, height=200)
        fm1_tab2.pack()
        amazon_label = tk.Label(fm1_tab2, text = 'this is for amazon')   
        amazon_label.pack()
        
        def back():
            fm1_tab2.destroy()
            tab1()
        
        amazon_button = tk.Button(fm1_tab2, text='home', command=back)
        amazon_button.pack()
        
    def pchome_func():
        fm1_tab1.destroy()
        fm2_tab1.destroy()
        
        fm1_tab2 = tk.Frame(root,bg='#FFFFFF', width=1000, height=200)
        fm1_tab2.pack()
        pchome_label = tk.Label(fm1_tab2, text = 'this is for pchome')   
        pchome_label.pack()    
        
        def back():
            fm1_tab2.destroy()
            tab1()
        
        pchome_button = tk.Button(fm1_tab2, text='home', command=back)
        pchome_button.pack()
        
    def image_func():
        fm1_tab1.destroy()
        fm2_tab1.destroy()
        
        fm1_tab2 = tk.Frame(root,bg='#FFFFFF', width=1000, height=200)
        fm1_tab2.pack()
        image_label = tk.Label(fm1_tab2, text = 'this is for image')   
        image_label.pack()
        
        def back():
            fm1_tab2.destroy()
            tab1()
        
        image_button = tk.Button(fm1_tab2, text='home', command=back)
        image_button.pack()
        
    def others_func():
        fm1_tab1.destroy()
        fm2_tab1.destroy()
        
        fm1_tab2 = tk.Frame(root,bg='#FFFFFF', width=1000, height=200)
        fm1_tab2.pack()
        others_label = tk.Label(fm1_tab2, text = 'this is for others')   
        others_label.pack()
        
        def back():
            fm1_tab2.destroy()
            tab1()
        
        others_button = tk.Button(fm1_tab2, text='home', command=back)
        others_button.pack()
        
    def yt_func():
        fm1_tab1.destroy()
        fm2_tab1.destroy()
        
        fm1_tab2 = tk.Frame(root,bg='#FFFFFF', width=1000, height=600)
        fm1_tab2.pack()
        
        fm = tk.Frame(fm1_tab2, bg = '#A52A2A', width=1000, height=300)
        fm.pack()
        
        lb2 = tk.Label(fm, text='請輸入Youtube影片網址:',bg='#A52A2A',fg='#FFFFFF', font=('細明體',16))
        lb2.place(rely=0.55,relx=0.5,anchor='center')

        lb = tk.Label(fm,text='請輸入下載路徑:',bg='#A52A2A',fg='#FFFFFF', font=('細明體',16))
        lb.place(rely=0.25,relx=0.5,anchor='center')
        
        yt_path = tk.StringVar()
        yt_path.set('預設路徑:下載')
        entry_path = tk.Entry(fm, textvariable=yt_path, width=40)
        entry_path.place(rely=0.3,relx=0.5,anchor='center')

        yt_url = tk.StringVar()
        entry = tk.Entry(fm,textvariable=yt_url, width=40)
        entry.place(rely=0.7,relx=0.5,anchor='center')
        
        dload = tk.Frame(fm1_tab2, width=700, height=600-300)
        dload.pack()

        lb2 = tk.Label(dload, text='下載狀態',fg = 'Black', font=('細明體',12))
        lb.place(rely=0.1, relx=0.5, anchor='center')

        listbox = tk.Listbox(dload, width=65, height = 15)
        listbox.place(rely=0.5, relx=0.5,anchor='center')

        sbar = tk.Scrollbar(dload)
        sbar.place(rely=0.5,relx=0.91, anchor='center', relheight=0.85)

        listbox.config(yscrollcommand = sbar.set)
        sbar.config(command = listbox.yview)
        
        def click_func():
            try:
                listbox.insert(tk.END, '下載中')
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
                
        btn = tk.Button(fm,text='下載影片', command = click_func, fg = 'Black', font=('細明體',12))
        btn.place(rely=0.7, relx=0.85, anchor='center')
        
        def back():
            fm1_tab2.destroy()
            tab1()
        
        mb_button = tk.Button(fm, text='home', command=back)
        mb_button.place(relx=0.5, rely=0.9, anchor='center')
    
    
    button_yt = tk.Button(fm2_tab1, text='Youtube Download',fg='Black', font=('Times New Roman',12), command=yt_func)
    button_mb = tk.Button(fm2_tab1, text='Managebac',fg='Black', font=('Times New Roman',12),command=mb_func)
    button_amazon = tk.Button(fm2_tab1, text='Amazon',fg='Black', font=('Times New Roman',12),command=amazon_func)
    button_pchome = tk.Button(fm2_tab1, text='Pchome', fg='Black', font=('Times New Roman',12),command=pchome_func)
    button_image = tk.Button(fm2_tab1, text='Image Download', fg='Black', font=('Times New Roman',12),command=image_func)
    button_others = tk.Button(fm2_tab1, text='Others', fg='Black', font=('Times New Roman',12),command=others_func)
    
    button_yt.place(relx = 0.25, rely = 0.3, anchor='center')
    button_mb.place(relx = 0.5, rely = 0.3, anchor='center')
    button_amazon.place(relx = 0.75, rely = 0.3, anchor='center')
    button_pchome.place(relx = 0.25, rely = 0.6, anchor='center')
    button_image.place(relx = 0.5, rely = 0.6, anchor='center')
    button_others.place(relx = 0.75, rely = 0.6, anchor='center')
    
tab1()

root.mainloop()