def firstUniqChar(s):
    tmp = {}
    for i in range(len(s)):
        if s[i] in tmp:
            tmp[s[i]][1] += 1
        else:  # 字典的value为一个记录key字母第一次出现时的索引和出现的次数的列表
            tmp[s[i]] = [i, 1]
    # dict.values()会自动排序
    for index, cnt in tmp.values():
        if cnt == 1:
            return index
    return -1


if __name__ == '__main__':
    print(firstUniqChar("loveleetcode"))
