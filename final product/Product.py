from tkinter import *
from pytube import YouTube
import urllib.request as url_req
import requests as req
from bs4 import BeautifulSoup as be
import webbrowser as webb
import json

root = Tk()
root.geometry('1300x800')
root.title('Personal Project')

def homepage():
    up_frame = Frame(root, bg='#2200AA', width=1300, height=300)
    up_frame.pack()
    down_frame = Frame(root, bg='#FFFFFF', width=1300, height=800-300)
    down_frame.pack()
    
    intro = Label(up_frame, text='''Introduction↓↓↓''', bg='#000080', fg='#FFFFFF', font=('Times New Roman', 20))
    intro.place(relx=0.3, rely=0.3,anchor='center')
    def open_url():
        webb.open('https://www.youtube.com/watch?v=6WM4FqrPf4A') #暫時
    intro_button = Button(up_frame, text='Click Me!!!', fg='Black', font=('Times New Roman',12), command=open_url)
    intro_button.place(relx=0.3, rely=0.6, anchor='center')
    
    source = Label(up_frame, text='Source Code↓↓↓', bg='#000080', fg='#FFFFFF', font=('Times New Roman', 20))
    source.place(relx=0.7, rely=0.3, anchor='center')
    def open_source():
        webb.open('https://github.com/tmwilliamlin168/CP-YouTube') #暫時
    source_button = Button(up_frame, text='Source Code', fg='Black', font=('Times New Roman',12), command=open_source)
    source_button.place(relx=0.7, rely=0.6,anchor='center')
    
    
    def yt_func():
        up_frame.destroy()
        down_frame.destroy()
        
        yt_frame = Frame(root, bg='#CC0000', width=1300, height=350)
        yt_frame.pack()
        
        lb1 = Label(yt_frame, text='Dowload Path:', bg='#CC0000', fg='#000000',font=('Times New Roman',22))
        lb1.place(relx=0.5,rely=0.15,anchor='center')
        
        lb2 = Label(yt_frame, text='URL:', bg='#CC0000', fg='#000000',font=('Times New Roman',22))
        lb2.place(relx=0.5,rely=0.5,anchor='center')
        
        yt_path = StringVar()
        yt_path.set('Default: Download')
        entry_path = Entry(yt_frame, textvariable=yt_path, width=50)
        entry_path.place(relx=0.5, rely=0.3, anchor='center')
        
        yt_url = StringVar()
        entry_url = Entry(yt_frame, textvariable=yt_url, width=50)
        entry_url.place(relx=0.5, rely=0.65,anchor='center')
        
        yt_frame2 = Frame(root, bg='#888888', width=1300, height=800-350)
        yt_frame2.pack()
        
        listbox = Listbox(yt_frame2, width=100, height=20)
        listbox.place(relx=0.5, rely=0.5, anchor='center')
        
        sbar = Scrollbar(yt_frame2)
        sbar.place(rely=0.5, relx=0.84, anchor='center', relheight=0.755)
        
        listbox.config(yscrollcommand = sbar.set)
        sbar.config(command = listbox.yview)
        
        def click_func():
            try:
                listbox.insert(END, 'downloading......')
                url = yt_url.get()
                yt = YouTube(url)
                title=yt.title
                path = yt_path.get()
                if path == 'Default: Download':
                    path = '/Users/billychen/Downloads/'
                yt.streams.get_highest_resolution().download(path)
                path = str(path)
                listbox.insert(END, f'{title}\n...Finish')
            except:
                listbox.insert(END,'Error!!!')
                
        btn = Button(yt_frame,text='Download', command = click_func, fg = 'Black', font=('Times New Roman',14))
        btn.place(relx=0.74,rely=0.65, anchor='center')
        
        def back():
            yt_frame.destroy()
            yt_frame2.destroy()
            homepage()
        
        mb_button = Button(yt_frame, text='Home',fg = 'Black', command=back)
        mb_button.place(relx=0.9, rely=0.1, anchor='center')
        
    def image_func():
        up_frame.destroy()
        down_frame.destroy()

        image_frame1 = Frame(root, bg='#DDDDDD', width=1300, height=100)
        image_frame1.pack()
        image_frame2 = Frame(root, bg='#DDDDDD', width=1300, height=800-100)
        image_frame2.pack()
        
        options = [
            'Download one image',
            'Download every image on the webpage'
        ]      
        clicked = StringVar()
        clicked.set(options[0])
        drop1 = OptionMenu(image_frame1, clicked,*options)
        drop1.place(relx=0.25, rely=0.5, anchor='center')
        
        def show():
            word = clicked.get()
            if word == 'Download one image':
                lb1 = Label(image_frame2, text='URL:', bg='#DDDDDD', fg='#000000',font=('Times New Roman',22))      
                lb1.place(relx=0.5, rely= 0.1,anchor='center') 
                        
                lb2 = Label(image_frame2, text='File Name:', bg='#DDDDDD', fg='#000000',font=('Times New Roman',22))      
                lb2.place(relx=0.5, rely= 0.2,anchor='center') 

                img_entry = StringVar()
                entry1 = Entry(image_frame2, textvariable=img_entry, width=50)
                entry1.place(relx=0.5, rely=0.15, anchor='center')
                        
                img_entry2 = StringVar()
                img_entry2.set('0000')
                entry2 = Entry(image_frame2, textvariable=img_entry2, width=50)
                entry2.place(relx=0.5, rely=0.25, anchor='center')
                        
                listbox = Listbox(image_frame2, width=100, height=20)
                listbox.place(relx=0.5, rely=0.65, anchor='center')
                        
                sbar = Scrollbar(image_frame2)
                sbar.place(rely=0.65, relx=0.84, anchor='center', relheight=0.485)
                        
                listbox.config(yscrollcommand = sbar.set)
                sbar.config(command = listbox.yview)
                        
                def download():
                    try:
                        listbox.insert(END,'Downloading')
                        url = img_entry.get()
                        file_name = img_entry2.get()
                        image_req = req.get(url).content
                        path = '/Users/billychen/Downloads/'
                        string = str(path)+str(file_name)+'.jpg'
                        with open(string,mode='wb') as file:
                            file.write(image_req)
                            listbox.insert(END,'...Finish')
                    except:
                        listbox.insert(END,'Error!!!')

                btn1 = Button(image_frame2, text='Download', command=download, fg = 'Black', font=('Times New Roman',14))
                btn1.place(relx=0.8, rely=0.25, anchor='center')
                
                def again():
                    lb1.destroy()
                    lb2.destroy()
                    entry1.destroy()
                    entry2.destroy()
                    listbox.destroy()
                    sbar.destroy()
                    btn1.destroy()
                
                btn2 = Button(image_frame2, text='Again', command=again, fg = 'Black', font=('Times New Roman',14))
                btn2.place(relx=0.9,rely=0.1,anchor='center')
                
            elif word == 'Download every image on the webpage':
                lb1 = Label(image_frame2, text='URL:', bg='#DDDDDD', fg='#000000',font=('Times New Roman',22))      
                lb1.place(relx=0.5, rely= 0.1,anchor='center') 
                        
                lb2 = Label(image_frame2, text='Numbers:', bg='#DDDDDD', fg='#000000',font=('Times New Roman',22))      
                lb2.place(relx=0.5, rely= 0.2,anchor='center') 

                img_entry = StringVar()
                entry1 = Entry(image_frame2, textvariable=img_entry, width=50)
                entry1.place(relx=0.5, rely=0.15, anchor='center')
                        
                img_entry2 = StringVar()
                img_entry2.set('Default: All')
                entry2 = Entry(image_frame2, textvariable=img_entry2, width=50)
                entry2.place(relx=0.5, rely=0.25, anchor='center')
                        
                listbox = Listbox(image_frame2, width=100, height=20)
                listbox.place(relx=0.5, rely=0.65, anchor='center')
                        
                sbar = Scrollbar(image_frame2)
                sbar.place(rely=0.65, relx=0.84, anchor='center', relheight=0.485)
                        
                listbox.config(yscrollcommand = sbar.set)
                sbar.config(command = listbox.yview)
                        
                def download():
                    try:
                        listbox.insert(END,'Downloading')
                        url = img_entry.get()
                        path = '/Users/billychen/Downloads/'
                        page = req.get(url)
                        souped = be(page.content, 'html.parser')
                        imags = souped.find_all('img')

                        arr = []
                        for i in range(len(imags)):
                            arr.append(i)
                            
                        download_numbers = img_entry2.get()
                        if str(download_numbers) == 'Default: All':
                            download_numbers = len(imags)
                        else:
                            download_numbers = int(download_numbers)

                        x=0
                        for img in imags:
                            if img.attrs.get('class') != None or img.attrs.get('alt') != None:
                                continue
                            imglink=img.attrs.get('src')
                            image = req.get(imglink).content
                            filename = '00'+str(arr[x])
                            with open(path+filename+'.png', 'wb') as file:
                                file.write(image)
                            x+=1
                            listbox.insert(END,filename+'png'+'...Finish')
                            if x == download_numbers:
                                break
                        listbox.insert(END,'...Finish')
                    except:
                        listbox.insert(END,'Error!!!')

                btn1 = Button(image_frame2, text='Download', command=download, fg = 'Black', font=('Times New Roman',14))
                btn1.place(relx=0.8, rely=0.25, anchor='center')
                
                def again():
                    lb1.destroy()
                    lb2.destroy()
                    entry1.destroy()
                    entry2.destroy()
                    listbox.destroy()
                    sbar.destroy()
                    btn1.destroy()
                
                btn2 = Button(image_frame2, text='Again', command=again, fg = 'Black', font=('Times New Roman',14))
                btn2.place(relx=0.9,rely=0.1,anchor='center')
        
        btn_confirm = Button(image_frame1, fg = 'Black', text='confirm', command=show)
        btn_confirm.place(relx=0.5, rely=0.5, anchor='center')
        
        def back():
            image_frame1.destroy()
            image_frame2.destroy()
            homepage()
        
        mb_button = Button(image_frame1, fg = 'Black',text='Home', command=back)
        mb_button.place(relx=0.75, rely=0.5, anchor='center')
        
    def amazon_func():
        up_frame.destroy()
        down_frame.destroy()
        
        amazon_frame1 = Frame(root, bg='#FFAA33', width=1300, height=200)
        amazon_frame1.pack()
        
        amazon_frame2 = Frame(root, bg="#FFFFFF", width=1300, height=800-200) 
        amazon_frame2.pack()       
        
        lb1 = Label(amazon_frame1, text='輸入搜尋關鍵字(用英文):', bg='#FFAA33', fg='#000000', font=('Times New Roman',22))
        lb1.place(relx=0.5, rely=0.2, anchor='center')
        
        entry_input = StringVar()
        entry_input.set('Search')
        entry1 = Entry(amazon_frame1, textvariable=entry_input, width=100)
        entry1.place(relx=0.45, rely=0.4, anchor='center')
        
        lb_product = Label(amazon_frame2, text='搜尋結果(含編號):', bg='#FFFFFF', fg='Black', font=('Times New Roman',22))
        lb_product.place(relx=0.25, rely=0.07, anchor='center')
        
        listbox1 = Listbox(amazon_frame2, width=60, height=30)
        listbox1.place(relx=0.25, rely=0.55, anchor='center')
        
        sbar1 = Scrollbar(amazon_frame2)
        sbar1.place(relx=0.452, rely=0.55, anchor='center', relheight=0.86)
        
        listbox1.config(yscrollcommand = sbar1.set)
        sbar1.config(command = listbox1.yview)
        
        lb_information = Label(amazon_frame2, text='產品資訊:', bg='#FFFFFF', fg='Black', font=('Times New Roman',22))
        lb_information.place(relx=0.75, rely=0.07, anchor='center')
        
        listbox2 = Listbox(amazon_frame2, width=60, height=30)
        listbox2.place(relx=0.75, rely=0.55, anchor='center')
        
        sbar2 = Scrollbar(amazon_frame2)
        sbar2.place(relx=0.952, rely=0.55, anchor='center', relheight=0.86)
        
        listbox2.config(yscrollcommand = sbar2.set)
        sbar2.config(command = listbox2.yview)
        
        lb_number = Label(amazon_frame1, text='選擇編號', bg='#FFAA33', fg='#000000', font=('Times New Roman',16))
        lb_number.place(relx=0.2, rely=0.6, anchor='center')
        
        arr_number = [x for x in range(1,21)]
        
        clicked_number = StringVar()
        clicked_number.set(arr_number[0])
        drop1 = OptionMenu(amazon_frame1, clicked_number, *arr_number)
        drop1.place(relx=0.2, rely=0.8, anchor='center')
        
        lb_specs = Label(amazon_frame1, text='要查看規格嗎', bg='#FFAA33', fg='#000000', font=('Times New Roman',16))
        lb_specs.place(relx=0.4, rely=0.6, anchor='center')
        
        arr_specs = [
            '是(Yes)',
            '否(No)'
        ]
        clicked_specs = StringVar()
        clicked_specs.set(arr_specs[1])
        drop2 = OptionMenu(amazon_frame1, clicked_specs, *arr_specs)
        drop2.place(relx=0.4, rely=0.8, anchor='center')
        
        lb_info = Label(amazon_frame1, text='要查看詳細資訊嗎', bg='#FFAA33', fg='#000000', font=('Times New Roman',16))
        lb_info.place(relx=0.6, rely=0.6, anchor='center')
        
        arr_info = [
            '是(Yes)',
            '否(No)'
        ]
        clicked_info = StringVar()
        clicked_info.set(arr_info[1])
        drop3 = OptionMenu(amazon_frame1, clicked_info, *arr_info)
        drop3.place(relx=0.6, rely=0.8,anchor='center')
        
        def confirm():
            try:
                text_input = str(entry_input.get()).strip()
                text = text_input.replace(' ', '+')
                URL = f'https://www.amazon.com/s?k={text}&dc&language=zh_TW&crid=2WOL9MPEXS5MO&sprefix={text}%2Caps%2C265&ref=a9_sc_1'
                
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

                page = req.get(URL, headers=headers)

                soup1 = be(page.content, "html.parser")
                soup2 = be(soup1.prettify(), "html.parser")
                
                titles = soup2.find_all('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
                
                global arr1
                arr1 = []
                
                x_number = 1
                for i in titles:
                    if x_number == 21:
                        break
                    
                    product_name = str(i.span.string)
                    product_url = 'https://www.amazon.com' + i['href']
                    
                    product_info = [str(x_number)+'-> ', product_name, product_url]
                    arr1.append(product_info)

                    x_number+=1
                    
                for i in arr1:
                    i[1] = i[1].replace('\n', " ").strip()
                
                
                for i in arr1:
                    x = str(i[0])+str(i[1])
                    listbox1.insert(END, x)
                    listbox1.insert(END, " ")
                    
            except:
                listbox1.insert(END, 'Error!!!')
        
        btn1 = Button(amazon_frame1, text='確認搜尋', command=confirm, fg = 'Black', font=('Times New Roman',16))
        btn1.place(relx=0.85, rely=0.4, anchor='center')
        
        def confirm_info():
            
            search_number = clicked_number.get()
            search_specs = clicked_specs.get()
            search_info = clicked_info.get()
            
            try:
                for i in arr1:
                    x = i[0]
                    if str(search_number) in x:
                        item_url = i[2]
                        
                        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
                        new_content = req.get(item_url, headers = headers)
        
                        new_page = be(new_content.content,'html.parser')
                        try:
                            price = new_page.find('td', class_='a-span12')
                            price = price.find('span', class_='a-offscreen')
                            item_price = '價格:'+str(price.string)
                            
                        except:
                            item_price = '沒貨'
                        
                        listbox2.insert(END, item_price)
                        listbox2.insert(END, " ")
                        
                        if search_specs == '是(Yes)':
                            arr_tree1 = []
                            arr_info = []
                            info = new_page.find('table', class_='a-normal a-spacing-micro')
                            tree = info.find_all('tr')

                            for i in tree:
                                td_tree = i.find_all('td')
                                arr_tree1.append([])
                                length = len(arr_tree1)-1
                                for i in td_tree:
                                    x = str(i.span.string)
                                    arr_tree1[length].append(x)
                            
                            for i in arr_tree1:
                                x = str(i[0])
                                y = str(i[1])
                                xy = x+": "+y
                                arr_info.append(xy)
                        
                            for i in arr_info:
                                listbox2.insert(END, i)
                            listbox2.insert(END, " ")
                            
                        else:
                            pass
                        
                        if search_info == '是(Yes)':
                            arr_tree1 = []
            
                            info = '關於此商品:'
                            arr_tree1.append(info)
                            
                            more_info = new_page.find('ul', class_='a-unordered-list a-vertical a-spacing-mini')
                            span = more_info.find_all('span', class_='a-list-item')
                            for i in span:
                                x = str(i.string)
                                if x == 'None':
                                    continue
                                x = '->'+x
                                arr_tree1.append(x)
                            
                            for i in arr_tree1:
                                listbox2.insert(END, i)
                            listbox2.insert(END, " ")
                        else:
                            pass
                        
                    else:
                        continue
                    
                    break 
                
            except:
                listbox2.insert(END, 'Error!!!')
        
        btn_info = Button(amazon_frame1, text='確認', fg='#000000', command=confirm_info)
        btn_info.place(relx=0.8,rely=0.8,anchor='center')
        
        def back():
            amazon_frame1.destroy()
            amazon_frame2.destroy()
            homepage()
        
        btn_home = Button(amazon_frame1, text='Home', fg='Black', command=back)
        btn_home.place(relx=0.85, rely=0.2, anchor='center')
        
    def covid_func():
        up_frame.destroy()
        down_frame.destroy()
        
        covid_frame1 = Frame(root, bg='#BBFF66', width=1300, height=300)
        covid_frame1.pack()
        
        covid_frame2 = Frame(root, bg='#FFFFFF', width=1300, height=800-300)
        covid_frame2.pack()
        
        lb1 = Label(covid_frame1, text='查看全球確診數量', bg='#BBFF66', fg='Black', font=('Times New Roman',22))
        lb1.place(relx=0.45, rely=0.25, anchor='center')
        
        lb2 = Label(covid_frame1, text='搜尋國家(英文全名):', bg='#BBFF66', fg='Black', font=('Times New Roman',22))
        lb2.place(relx=0.5, rely=0.45,anchor='center')
        
        entry1_input = StringVar()
        entry1_input.set('taiwan')
        entry1 = Entry(covid_frame1, textvariable=entry1_input, width=85)
        entry1.place(relx=0.5, rely=0.65, anchor='center')
        
        listbox1 = Listbox(covid_frame2, width=120, height=24)
        listbox1.place(relx=0.5, rely=0.5,anchor='center')
        
        sbar1 = Scrollbar(covid_frame2)
        sbar1.place(relx=0.91, rely=0.5, relheight=0.82, anchor='center')
        
        listbox1.config(yscrollcommand = sbar1.set)
        sbar1.config(command = listbox1.yview)
        
        def confirm():
            try:
                url = "https://www.worldometers.info/coronavirus/"
                
                text = req.get(url).text

                html = be(text, 'lxml')
                
                case_death_recover = html.find_all("div", id='maincounter-wrap')
                numbers_cdr = html.find_all('div', class_='maincounter-number')
                arr_cdr = []

                arr = []
                arr2 = []

                for i in case_death_recover:
                    x = str(i.h1.string)
                    arr.append(x)

                for i in numbers_cdr:
                    x = str(i.span.string)
                    arr2.append(x)

                for i in range(len(arr2)):
                    x = arr[i]
                    y = arr2[i]
                    z = x+" "+y
                    arr_cdr.append(z)

                for i in arr_cdr:
                    listbox1.insert(END, i)
                
                listbox1.insert(END, " ")
            except:
                listbox1.insert(END, 'Error!!!')
            
        
        btn1 = Button(covid_frame1, text='確認', command=confirm, fg='Black', font=('Times New Roman',16))
        btn1.place(relx=0.65, rely=0.25,anchor='center')
        
        def confirm_search():
            text_input = str(entry1_input.get()).strip().lower()

            try:
                url = "https://www.worldometers.info/coronavirus/"

                text = req.get(url).text
                html = be(text, 'lxml')
                
                content = html.find('tbody')
                tr = content.find_all('tr')

                datas = []
                type = [
                    'country: ',
                    'Total Cases: ',
                    'New Cases: ',
                    'Total Deaths: ',
                    'New Deaths: ',
                    'Total Recovered: ',
                    'New recovered: ',
                    'Active Cases: ',
                    'Serious Critical: '
                ]

                for i in tr:
                    datas_1 = []
                    a = i.find('a')
                    if a ==None:
                        continue
                    arr_data = []

                    c = str(a.string)

                    
                    arr_data.append(c)
                    
                    td = i.find_all('td')
                    for o in range(2,10):
                        numbers = str(td[o].string)
                        if numbers == 'None':
                            numbers = '0'
                        arr_data.append(numbers)
                    
                    for g in range(9):
                        x = type[g]
                        y = arr_data[g]
                        xy = x+y
                        if xy == 'Total Deaths:  ':
                            xy = 'Total Deaths: 0'
                        datas_1.append(xy)
                    datas.append(datas_1)
                
                for i in datas:
                    x = str(i[0]).lower()
                    if text_input in x:
                        for u in i:
                            listbox1.insert(END, str(u))
                    else:
                        continue
                
                listbox1.insert(END," ")                    
                
            except:
                listbox1.insert(END,'Error!!!')
        
        btn2 = Button(covid_frame1, text='確認搜尋', command=confirm_search, fg='Black', font=('Times New Roman',16))
        btn2.place(relx=0.88, rely=0.65,anchor='center')
        
        def back():
            covid_frame1.destroy()
            covid_frame2.destroy()
            homepage()
        
        btn_home = Button(covid_frame1, text='Home', fg='Black', command=back)
        btn_home.place(relx=0.85, rely=0.25, anchor='center')
    
    def pchome_func():
        up_frame.destroy()
        down_frame.destroy()
        
        pchome_frame1 = Frame(root, bg='#CC0000', width=1300, height=300)
        pchome_frame1.pack()
        
        pchome_frame2 = Frame(root, bg='#00BBFF', width=1300, height=800-300)
        pchome_frame2.pack()
        
        lb1 = Label(pchome_frame1, text='請輸入關鍵字(英文):', bg='#CC0000', fg='Black', font=('Times New Roman',22))
        lb1.place(relx=0.5, rely=0.25,anchor='center')
        
        entry_input = StringVar()
        entry_input.set('搜尋')
        entry1 = Entry(pchome_frame1, textvariable=entry_input, width=85)
        entry1.place(relx=0.5, rely=0.5, anchor='center')
        
        lb_number = Label(pchome_frame1, text='選擇產品編號:', bg='#CC0000', fg='Black', font=('Times New Roman',22))
        lb_number.place(relx=0.3, rely=0.8, anchor='center')
        
        pchome_numbers = [x for x in range(1,20)]
        clicked_number = StringVar()
        clicked_number.set(pchome_numbers[0])
        drop1 = OptionMenu(pchome_frame1, clicked_number, *pchome_numbers)
        drop1.place(relx=0.4, rely=0.8, anchor='center')
        
        lb_confirm = Label(pchome_frame1, text='確認查看詳細資訊:', bg='#CC0000', fg='Black', font=('Times New Roman',22))
        lb_confirm.place(relx=0.7, rely=0.8, anchor='center')
        
        lb_product = Label(pchome_frame2, text='搜尋結果(編號和價格):', bg='#00BBFF', fg='Black', font=('Times New Roman',22))
        lb_product.place(relx=0.25, rely=0.06, anchor='center')
        
        listbox1 = Listbox(pchome_frame2, width=60, height=25)
        listbox1.place(relx=0.25, rely=0.55, anchor='center')
        
        sbar1 = Scrollbar(pchome_frame2)
        sbar1.place(relx=0.452, rely=0.55, anchor='center', relheight=0.85)
        
        listbox1.config(yscrollcommand = sbar1.set)
        sbar1.config(command = listbox1.yview)
        
        lb_info = Label(pchome_frame2, text='詳細資訊:', bg='#00BBFF', fg='Black', font=('Times New Roman',22))
        lb_info.place(relx=0.75, rely=0.06, anchor='center')
        
        listbox2 = Listbox(pchome_frame2, width=70, height=25)
        listbox2.place(relx=0.73, rely=0.55, anchor='center')
        
        sbar2 = Scrollbar(pchome_frame2)
        sbar2.place(relx=0.97, rely=0.55, anchor='center', relheight=0.85)
        
        listbox2.config(yscrollcommand = sbar2.set)
        sbar2.config(command = listbox2.yview)
        
        def confirm():
            try:
                search_input = str(entry_input.get())
                search = search_input.strip()
                search = search.replace(' ', '%20')
                url = f'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={search}&page=1&sort=sale/dc'
                
                root = url_req.Request(url, headers = {
                    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
                })

                with url_req.urlopen(root) as re:
                    data = re.read().decode('utf-8')
                
                data = json.loads(data)
                
                global arr_pchome_info
                arr_pchome_info = []
                
                product = data['prods']
                for i in range(1,20):
                    p1 = product[i]
                    product_name = p1['name']
                    product_price = p1['originPrice']
                    product_info = p1['describe']
                    i = str(i)+'-> '
                    x = [i, product_name, product_price, product_info]
                    arr_pchome_info.append(x)
                
                for i in arr_pchome_info:
                    insert_string = str(i[0]) + str(i[1])
                    listbox1.insert(END, insert_string)
                    
                    insert_price = '價格:'+str(i[2])
                    listbox1.insert(END, insert_price)
                    
                    listbox1.insert(END, " ")
                    
            except:
                listbox1.insert(END, 'Error!!!')
                
        btn1 = Button(pchome_frame1, text='確認', command=confirm, fg='black')
        btn1.place(relx=0.85, rely=0.5, anchor='center')
        
        def confirm_search():
            try:
                selected_number = str(clicked_number.get()).strip()
                for i in arr_pchome_info:
                    number = str(i[0])
                    if selected_number in number:
                        product_info = str(i[3])
                        new_info = product_info.replace('\r'," ").split('\n')
                        for i in new_info:
                            if '•' in str(i):
                                new_product_info = str(i).split('•')
                                for i in new_product_info:
                                    listbox2.insert(END, i)
                                    
                            elif "■" in str(i):
                                new_product_info = str(i).split('■')
                                for i in new_product_info:
                                    listbox2.insert(END, i)
                                    
                            elif "●" in str(i):
                                new_product_info = str(i).split('●')
                                for i in new_product_info:
                                    listbox2.insert(END, i)
                            else:
                                listbox2.insert(END, i)
                        
                        listbox2.insert(END, " ")
                        break
                        
            except:
                listbox2.insert(END, "Error!!!")
        
        btn2 = Button(pchome_frame1, text='確認', command=confirm_search, fg='Black')
        btn2.place(relx=0.84, rely=0.8, anchor='center')
        
        def back():
            pchome_frame1.destroy()
            pchome_frame2.destroy()
            homepage()
        
        btn_home = Button(pchome_frame1, text='Home', fg='Black', command=back)
        btn_home.place(relx=0.85, rely=0.25, anchor='center')
        
    button_yt = Button(down_frame, text='Youtube Download',fg='Black', font=('Times New Roman',12), command=yt_func)
    button_amazon = Button(down_frame, text='Amazon',fg='Black', font=('Times New Roman',12),command=amazon_func)
    button_pchome = Button(down_frame, text='PChome', fg='Black', font=('Times New Roman',12),command=pchome_func)
    button_image = Button(down_frame, text='Image Download', fg='Black', font=('Times New Roman',12),command=image_func)
    button_covid = Button(down_frame, text='COVID cases', fg='Black', font=('Times New Roman',12),command=covid_func)
    
    button_pchome.place(relx = 0.25, rely = 0.3, anchor='center')
    button_amazon.place(relx = 0.5, rely = 0.3, anchor='center')
    button_covid.place(relx = 0.75, rely = 0.3, anchor='center') 
    button_yt.place(relx = 0.25, rely = 0.6, anchor='center')
    button_image.place(relx = 0.5, rely = 0.6, anchor='center')

    
homepage()

root.mainloop()