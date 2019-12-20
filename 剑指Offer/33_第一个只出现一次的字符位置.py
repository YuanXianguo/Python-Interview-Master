"""
题目：在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个
只出现一次的字符,并返回它的位置
"""


def get_first_alp(str):
    if not str:
        return -1
    for s in str:
        if str.count(s) == 1:
            return str.index(s), s



class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        tmp = dict()
        for i in range(len(s)):
            if s[i] in tmp:
                tmp[s[i]][1] += 1
            else:
                tmp[s[i]] = [i, 1]
        res = -1
        li = sorted(tmp.values(), key=lambda i: i[0])
        for i, v in li:
            if v == 1:
                res = i
                break
        return res


if __name__ == '__main__':
    print(get_first_alp("abcdabce"))
    print(get_first_alp("google"))

    s = Solution()
    print(s.FirstNotRepeatingChar("google"))
