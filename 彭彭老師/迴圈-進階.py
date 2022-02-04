#break 的簡易範例
n=0
while n<5:
    if n==4:
        break #當n=4時，結束迴圈（不會顯示出來）
    print(n) #印出迴圈中的n
    n+=1  #每跑一次迴圈，n+1
print("最後的n: ", n) #印出迴圈結束後的n（4)

#continue 的簡易範例
f=0
for x in [0,1,2,3,4,5,6,7]: #會跑6次，但是如果遇到偶數，就會跳過之後的程式，重新continue
    if x%2==0: #代表x除2之後的餘數是0，也就是說，x是偶數
        continue #達成條件就跳過之後的程式，直接跑下一圈(不列印x=0,2,4)，照著if指示，如果是True，continue成立，反之
    print(x) #如果迴圈跑到這裡，就列印
    f+=1 #因為迴圈跑到這行的有三次，因此f會加三次1
print("最後的f: ", f) #程式run 完之後的f

#while迴圈版本
x=0
while x<=7:
    x+=1 
    if x%2==0: 
        continue 
    print(x) 
    n+=1 #先定義n，之後會用到


#else 的簡易範例    
sum=0 #sum的初始值
for x in range(11): #假設x範圍(0-10)
    sum=sum+x #計算總和的公式
else: #如果x大於10（x不在range(11)之內的話），跑else
    print(sum) #列印最後的sum

#綜合範例：練習，輸入一個可開根號的整數，可以得到整數平方根
#意思就是說，輸入9，得到3
#使用者輸入11，得到（沒有），因為並非整數平方根
n=input("輸入一個正整數：")
n=int(n) #將使用者輸入的轉換成數字
for h in range(n): #代表，h=0 ~(n-1)
    if h*h==n:
        print("整數平方根:",h)
        break #如果是True，就會執行break結束迴圈，就不會跑else
else:
    print("錯誤資訊，請輸入新的正整數") #不會出現小數因爲range中沒有小數

