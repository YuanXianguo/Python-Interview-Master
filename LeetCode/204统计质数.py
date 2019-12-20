def countPrimes(n):

    def is_prime(num):
        """判断一个是否质数"""
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    cnt = 0
    for i in range(2, n):
        if is_prime(i):
            cnt += 1
    return cnt


def countP(n):
    """
    厄拉多塞筛法
    先将 2~n 的各个数放入表中，然后在2的上面画一个圆圈，然后划去2的其他倍数；
    第一个既未画圈又没有被划去的数是3，将它画圈，再划去3的其他倍数；
    现在既未画圈又没有被划去的第一个数 是5，将它画圈，并划去5的其他倍数……
    依次类推，一直到所有小于或等于 n 的各数都画了圈或划去为止。
    这时，表中画了圈的以及未划去的那些数正好就是小于 n 的素数。
    """
    if n < 3:
        return 0
    lst = [1] * n
    index = 2
    while index <= pow(n, 0.5):
        if lst[index]:
            tmp = index + index
            while tmp < n:
                lst[tmp] = 0
                tmp += index
        index += 1
    return lst.count(1) - 2


if __name__ == '__main__':
    for i in range(10):
        print(countP(i))
    print(countP(10))
    # print(countP(499979))
