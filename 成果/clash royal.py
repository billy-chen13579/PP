import urllib.request as req
url="https://statsroyale.com/top/players"
root=req.Request(url, headers={
    "cookie":"_ga=GA1.2.720921289.1632444394; _pubcid=91257460-87bc-42bb-9226-69df354cec8b; _ym_uid=1632444395134373461; _ym_d=1632444395; GUIDE_PROMO_SHOWED=1; cto_bidid=uqQN0F9OcDRhS2ZnNTB6cEN2clUyWTJlWmdCT1hiNFVPUXlPZ241RGNzOHE4bEIySyUyRlBUTGNsdjVITDR4d2xrTHdpMSUyQlJJeE9ESHdKUSUyRnJxVlQ5NUZGd1NpRGQ3UGE0eXAxMmp2RGVJJTJGZFJGaGpQRVRyNVBvcVklMkYlMkJvWiUyQkpYdDhFd0QlMkJTZ1JIVlFiJTJCSzB4aVZRUXFWVFE1cHclM0QlM0Q; cto_bundle=9iUgjF9ub2diYVhhalFhWiUyQkdFbExHZVpMenZvSkV0OUFxJTJCVXN6UzNFb083QkNOOGNQS3dyMzMlMkJWWWRxcWlLU1ExQ0RtNEswUW1hTm1rUnM5cXhCMHB3QzhQZ1VRVzhaMjloJTJGWkRaNUh6SzdsaHdiNUxmJTJCWmxCY1ZSa1VPWmJ3M3k4Tnc1SFlIZ1BMZE42SkJxJTJGczNNY0MyYWdQMzltVzFxcUxUSVZXaTZLZzBqRFBNUGIwZk0lMkYzbEZ5cmIlMkY0SmFnTCUyQkxRTkdLaWhsZ1BPOUc1UTF6QzE4NmxBJTNEJTNE; _gid=GA1.2.1107017136.1637742066; _ym_isad=1; XSRF-TOKEN=eyJpdiI6IldSXC9VUm5NVHMyWEhqZ0VrQUFmSGNnPT0iLCJ2YWx1ZSI6Ik9ZRnQ3VUN6OUxGS0NkbzdXQ1VlMXpicXlIXC80QUt1cTFWeVZNWWNsaXRzY2FVR21cL3ZzazAzRVdrV0xCRkZ6NDRaSkFFbzhXekU1RUUyZVNjYjhNK2dGS0xCNkRUdkJZUTZveEJxSmc1d1NiYnVCYVwvcW9DUmpoS1pLY0hMZGZmIiwibWFjIjoiMmJmYzU1NWNjZWZhNThmMTM3ZmFkY2E5MWEzMjQ0OTExMjYxOWQwZTdlMTc0ZTE5MjhjMjEwYTVhZjVhMDM3MiJ9; laravel_session=eyJpdiI6InVUbmdNajMrOGVQaEJKbTdIbFdtMXc9PSIsInZhbHVlIjoiRDBTT2xleFJqKzZLakJQQkdHalY3SFRldFFOUElIQkVYQjNlWHl3Yk0xVkxnc2h1cVBMc1Y2T2hJXC9SV3F3d1hITTVzWncyVmt2cGZ3cThweFM3NVlzUnhibHQzc2xoVUt5dTNlRk14VUt0bVJZbWxJOUcwSmdEM1FQbWgzOVcxIiwibWFjIjoiODUyMDU3ZTc3Y2JkMzk0OTYwM2Y1ZjUzODhjY2M0OTdlY2YwYTIzNmQ3MDIyZGQ5MTY4ZDhhNzIwZTNlODgwYyJ9; i26Zr0RgYLzH8MeB3LZm4j7Ud7SGTHTrBC0twXpl=eyJpdiI6InA2R0NYd2J5eDMwdG9jaVZabGRnbEE9PSIsInZhbHVlIjoiUytEUEdrU1F0QXkxTTE1VUg0cnErVjlEMFRVYnVBYUk4YXZFU1JRQjduWHI4N3ZMcWtIa3hoMTB1bXZIcWJxV01ONnRVXC94SXV6NjZuM1BwOE02TTRGeEc2VFNoeFkyYmJ1U1czOWYyTCtDWDc0d1liNzJQNkJRSzJFOUREUU1ScmNWWTFmM2NmZnFVemhkQkVyb3hcL3lGemhtdCtCdXFmbEVnUVhITk1uOW5wcHJmK09xRlJqd1hiUjZtN3VcL0c3S1NOejV1NXdIbWh1bG55YkhUaXdmemJnU1l2UG9HVTU3WUo5enlValhtK3JwOFlmWUE5VzY2dSszc1NSNEJJTmU0MDdkMUVnUnhZT29GWDJyYVFKUE5mOXZDSTZuc2hOSHNtaGVHeUhmOGl5dG9XYUdyUDBnUG1QMUJoQ1hGZWNBSlFQWmI0SFoxQlwvaDBjcll5RWFEdzltVmYyTFRcL2RrVlhLR2lwSTNGdzdlbDhndlJ2QVN5Z2JGaHJiUjNWMVwvIiwibWFjIjoiODNlZDhjN2U1MzhjOWM0YjY1M2M5NjMxMjM4NzVlOTQ1NzQzNzdiNWE0YjUyMDM1YjgyNmUxYWZkYmE1MDFiZiJ9",
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36"
})
with req.urlopen(root) as re:
    data=re.read().decode("utf-8")

from bs4 import  BeautifulSoup as be
cr=be(data,"html.parser")
name=cr.find_all("a", class_="ui__blueLink topPlayers__name")

arr=[]
for na in name:
    x=na.string
    arr.append(x)

arr1=[]
cu=cr.find_all("div",class_="topPlayers__cup")
for c in cu:
    y=c.string
    arr1.append(y)

with open("Clash Royal.txt", mode="w", encoding="utf-8") as cr:
    for i,o in zip(arr,arr1):
        zo=i+" is "+o+" trophies "
        cr.write(zo)
        cr.write("\n***\n")