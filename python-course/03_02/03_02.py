str_list=["apple", "banana", "cherry", "peach", "grape"]
for x in str_list:
    print(x)

A=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
s=0
s=A[0]+A[1]+A[2]+A[3]+A[4]+A[5]+A[6]+A[7]+A[8]+A[9]+A[10]+A[11]+A[12]+A[13]+A[14]+A[15]+A[16]+A[17]+A[18]+A[19]
print(s)
z=0
for i in range(len(A)):
    z+=A[i]
print(f"リストの合計は{z}です。")
print(f"リストの平均は{z/len(A)}です。")

num_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(num_list)):
    print(num_list[i])

for i in range(10):
    print(i+1)

for i in range(1,11):
    print(i)

for i in range(10,0, -1):
    print(i)

count1=0
count2=0
count3=0
for i in range(1,101):
    if i%3==0 and i%5==0:
        count1+=1
    elif i%3==0:
        count2+=1
    elif i%5==0:
        count3+=1
print(f"1から100までのFizzBuzz: {count1}回, Fizz: {count2}回, Buzz: {count3}回")