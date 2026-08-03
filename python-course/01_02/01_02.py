print("Hello, \nWorld!")
a=10
print(f"現在、私は{a}歳です。")
b=10
print(f"{b}年後には、私は{a+b}歳になります。")
a=[ 1,2,3,4,5]
print(a)
print(a[3])
print(len(a))
e=[0,1,2,3,4,5,6,7,8,9]
print(e[0:7:2])
print(e[2:-3])
e[9]=100
print(e)
e[9]=9
e.append(100)
print(e)
f=[200,300,400,500]
e.extend(f)
print(e)
g=[600,700,800,900,1000]
e=e+g
print(e)
del e[-1]
print(e)
