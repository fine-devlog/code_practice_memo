def average(num_list):
    return(sum(num_list)/len(num_list))


def variance(num_list):
    avg=int(average(num_list))
    print(avg)
    bunnsann=0
    for x in num_list:
        bunnsann+=(x-avg)**2
    print(bunnsann/len(num_list))

height_list=[170,180,165,155,175]
weight_list=[45,50,55,60,75,53]

average(height_list)
variance(height_list)
average(weight_list)
variance(weight_list)

#関数の戻り値を用いて別の関数の処理を行う場合、printだけでなくreturnで返さなければ別の関数で利用ができず、Noneとなってしまう
player1 = {'名前':'太郎', 'レベル':10, '体力':110, '攻撃力':23,'防御力':54, '所持金':3000}

def level_up(p, param,price):
    p['体力']=int(p['体力']*param)
    p['攻撃力']=int(p['攻撃力']*param)
    p['防御力']=int(p['防御力']*param)
    p['レベル']+=1
    p['所持金']=int(p['所持金']-price)
    return
    
print(player1)
level_up(player1, 1.3,1500)
print(player1)

def double_elements_in_place(num_list):
    for i in range(len(num_list)):
        print(num_list[i]*2)

numbers=[1,2,3,4,5]
double_elements_in_place(numbers)
