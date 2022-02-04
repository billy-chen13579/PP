import urllib.request as req
from bs4 import BeautifulSoup as be
find_text = input('你想要找尋的商品(小寫要空格):')

url = 'https://www.amazon.com/s?k=gpu&ref=nb_sb_noss_2'
request = req.Request(url, headers={
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
    "cookie": '''ession-id=139-5611736-6545643; i18n-prefs=USD; lc-main=zh_TW; sp-cdn="L5Z9:TW"; ubid-main=132-8110898-6515554; session-id-time=2082787201l; session-token=kFBx118zpbq2cvyC9sz9XjUjmB7BNqCIh0O5O1IzRPIZzRkhTQLKf+CjS+Jij9dXqQhUJltJIPDQBsArSqaYfDY9iREhl6BT3snKynbon0kHfETtVZpi+ORgE3j7ywNeMOzMo6cMptoqKIh/IrmjRuvSi62IHspShqI1gmS3WavLUzeNvHxm4ttbKkipkoGN; skin=noskin; csm-hit=adb:adblk_no&t:1639206563159&tb:29Z3T61H1KT68R9JD0Y5+s-7VS6QHMAP6QMG3W1FJ9D|1639206563159'''
})

with req.urlopen(request) as res:
    data = res.read().decode('utf-8')

page_number = be(data, 'html.parser')
total_pages = page_number.find_all('li', class_ = 'a-disabled')
for i in total_pages:
    x = i.string


def scrap_name(url):
    request = req.Request(url, headers={
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
        "cookie": '''ession-id=139-5611736-6545643; i18n-prefs=USD; lc-main=zh_TW; sp-cdn="L5Z9:TW"; ubid-main=132-8110898-6515554; session-id-time=2082787201l; session-token=kFBx118zpbq2cvyC9sz9XjUjmB7BNqCIh0O5O1IzRPIZzRkhTQLKf+CjS+Jij9dXqQhUJltJIPDQBsArSqaYfDY9iREhl6BT3snKynbon0kHfETtVZpi+ORgE3j7ywNeMOzMo6cMptoqKIh/IrmjRuvSi62IHspShqI1gmS3WavLUzeNvHxm4ttbKkipkoGN; skin=noskin; csm-hit=adb:adblk_no&t:1639206563159&tb:29Z3T61H1KT68R9JD0Y5+s-7VS6QHMAP6QMG3W1FJ9D|1639206563159'''
    })

    with req.urlopen(request) as res:
        data = res.read().decode('utf-8')
    
    html = be(data, 'html.parser')
    
    contents = html.find_all('a', class_="a-link-normal a-text-normal")

    for content in contents:
        x = str(content.span.string).lower()
        if find_text in x:
            link = 'https://www.amazon.com' + content['href']
            print(x, '\n')
            print(link, '\n')
            request = req.Request(link, headers = {
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
                "cookie": '''session-id=139-5611736-6545643; i18n-prefs=USD; lc-main=zh_TW; sp-cdn="L5Z9:TW"; ubid-main=132-8110898-6515554; session-id-time=2082787201l; skin=noskin; session-token=Zl6lDSm3TLKrlB3Q+hhvNJOdVdZzaP9uHmZSCx9AywFi8cYbJd/pbWs7TAkf33zFK4V3aLyP7LyBSv25lq6BsxXsIYR5VcRhXTylv8M76KIiZhO4s+BDN1llgjqrVHiW9MkvWF32rNvY2RMsoVsWvTaPYmZVMT7YFN5NvHzQp7R4eqqUg6i8MJwxkqehvdi0; csm-hit=adb:adblk_no&t:1639208505265&tb:JD966N769SBCMJ16GX8S+s-JD966N769SBCMJ16GX8S|1639208505265'''
            })
            with req.urlopen(request) as res:
                data = res.read().decode('utf-8')
            arr = []
            con2 = be(data, 'html.parser')
            contents_2 = con2.find_all('th', class_="comparison_attribute_name_column comparison_table_first_col")
            for i in contents_2:
                i = i.span.string
                arr.append(i)
            contents = con2.find_all('th', class_="a-span3 comparison_attribute_name_column comparison_table_first_col")
            for i in contents:
                i = i.span.string
                arr.append(i)            
            data_gpu = con2.find_all('td', class_= "comparison_baseitem_column")
            arr1 = []
            for i in data_gpu:
                try:
                    x = i.span.string
                    if x != None:
                        z = i.span.string
                        arr1.append(z)
                    else:
                        if i.find_all('span', class_= "a-icon-alt") != []:
                            rating = i.find_all('span', class_= "a-icon-alt")
                            for o in rating:
                                z = o.string
                                arr1.append(z)
                        else: 
                            z = i.a.string
                            f = 'https://www.amazon.com/'+i.a['href']
                            tuple = (z, f)
                            arr1.append(tuple)
                except:
                    continue
            for i,o in zip(arr, arr1):
                print(i, '--->', o)
            return 'break'
    
    new_url = html.find_all('li', class_="a-last")
    for i in new_url:
        href_url = i.a['href']
        return 'https://www.amazon.com/' + href_url

count = 0
page_url = 'https://www.amazon.com/s?k=gpu&ref=nb_sb_noss_2'
scrap_name(page_url)
while count < x-1:
    page_url = scrap_name(page_url)
    if page_url == 'break':
        break
    print(page_url)
    count += 1
