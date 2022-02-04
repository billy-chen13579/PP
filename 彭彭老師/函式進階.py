#參數預設資料
def power(base, exp=3):
    print(base**exp)
power(3,2)
power(5)

#參數明稱對應
def divide(n1,n2):
    print(n1/n2)
divide(8,2)
divide(n2=8,n1=2) #有特別指定參數資料   
