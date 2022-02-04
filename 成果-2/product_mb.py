import urllib.request as req
from bs4 import BeautifulSoup as be

#homepage
url = 'https://kueishan.managebac.com/student'

root = req.Request(url, headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'cookie':'__utma=58354037.2093169445.1641642234.1641642234.1641642234.1; __utmc=58354037; __utmz=58354037.1641642234.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); user_id=12675811; user=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ik1USTJOelU0TVRFPSIsImV4cCI6bnVsbCwicHVyIjoiY29va2llLnVzZXIifX0%3D--0273dcd3dbf380c6afb50a343946e045ff4076d1; _managebac_session=INju5fWWoRVcCagmRFRBlAOMpT13NYDKZGDm%2BKPbHLTvucWhVh7unfybv05SytP%2FvHEVARTmMKRCg5PCq5Ot5oN%2Fd9YNr3MRJLmf%2BCu2Siu7ZjNZ8EjiwzoTNrfcN6fJTTOFcGQWxTUytwiA1%2FYduHsX2bXXUswn0LE1IN2T5jfSa8wAUwsIIXH8Xtg0XvcUuzSSWcLFrW%2FS1bsutKAuE9KWsX54UWbfk9c0iPkGmXPW1OJL%2BHn6KYL7J1n0AphS%2Bv4deiAOYId3OZ3reTQirPtT99KlK3NRX2nN0roMgsanHI30bjGagfSusBI9lJkVVMTaMYCAAKiT7cgfVKKwds%2BHgSGMAZPFBNqZ79pPVW6M92r%2B9JIQEk3AVBZ%2BC5Do%2FFp6iqI4w1crf8yddweC8bYpbrQ9kapkQIasjQkP78gvfWkh2xpKdGXd6u0rsJkxyZwEbazy5LoNRmDHgYvAKIimnZyg9rCqlo8nb%2B0JrNhzkfXiLOyRFAn5mMrVXWIkeDYhTOs6%2FE%2BNhoRaTWp%2BYZCsIvguC2xfJ6z1ydgKppv7r7ZBNVIRgcCEnIxrVQ2LNgIscmq2lI4SxyFlh20OyZ%2FCQLTL3SdFX3T41vAEwPzFyKCiIhhrGuo9bQ3%2Fnf9rE8oJaDQCT9E%3D--1hiDtMM5VCuyM%2BaL--pSr0yeexKNNzy8WGnv2rww%3D%3D'
})

with req.urlopen(root) as re:
    data = re.read().decode('utf-8')


content = be(data,'html.parser')
tasks_calendar = content.find_all('div', class_='table-responsive')

arr_task=[]
arr_number=[]
arr_enumerate=[]

for i in tasks_calendar:
    tasks = i.find_all('a')
    for o in tasks:
        if 'span' in str(o.parent):
            arr_task.append(o.string)
for i in range(len(arr_task)):
    x=i+1
    tuple = str(x)+' : '+str(arr_task[i])
    arr_enumerate.append(tuple)
for i in arr_enumerate:
    print(i)

number = int(input('要查看哪一個(輸入數字):'))

task_chosen = arr_task[number-1]
more = task_chosen.parent
new_url = 'https://kueishan.managebac.com/' + more['href']

#page_task
root2 = req.Request(new_url, headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'cookie':'__utma=58354037.2093169445.1641642234.1641642234.1641642234.1; __utmc=58354037; __utmz=58354037.1641642234.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); user_id=12675811; user=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ik1USTJOelU0TVRFPSIsImV4cCI6bnVsbCwicHVyIjoiY29va2llLnVzZXIifX0%3D--0273dcd3dbf380c6afb50a343946e045ff4076d1; _managebac_session=INju5fWWoRVcCagmRFRBlAOMpT13NYDKZGDm%2BKPbHLTvucWhVh7unfybv05SytP%2FvHEVARTmMKRCg5PCq5Ot5oN%2Fd9YNr3MRJLmf%2BCu2Siu7ZjNZ8EjiwzoTNrfcN6fJTTOFcGQWxTUytwiA1%2FYduHsX2bXXUswn0LE1IN2T5jfSa8wAUwsIIXH8Xtg0XvcUuzSSWcLFrW%2FS1bsutKAuE9KWsX54UWbfk9c0iPkGmXPW1OJL%2BHn6KYL7J1n0AphS%2Bv4deiAOYId3OZ3reTQirPtT99KlK3NRX2nN0roMgsanHI30bjGagfSusBI9lJkVVMTaMYCAAKiT7cgfVKKwds%2BHgSGMAZPFBNqZ79pPVW6M92r%2B9JIQEk3AVBZ%2BC5Do%2FFp6iqI4w1crf8yddweC8bYpbrQ9kapkQIasjQkP78gvfWkh2xpKdGXd6u0rsJkxyZwEbazy5LoNRmDHgYvAKIimnZyg9rCqlo8nb%2B0JrNhzkfXiLOyRFAn5mMrVXWIkeDYhTOs6%2FE%2BNhoRaTWp%2BYZCsIvguC2xfJ6z1ydgKppv7r7ZBNVIRgcCEnIxrVQ2LNgIscmq2lI4SxyFlh20OyZ%2FCQLTL3SdFX3T41vAEwPzFyKCiIhhrGuo9bQ3%2Fnf9rE8oJaDQCT9E%3D--1hiDtMM5VCuyM%2BaL--pSr0yeexKNNzy8WGnv2rww%3D%3D'
})

with req.urlopen(root2) as re:
    data2 = re.read().decode('utf-8')

arr_task2 = []

content_2 = be(data2, 'html.parser')
task_2 = content_2.find_all('h4', class_='title')
for i in task_2:
    x = 'Task Title : '+str(i.string)
    x = x.replace('\n','')
    arr_task2.append(x)

task_basic_info= content_2.find_all('div', class_='label')

x = 'Information : '
for i in range(len(task_basic_info)):
    y = i
y-=1
z = 0   

for i in task_basic_info:
    z+=1
    if z<y:
        x+= str(i.string)+', '
    else:
        x+=str(i.string)
x = x.replace('\n','')
x = x.replace('NoneCurrent Unit','')
arr_task2.append(x)


for i in arr_task2:
    print(i)
