"""题目：求输入数字的平方，如果平方运算后小于 50 则退出。"""
f = 0
while True:
    num = eval(input("输入数字，平方小于50则退出："))
    f = pow(num,2)
    if f < 50:
        break
    else:
        print("输入数字结果是：{}".format(num))
