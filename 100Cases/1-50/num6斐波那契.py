def feibo(n):
    if n == 0:
        res = 0
    elif n == 1:
        res = 1
    else:
        res = feibo(n-1) + feibo(n-2)
    return res
def main():
    try:
        n = eval(input())
        m = 0
        for i in range(n+1):
            print(feibo(i),end=', ')
            m += feibo(i)
        ave = m / n
        print("总和：{},平均值{}".format(m,int(ave)) )
    except:
        pass

main()
