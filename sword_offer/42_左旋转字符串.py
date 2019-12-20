"""
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。
"""


def left_rotate(str, k):
    if len(str) <= k:
        return str
    return str[k:] + str[:k]


def left_rotate2(str, k):
    if len(str) <= k:
        return str
    lst = []
    for i in range(len(str)):
        if i + k < len(str):
            lst.append(str[i+k])
        else:
            lst.append(str[i+k-len(str)])
    return "".join(lst)


if __name__ == '__main__':
    print(left_rotate("abcXYZdef", 4))
    print(left_rotate2("abcXYZdef", 4))

