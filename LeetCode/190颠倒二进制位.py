"""
颠倒给定的 32 位无符号整数的二进制位。
 """


def reverseBits(n):
    tmp = str(bin(n))[2:][::-1]
    while len(tmp) < 32:
        tmp += "0"
    return int(tmp, 2)


def reverseBits2(n):
    tmp = "{:0>32b}".format(n)[::-1]
    return int(tmp, 2)


if __name__ == '__main__':
    print(reverseBits(43261596))
    print(reverseBits(4294967293))
    print(reverseBits2(43261596))
    print(reverseBits2(4294967293))
