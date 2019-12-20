"""题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。"""
num = eval(input("输入奇数："))
count = 0
resnum = 0
if num % 2 == 0:
    print("输入错误")
else:
    res = 0
    while True:
        count += 1
        res = res * 10 + 9
        if res % num == 0:
            resnum = len(str(res))
            break
        elif count > 1000:
            print('不能被n个9整除')
            break
    print(resnum)
