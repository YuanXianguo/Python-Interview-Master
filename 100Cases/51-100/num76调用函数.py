"""题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n"""
def getNum(num):
    if num % 2 != 0:
        oodd(num)
    else:
        eeven(num)

def oodd(oddnum):
    oddcount = 0
    for i in range(1,oddnum+1,2):
        oddcount += 1 / i
    print(oddcount)

def eeven(evenum):
    evencount = 0
    for i in range(2,evenum+1,2):
        evencount += 1 / i
    print(evencount)

def main():
    num = eval(input("输入数字："))
    getNum(num)
main()
