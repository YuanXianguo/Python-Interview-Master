"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
"""


def isValid(s):
    # 定义一个括号有效值的映射
    dic = {"(": ")", "[": "]", "{": "}"}
    stack = []  # 定义一个堆栈
    flag = 0
    while flag < len(s):  # 对输入字符串遍历
        if s[flag] in dic:  # 如果是左括号，直接入栈
            stack.append(s[flag])
        # 如果是右括号，且堆栈不为空，如果是栈顶括号和当前括号对应，就pop栈顶括号
        elif s[flag] in dic.values() and stack and s[flag] == dic[stack[-1]]:
            stack.pop()
        else:  # 如果栈顶括号和当前括号不对应，则无效
            return False
        flag += 1
    if stack:  # 如果遍历结束，堆栈还有左括号，则无效
        return False
    return True


class Solution:
    def isValid(self, s: str) -> bool:
        map = {"(": ")", "[": "]", "{": "}"}
        stack = list()
        for i in s:
            if i in map:
                stack.append(i)
            elif i in map.values() and stack and map[stack[-1]] == i:
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    s.isValid("]")
    print(isValid("{[]}"))
    print(isValid("{[]()}"))
    print(isValid("{[]}({})"))
    print(isValid("([)]"))
    print(isValid("["))

