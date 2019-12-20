"""
题目：将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。
数值为0或者字符串不是一个合法的数值则返回0
"""


def get_int(string):
    if not string:
        return 0

    def get_int_(string):
        """不考虑符号的转换"""
        if not string.isdecimal():
            return 0
        res = 0
        for i in range(len(string)):
            for digit in range(10):
                if string[i] == str(digit):
                    res = res * 10 + digit
                    break
        return res

    if string[0] == "-":
        return -get_int(string[1:])

    return get_int_(string)


def StrToInt(s):
    # write code here
    if not s:
        return 0

    def get_int(s):
        """不考虑符号"""
        s.is
        if not s.isdecimal():
            return 0
        res = 0
        for i in s:
            for d in range(10):
                if str(d) == i:
                    res = res * 10 + d
        return res

    if s[0] == "-":
        return -get_int(s[1:])
    return get_int(s)


if __name__ == '__main__':
    print(get_int("-184524"))
    print(StrToInt("123"))





