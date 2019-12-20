"""
题目：请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，
而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
"""


def match(s, pattern):
    # 同时为空
    if not len(s) and not len(pattern):
        return True
    # 模式为空，匹配不为空
    if len(s) and not len(pattern):
        return False

    # 模式长度大于1，且第二个字符为"*"
    # 如果s[0]==pattern[0]或者pattern[0]=="."，则会有
    # "aaa"和"a*a"的情况，"*"代表多个"a",因此s需要不断右移一位继续比较
    # "a"和"a*a"的情况，"*"代表0个"a"，因此s不需要右移，pattern需要右移两位
    # "abc"和"a*bc"的情况，"*"代表1个"a"，因此s需要右移一位，pattern右移两位继续比较
    if len(pattern) > 1 and pattern[1] == "*":
        if len(s) and (s[0] == pattern[0] or pattern[0] == "."):
            return (match(s[1:], pattern) or match(s, pattern[2:])
                    or match(s[1:], pattern[2:]))
        else:
            return match(s, pattern[2:])

    # pattern长度大于等于1，且第二位不为"*"
    if len(s) and (s[0] == pattern[0] or pattern[0] == "."):
        return match(s[1:], pattern[1:])
    return False


def match2(s, p):
    if not p:
        return not s

    first_match = s and p[0] in {s[0], "."}

    # 如果模式串中有星号，它会出现在第二个位置，即pattern[1]
    # 这种情况下，我们可以直接忽略模式串中这一部分，
    # 或者删除匹配串的第一个字符，前提是它能够匹配模式串当前位置字符
    if len(p) > 1 and p[1] == "*":
        return match2(s, p[2:]) or (first_match and match2(s[1:], p))
    else:
        return first_match and match2(s[1:], p[1:])


def match3(string, pattern):
    if not pattern:
        return not string

    first_match = string and pattern[0] in {string[0], "."}

    if len(pattern) > 1 and pattern[1] == "*":
        return match3(string, pattern[2:]) or (first_match and match3(string[1:], pattern))
    return first_match and match3(string[1:], pattern[1:])


def match4(string, pattern):
    if not pattern:
        return not string
    first_match = string and pattern[0] in [string[0], "."]
    if len(pattern) > 1 and pattern[1] == "*":
        return match4(string, pattern[2:]) or (first_match and match4(string[1:], pattern))
    return first_match and match4(string[1:], pattern[1:])


if __name__ == '__main__':
    print(match("aaa", "a*a"), match("aaa", ".*a"))
    print(match("a", "a*a"), match("a", ".*a"),)
    print(match("abc", "a*bc"))
    print(match2("abc", "a*bc"))
