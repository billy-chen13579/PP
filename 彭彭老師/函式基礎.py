#return就像是韓世忠的print，是一個結果
#定意函式
#函式內部，若是不呼叫，就不會有執行
def multiply(n1,n2): #multiply為此函式的名稱
    print(n1*n2) #這一個print是把所有multiply()中的指令個別印出來
    return n1*n2 #回傳：跑完程式後回傳，如果沒有就是none，有回傳值才能使函式外部的指令和內部的指令結合
#呼叫函式
multiply(3,4) #此動作為呼叫，呼叫函示名稱，每一次都可以改，讓內部命令有彈性
value=multiply(3,6)+multiply(6,7) #(3*6)+(6*7)
print(value) #這個print是把value的指領印出來，而value中的指令和前面的函示有關

#程式的包裝
def calculate(max): #呼叫函式後，可以換出呼叫中的指令
    sum=0
    for x in range (1,max+1):
        sum=sum+x
    print(sum)
#    return sum #將函式外部的運算回傳至內部
calculate(10)
calculate(20)
#oct=calculate(10)+calculate(20) #這行程式的值是藉由回傳跑的，沒有回傳就讀不到這裡
#print(oct)

#return的定義：return後面的函式為呼叫完後回傳在跑的函示
#e.g.
def say(g):
    print(g)
    return #return後面沒有東西，就是none
v=say("hhh") #這次呼叫會先被原先的函式接收，再回傳至return
print(v) #return的回傳職為none，所以印出none

