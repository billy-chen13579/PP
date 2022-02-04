#https://www.youtube.com/watch?v=NBuED2PivbY 12:52 11/18
from selenium import webdriver as web
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import time

path ="/Users/billychen/Desktop/chromedriver"

wd = web.Chrome(path)

def get_from_google(wd, delay, max_image):
    def scroll_down(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)
    
    url="https://www.google.com/search?q=cat&tbm=isch&ved=2ahUKEwjIldKzvqb0AhUEB94KHfq5ARMQ2-cCegQIABAA&oq=cat&gs_lcp=CgNpbWcQAzIFCAAQgAQyCAgAEIAEELEDMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgARQmQVYmQVgrwdoAHAAeACAAbQBiAHQApIBAzAuMpgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=C62YYYjkHYSO-Ab684aYAQ&bih=1076&biw=2133&hl=zh-TW"
    wd.get(url)
    
    image_url = set()
    skips=0
    while len(image_url) + skips < max_image:
        scroll_down(wd)
        
        thumbnails = wd.find_elements(By.CLASS_NAME,"Q4LuWd")
        for img in thumbnails[len(image_url) + skips:max_image]:
            try:
                img.click()
                time.sleep(delay)
            except:
                continue
            
            images = wd.find_elements(By.CLASS_NAME, "n3VNCb")
            for image in images:
                if image.get_attribute('src') in image_url:
                    max_image += 1
                    skips += 1
                    break
                    
                if image.get_attribute("src") and "http" in image.get_attribute("src"):
                    image_url.add(image.get_attribute("src"))
                    print(f'Found {len(image_url)}')
                    
    
    return image_url
        
#image_url="https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png"

def download(downpath, url, filename):
    try:
        image_content=requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = downpath + filename
        
        with open(file_path, "wb") as f:
            image.save(f, "JPEG")
            
        print("success")
    except Exception as ef:
        print('failed-', ef)
        

#download("",image_url, "test.jpg")
urls = get_from_google(wd,1,3)
for i, url in enumerate(urls):
    download("imgs", url, "00" + str(i) + ".jpg")
wd.quit()