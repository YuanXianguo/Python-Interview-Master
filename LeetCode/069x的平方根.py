"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
"""


def my_sqrt(x):
    if not x:
        return 0
    left, right = 0, x
    while left < right:
        mid = (left + right + 1) // 2
        if mid ** 2 > x:
            right = mid - 1
        else:
            left = mid
    return left


if __name__ == '__main__':
    # print(my_sqrt(1))
    # print(my_sqrt(2))
    # print(my_sqrt(4))
    # print(my_sqrt(6))
    print(my_sqrt(8))
    print(my_sqrt(16))
    # print(my_sqrt(17))
    # print(my_sqrt(36))
    # print(my_sqrt(1024))
