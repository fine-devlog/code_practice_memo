seireki=int(input("西暦を入力してください："))
if seireki%4==0:
    if seireki%100==0:
        if seireki%400==0:
            print(f"{seireki}年はうるう年です。")
        else:
            print(f"{seireki}年はうるう年ではありません。")
    else:
        print(f"{seireki}年はうるう年です。")
else:
    print(f"{seireki}年はうるう年ではありません。")

suuji=float(input("小数を入力してください："))
print(f"入力された値は{suuji}です。")
print(f"入力された値の整数部分は{int(suuji)}です。")
print(f"入力された値の小数部分は{round(suuji-int(suuji), 10)}です。")
print(f"入力された値の小数部分を四捨五入した値は{round(suuji, 0)}です。")

lank={
    "A大学":75,
    "B大学":55,
    "C大学":45,
}
name=input("大学名を入力してください：")
if name in lank:
    print(f"{name}の偏差値は{lank[name]}です。")
else:
    lank[name]=int(input(f"{name}の偏差値を入力してください："))
    print(f"{name}の偏差値は{lank[name]}です。")
    print(lank)