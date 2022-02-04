import requests as req

url = 'https://kueishan.managebac.com/attachments/BAh7CEkiCGdpZAY6BkVUSSIvZ2lkOi8vbWFuYWdlYmFjL0Fzc2V0LzEwMjQ4Njk0Nj9leHBpcmVzX2luBjsAVEkiDHB1cnBvc2UGOwBUSSIMZGVmYXVsdAY7AFRJIg9leHBpcmVzX2F0BjsAVDA=--9a6c506856236d157cc63c787f21d59ff7159549'

r= req.get(url).content

path = '/Users/billychen/Downloads/'

with open('1234.pdf', mode='wb') as file:
    file.write(r)