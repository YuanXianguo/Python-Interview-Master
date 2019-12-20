"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
"""
r = ""
print(int(r))
def reverse(x):
    if x == 0:
        return 0
    res = x // abs(x) * int(str(abs(x))[::-1])
    if res < -pow(2, 31) or res > pow(2, 31) - 1:
        return 0
    return res


if __name__ == '__main__':
    print(reverse(123))
    print(reverse(-123))
    print(reverse(120))

