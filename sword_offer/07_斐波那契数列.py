from functools import wraps


def decorate(func):
    mem_d = {}

    @wraps(func)
    def inner(*args):
        if args not in mem_d:
            mem_d[args] = func(*args)
        return mem_d[args]
    return inner


@decorate
def feibo_digui(n):
    if n < 3:
        return 1
    return feibo_digui(n-2) + feibo_digui(n-1)


def feibo_iter(n):
    a, b = 0, 1
    while n:
        b, a = a + b, b
        n -= 1
    return a


def fibo(n):
    res = [0, 1]
    while len(res) <= n:
        res.append(res[-1] + res[-2])
    return res[n]


def fibo_dp(n):
    dp0, dp1 = 0, 1
    for i in range(n):
        dp0, dp1 = dp1, dp0 + dp1
    return dp0


if __name__ == '__main__':
    for i in range(10):
        print(feibo_iter(i+1), end=" ")
    print("")
    for i in range(10):
        print(feibo_digui(i+1), end=" ")
    print("")
    for i in range(10):
        print(fibo(i+1), end=" ")
    print("")
    for i in range(10):
        print(fibo_dp(i), end=" ")

