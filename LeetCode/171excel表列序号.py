"""
给定一个Excel表格中的列名称，返回其相应的列序号。
"""


def titleToNumber(s):
    res = 0
    for i in s:
        res = (ord(i) - 64) + res * 26
    return res


if __name__ == '__main__':
    print(titleToNumber("ZY"))

