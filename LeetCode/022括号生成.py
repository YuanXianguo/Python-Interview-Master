"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""


class Solution:
    def generateParenthesis(self, n: int):
        self.n = n
        self.res = list()
        self.backtrack("", 0, 0)
        return self.res

    def backtrack(self, s, left, right):
        if len(s) == 2 * self.n:
            self.res.append(s)
            return
        if left < self.n:
            self.backtrack(s + "(", left + 1, right)
        if right < left:
            self.backtrack(s + ")", left, right + 1)
