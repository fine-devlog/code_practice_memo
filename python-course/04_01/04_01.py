x = int(input("一つ目の数字を入力してください。："))
y = int(input("二つ目の数字を入力してください。："))

def wa(x,y):
    tasizan=0
    tasizan=x+y
    return tasizan

def sa(x,y):
    hikizan=0
    hikizan=x-y
    return hikizan

def seki(x,y):
    kakezan=0
    kakezan=x*y
    return kakezan

def syou(x,y):
    warizan=0
    warizan=x//y
    return warizan

print("足し算の結果は", wa(x,y), "です。")
print("引き算の結果は", sa(x,y), "です。")
print("掛け算の結果は", seki(x,y), "です。")
print("割り算の結果は", syou(x,y), "です。")

def yen_to_dollar(rate, yen):
    dollar = yen *rate
    return dollar

def dollar_to_yen(rate, dollar):
    yen = dollar / rate
    return yen

rate=float(input("為替レートを入力してください（ドル/円）："))
yen = float(input("円を入力してください。："))
dollar = yen_to_dollar(rate, yen)
print("円からドルへの変換結果は", dollar, "ドルです。")
dollar_input = float(input("ドルを入力してください。："))
yen_result = dollar_to_yen(rate, dollar_input)
print("ドルから円への変換結果は", yen_result, "円です。")