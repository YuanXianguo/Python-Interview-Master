"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
"""


def longestCommonPrefix(strs):
    if not strs:
        return ""
    flag = 0
    res = ""
    while True:
        if flag > len(strs[0]) - 1:
            return res
        tmp = strs[0][flag]
        for s in strs[1:]:
            if flag > len(s) - 1:
                return res
            if s[flag] != tmp:
                return res
        res += tmp
        flag += 1


def longets2(strs):
    res = ""
    # zip()是Python的一个内建函数，它接受一系列可迭代的对象作为参数，
    # 将对象中对应的元素打包成一个个tuple（元组），然后返回由这些tuples组成的zip对象，
    # 可直接遍历，遍历输出为每个元组，可通过list转为列表；
    # 若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同
    # 如z = zip(["flower","flow","flight"])，通过list(z)转换为列表结果为
    # [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
    for tmp in zip(*strs):
        # 将每个元组通过集合去重，如果集合长度为1，说明全部相同元素
        if len(set(tmp)) == 1:
            res += tmp[0]
        else:
            break
    return res


if __name__ == '__main__':
    print(longets2(["flower","flow","flight"]))

    print(longestCommonPrefix(["flower","flow","flight"]))
    print(longestCommonPrefix(["fl","flower","flow","flight"]))
    print(longestCommonPrefix(["dog","racecar","car"]))

