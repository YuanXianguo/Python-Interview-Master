"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
"""


def longestPalindrome(s):
    if len(s) <= 1:
        return s

    def center_spread(s, left, right):
        """中心扩展法，分为偶数长子串和奇数长子串"""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right], right - left - 1

    longest = 0
    res_str = ""
    for i in range(len(s)):
        even_str, even_l = center_spread(s, i, i+1)
        odd_str, odd_l = center_spread(s, i, i)
        if even_l > odd_l:
            this_str, this_l = even_str, even_l
        else:
            this_str, this_l = odd_str, odd_l

        if this_l > longest:
            longest = this_l
            res_str = this_str

    return res_str


def longest2(s):
    """动态规划"""
    if len(s) <= 1:
        return s
    # dp是一个二维bool，dp[i][j]=true表示s[i:j]（包括i,j）是一个回文子串
    dp = [[False for i in range(len(s))] for i in range(len(s))]
    longest = 1
    res_str = s[0]

    for j in range(1, len(s)):
        for i in range(j):
            # 如果当前i,j对应的子符相同
            # 且间隔距离小于等于2（内部只有1个或无字符）或内部也是回文子串
            if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                dp[i][j] = True
                if j - i + 1 > longest:
                    res_str = s[i:j+1]
                    longest = j - i + 1
    return res_str


if __name__ == '__main__':
    print(longestPalindrome("babad"))
    print(longest2("babad"))
