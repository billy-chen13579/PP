#while迴圈 #給數字初始值＆其範圍＆數字改變的頻率 #跑到指令範圍之後才會結束
n=1     #n 的初始值
while n<=10: #n的最大值。如果指令為True，則數字會一直跑到無限
    print(n)  #因為有前面的空格，所以指令聯通的
    n+=2 #數列指令，每格的差距，每一次累加的值

#累加之後的總值
n=1     #n 的初始值
sum=0   #用於記錄累加的結果 #這地方代表sum的初始值
while n<=100: #n的最大值+1
    sum=sum+n
    n+=1 #數列指令，每格的差距，每一次累加的值
print(sum)

print("hello")
#for 迴圈 #給數字和其條件，然後把所有直列出來 #跑完就結束
lum=0   #累加的結果
for x in range(1,11):
    lum=lum+x
print(lum)

for y in [3,4,5,123]:
    print(y)

