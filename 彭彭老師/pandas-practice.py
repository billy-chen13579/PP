# 載入 pandas 模組
import pandas as pd
# 建立 Series
data=pd.Series([20,10,15])
# 基本 Series 操作
#print(data)
print("max",data.max()) #最大值
print("median",data.median()) #中位數
data=data*2 #所有資料乘以2
print(data)
da=data==20 #判斷data中的資料是否為20，回傳布林值
print(da)

# 建立 DataFrame
data=pd.DataFrame({
    "fruit":["banana","apple","orange"],
    "number":[3,5,4]
})
print(data,"\n")
# 基本 DataFrame 操作
print(data["fruit"]) #取得特定的欄位
print(data.iloc[0]) #取得特定的列