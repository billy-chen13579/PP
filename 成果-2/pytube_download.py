from pytube import YouTube

url = 'https://www.youtube.com/watch?v=BSfbjrqIw20&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=2'
yt = YouTube(url)
path = '/Users/billychen/Downloads/廢圖'
print('下載中')
yt.streams.get_highest_resolution().download(path)
print('下載完成')