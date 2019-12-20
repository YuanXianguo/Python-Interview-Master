def height(n):
    if n == 1:
        h = 50
    else:
        h = height(n-1)/2
    return h
def main():
    n = eval(input("输入弹起次数："))
    res = 0
    for i in range(1,n+1):
        res += height(i)*3
    print(res,height(n))
main()
