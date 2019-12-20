try:
    n = eval(input())
    if 90 <= n <= 100:
        grade = 'A'
    elif 60 <= n < 90:
        grade = 'B'
    elif 0 <= n < 60:
        grade = 'C'
    print("你的成绩等级为{}".format(grade))
except:
    print("输入错误！")
else:
    print("加油！")
finally:
    print("好好学习，天天向上！")
