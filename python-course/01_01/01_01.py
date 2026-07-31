# 計算
x = 10
y = 3
addition = x + y
print(addition)
subtraction = x - y
print(subtraction)
multiplication = x * y
print(multiplication)
division = x / y
print(division)
remainder = x % y
print(remainder)
integer_division = x // y
print(integer_division)
exponentiation = x ** y
print(exponentiation)
#　結果は上から13, 7, 30, 3.3333333333333335, 1, 3, 1000と並ぶ


# 間違った累積代入
x = 10
y = 3
x+=y
print(x)
x-=y
print(x)
x*=y
print(x)
x/=y
print(x)
x%=y
print(x)
x//=y
print(x)
x**=y
print(x)
# 結果は上から13, 10, 30, 10.0, 1.0, 0.0, 0.0と並ぶ


# 正しい累積代入
x = 10
y = 3
x += y
print(x)
x = 10
y = 3
x -= y
print(x)
x = 10
y = 3
x *= y
print(x)
x = 10
y = 3
x /= y
print(x)
x = 10
y = 3
x %= y
print(x)
x = 10
y = 3
x//=y
print(x)
x = 10
y = 3
x **= y
print(x)
#　結果は上から13, 7, 30, 3.3333333333333335, 1, 3, 1000と並ぶ