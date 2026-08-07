x=input("１つ目の値(小数も可)を入力してください：")
y=input("２つ目の値(小数も可)を入力してください：")
if x>y:
    z=(str(x))-(str(y))
    print(f"一つ目の数字の方が{z}だけ大きいです")
elif y>x:
    z=(str(y))-(str(x))
    print(f"二つ目の数字の方が{z}だけ大きいです")
else:
    print(f"二つの数字の値は等しいです。")

s=input("文字列を入力してください：")
if "あ" or "い" or "う" or "え" or "お" in s:
    print("入力された文字列には、あいうえおのいずれかが含まれています。")
if "あ" and "い" and "う" and "え" and "お" in s:
    print("入力された文字列には、あいうえおのすべてが含まれています。")

x=input("１つ目の値(小数も可)を入力してください：")
print(float(x))
print(int(x))

if x%2==0:
    print("入力された値は偶数です。")
    if x%3==0:
        print("入力された値は6の倍数です。")
    elif x%5==0:
        print("入力された値は10の倍数です。")
else:
    print("入力された値は奇数です。")

z=int(input("年齢を整数を入力してください："))
if z>=20:
    if z>=65:
        print("あなたは高齢者です。")
    else:
        print("あなたは成人です。")
else:
    print("あなたは未成年です。")

