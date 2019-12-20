"""题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？
程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。"""
i = eval(input())
if i <= 100000:
    jjin = i*10/100
elif i <= 200000:
    jjin = 100000*10/100 + (i-100000)*7.5/100
elif i <= 40:
    jjin = 100000*(10+7.5)/100 + (i-200000)*5/100
elif i <=60:
    jjin = 100000*(10+7.5)/100 + 200000*5/100 + (i-400000)*3/100
elif i <=100:
    jjin = 100000*(10+7.5)/100 + 200000*(5+3)/100 + (i-600000)*1.5/100
else:
    jjin = 100000*(10+7.5)/100 + 200000*(5+3)/100 + 400000*1.5/100 + (i-1000000)*1/100
print(jjin)
#答案
i = int(input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(6):
    if i > arr[idx]:
        r += (i-arr[idx])*rat[idx]
        i = arr[idx]
print(r)
