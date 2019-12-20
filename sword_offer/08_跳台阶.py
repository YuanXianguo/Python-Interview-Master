"""
题目：一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""
"""
对于本题,前提只有一次1阶或者2阶的跳法。
a.如果两种跳法，1阶或者2阶，那么假定第一次跳的是一阶，那么剩下的是n-1个台阶，跳法是f(n-1);
b.假定第一次跳的是2阶，那么剩下的是n-2个台阶，跳法是f(n-2)
c.由a、b假设可以得出总跳法为: f(n) = f(n-1) + f(n-2) 
d.然后通过实际的情况可以得出：只有一阶的时候 f(1) = 1 ,只有两阶的时候可以有 f(2) = 2
"""


def jump(n):
    res = [1, 2]
    while len(res) < n:
        res.append(res[-1]+res[-2])
    return res[n-1]


"""
题目：一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""
"""
因为n级台阶，第一步有n种跳法：跳1级、跳2级、到跳n级
跳1级，剩下n-1级，则剩下跳法是f(n-1)
跳2级，剩下n-2级，则剩下跳法是f(n-2)
所以f(n)=f(n-1)+f(n-2)+...+f(1)
因为f(n-1)=f(n-2)+f(n-3)+...+f(1)
所以f(n)=2*f(n-1)
然后求解这个无穷级数的和，
正确答案应该是：每次至少跳一个，至多跳n个，一共有f(n)=2**(n-1)种跳法
"""


def jump_plus(n):
    res = 1
    if n >= 2:
        for i in range(n-1):
            res *= 2
    return res


def jump_plus2(n):
    return pow(2, n - 1)


if __name__ == '__main__':
    for i in range(10):
        print(jump(i+1), end=" ")
    print("")
    for i in range(10):
        print(jump_plus(i+1), end=" ")
    print("")
    for i in range(10):
        print(jump_plus2(i+1), end=" ")
