#判斷式
x=input("請輸入數字：") #以字串形式輸入
x=int(x)  #將字串型態轉成數字
if x>100: #輸入指令，如果數字大於100，則電腦判斷True，列印if 之後的資訊
    print("大於100") #情況為True時電腦會顯示這一行
elif x>50:
    print("小於100，大於50")
else:
    print("小於50") #情況為False時電腦會顯示這一行，電腦判讀（50)為小於50

#判斷式運算
n1=int(input("請輸入數字一：")) 
n2=int(input("請輸入數字二："))
print(n1+n2) #計算使用者輸入後的數字

#進階運算
s1=int(input("輸入數字一：")) 
s2=int(input("輸入數字二：")) 
oo=input("請輸入運算符號：+,-,*,/:") #使用者輸入第三個指令
if oo=="+": 
    print(s1+s2) #輸入指令，照著這個格式
elif oo=="-":    #輸入多個指令時，以elif為開始
    print(s1-s2) 
elif oo=="*":
    print(s1*s2)
elif oo=="/":
    print(s1/s2)
else:
    print("error")
