"""
题目：求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case
等关键字及条件判断语句（A?B:C）。
"""


def get_sum(n):
    lst = [1]
    try:
        return lst[n-1]
    except:
        return get_sum(n-1) + n


def get_sum2(n):
    return sum(list(range(1, n+1)))


if __name__ == '__main__':
    print(get_sum(4))
    print(get_sum2(4))
