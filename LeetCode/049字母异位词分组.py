"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
"""


def groupAnagrams(strs):
    if not strs:
        return []
    res = []  # 记录结果
    tmp = []  # 记录结果集中各项的排序字符集
    for s in strs:
        if sorted(s) in tmp:  # 如果当前字符串排序后出现在临时数组中
            # 根据临时数组中索引，将当前字符串添加到结果集对应索引列表中
            res[tmp.index(sorted(s))].append(s)
        # 如果还没出现过当前字符串，新建一个包含当前字符串的列表，并将列表添加到结果集中
        else:
            tmp.append(sorted(s))
            res.append([s])
    return res


class Solution:
    def groupAnagrams(self, strs):
        res = dict()
        for s in strs:
            tmp = "".join(sorted(s))
            if tmp in res:
                res[tmp].append(s)
            else:
                res[tmp] = [s]
        return res.values()


if __name__ == '__main__':
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(groupAnagrams([""]))

    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
