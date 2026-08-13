def weight(grams):
    pounds = grams * 0.00220462
    kilograms = grams * 0.001
    return pounds, kilograms

def length(meters):
    feet = meters * 3.28084
    centimeters = meters * 100
    kilometers=meters*0.001
    return feet, centimeters, kilometers

grams=float(input("重量（g）を入力してください："))
pounds, kilograms = weight(grams)
print(f"重量は {pounds} ポンドまたは {kilograms} キログラムです。")

meters=float(input("長さ（m）を入力してください："))
feet, centimeters, kilometers = length(meters)
print(f"長さは {feet} フィート、{centimeters} センチメートル、または {kilometers} キロメートルです。")

def age(age):
    if age<18:
        return "未成年"
    elif age<65:
        return "成人"
    else:
        return "高齢者"

age=int(input("年齢を入力してください："))
print(f"あなたは{age}歳で、{age(age)}です。")

def check_num(num):
    if num>0:
        if num%2==0:
            return "正の偶数"
        else:
            return "正の奇数"
    elif num<0:
        if num%2==0:
            return "負の偶数"
        else:
            return "負の奇数"
    elif num==0:
        return "原点"

num=int(input("整数を入力してください："))
print(f"入力された数字は{num}で、{check_num(num)}にあたります。")