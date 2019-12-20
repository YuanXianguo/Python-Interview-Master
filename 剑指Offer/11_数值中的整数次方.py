"""
题目：给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
"""


def get_exp(base, exp):
    return pow(base, exp)


if __name__ == '__main__':
    print(get_exp(1.1, 3))
