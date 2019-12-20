"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

"""
from collections import deque


def letterCombinations(digits):
    # 定义一个映射字典
    dic = {"2": ["a", "b", "c"],
           "3": ["d", "e", "f"],
           "4": ["g", "h", "i"],
           "5": ["j", "k", "l"],
           "6": ["m", "n", "o"],
           "7": ["p", "q", "r", "s"],
           "8": ["t", "u", "v"],
           "9": ["w", "x", "y", "z"]}
    # 定义一个队列
    res = deque()
    flag = 0
    while flag < len(digits):  # 对输入数字序列遍历
        if not res:  # 如果结果集为空，说明刚开始遍历第一个数字
            for i in dic[digits[flag]]:  # 直接将2对应字符添加到结果集中
                res.append(i)
        else:
            length = len(res)
            # 根据当前结果集长度遍历结果集，每次取出一个元素，将取出的元素依次添加当前数字对应的映射
            while length:
                tmp = res.popleft()
                for i in dic[digits[flag]]:
                    res.append(tmp + i)
                length -= 1
        flag += 1
    return list(res)


class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        self.map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        self.res = []
        self.get_letter("", digits)
        return self.res

    def get_letter(self, path, digits):
        if not digits:
            self.res.append(path)
            return
        for i in self.map[digits[0]]:
            self.get_letter(path + i, digits[1:])


if __name__ == '__main__':
    print(letterCombinations("23"))
