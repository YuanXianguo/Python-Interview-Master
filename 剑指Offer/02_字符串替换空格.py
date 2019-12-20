"""
题目：请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""


def replace_bs_split(string):
    """以空格分割成列表，再拼接成字符串"""
    lst = string.split()
    return "%20".join(lst)


def replace_bs_replace(string):
    """使用replace方法"""
    return string.replace(" ", "%20")


def replace_bs_iter(string):
    """使用迭代"""
    res = ""
    for s in string:
        if s == " ":
            res += "%20"
        else:
            res += s
    return res


if __name__ == '__main__':
    s = "we are happy"
    print(replace_bs_split(s))
    print(replace_bs_replace(s))
    print(replace_bs_iter(s))

