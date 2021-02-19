# 判斷式
x = input("請輸入數字:") #取得字串形式的使用者輸入
x = int(x)

if x > 200:
    print("大於 200")
elif x > 100:
    print("大於 100, 小於200")
else:
    print("小於100")
