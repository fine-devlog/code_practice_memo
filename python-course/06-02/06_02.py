import math as m
heihoukonn=m.sqrt(int((input("自然数を入力してください。："))))
print(f"{heihoukonn*heihoukonn}の平方根は{heihoukonn}です")

pi_value=m.pi
hannkei=int(input("正の数を入力してください："))
print(f"π={pi_value},半径を{hannkei}とする円の面積は{pi_value*hannkei*hannkei},弧の長さは{pi_value*2*hannkei}です")

a=int(input("自然数を入力してください："))
log_base_10=m.log10(a)
print(f"log10({a})={log_base_10}")
log_base_2=m.log2(a)
print(f"log2({a})={log_base_2}")

print("xのy乗を計算します")
suuji=int(input("xに入れる数字を入力して下さい："))
sisuu=float(input("yに入れる数字を入力してください："))
print(f"入力された数字を計算すると、{suuji}の{sisuu}乗で、",m.pow(suuji,sisuu))

zettaiti=int(input("絶対値を調べたい数字を入力してください："))
z_ti=m.fabs(zettaiti)
if zettaiti==0:
    print(f"{zettaiti}の絶対値は{z_ti}で、ほかにこの数字を絶対値に持つ数字はありません。")
else:
    print(f"{zettaiti}の絶対値は{z_ti}で、ほかにこの数字を絶対値に持つのは{-1*zettaiti}です")

