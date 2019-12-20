"""
题目：写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
"""


def get_sum(num1, num2):
    return sum([num1, num2])


if __name__ == '__main__':
    print(get_sum(1, 2))
