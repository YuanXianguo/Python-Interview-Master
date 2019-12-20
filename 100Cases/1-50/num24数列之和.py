"""题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。"""
def fb(n):
    if n == 0:
        res = 1
    elif n == 1:
        res = 1
    else:
        res = fb(n-1) + fb(n-2)
    return res

def main():
    sum = 0
    for i in range(20):
        sum += fb(i+2)/fb(i+1)
    print(sum)

main()
