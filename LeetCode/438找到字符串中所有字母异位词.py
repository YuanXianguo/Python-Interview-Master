"""
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
说明：
字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
"""


def find_anagram(s, p):
    p = sorted(p)
    len_p = len(p)
    res = []
    for i in range(len(s) - len_p + 1):
        if sorted(s[i:i+len_p]) == p:
            res.append(i)
    return res


class Solution:
    def findAnagrams(self, s: str, p: str):
        res = list()
        window = dict()
        tmp = dict()
        for i in p:
            tmp[i] = tmp.get(i, 0) + 1

        len_s, len_p = len(s), len(p)
        left, right = 0, 0

        while right < len_s:
            if s[right] not in tmp:
                window.clear()
                left = right = right + 1
            else:
                window[s[right]] = window.get(s[right], 0) + 1
                print(window)
                if right - left + 1 == len_p:
                    if window == tmp:
                        res.append(left)
                    # 长度达到
                    # 后左指针需要不断移动
                    window[s[left]] -= 1
                    left += 1
                right += 1
        return res


if __name__ == '__main__':
    print(find_anagram("cbaebabacd", "abc"))
    print(find_anagram("abab", "ab"))

    s = Solution()
    s.findAnagrams("cbaebabacd", "abc")
