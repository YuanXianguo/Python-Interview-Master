"""
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
"""


def hammingDistance(x, y):
    x_b = "{:0>32}".format(bin(x)[2:])
    y_b = "{:0>32}".format(bin(y)[2:])
    cnt = 0
    for i in range(32):
        if x_b[i] != y_b[i]:
            cnt += 1
    return cnt


def han2(x, y):
    return bin(x ^ y).count("1")


if __name__ == '__main__':
    print(hammingDistance(1, 4))
    print(han2(1, 4))
