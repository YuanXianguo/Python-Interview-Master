"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
"""


def lengthOfLongestSubstring(s):
    if not s:
        return 0
    if len(s) == 1:
        return 1
    flag = 1
    longest = 0
    while flag < len(s):
        if s[flag] not in s[:flag]:
            flag += 1
        else:
            if longest < flag:
                longest = flag
            tmp = s[flag]
            s = s[s.index(tmp)+1:]
            flag = s.index(tmp) + 1
    if longest < flag:
        longest = flag
    return longest


def length2(s):
    """滑动窗口"""
    if not s:
        return 0
    if len(s) == 1:
        return 1
    left, right = 0, 1  # 创建左右两个指针作为滑动窗口的端点
    max_l = 0
    while right < len(s):  # 右指针不断右移
        # 如果滑动窗口右端值与滑动窗口某个值重复，就更新左端点：新左端点为滑动窗口中重复值索引的下一位
        # 注意求重复索引时应从滑动窗口左端点开始，否则会得到滑动窗口之外的错误索引
        if s[right] in s[left:right]:
            if max_l < right - left:  # 更新最大值
                max_l = right - left
            left = s.index(s[right], left) + 1
        right += 1  # 右指针不断右移
    if max_l < right - left:  # 更新最大值
        max_l = right - left
    return max_l


if __name__ == '__main__':
    print(lengthOfLongestSubstring("pwabwkeww"))
    print(length2("pwwkew"))
    print(length2("abc"))
    print(length2("wwkew"))
