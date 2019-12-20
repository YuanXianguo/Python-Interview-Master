"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
"""


def isAnagram(s, t):
    def get_u(u):
        return u.encode()
    return sorted(s, key=get_u) == sorted(t, key=get_u)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


if __name__ == '__main__':
    print(isAnagram("anagram", "nagaram"))
