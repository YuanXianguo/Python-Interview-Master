"""
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。
"""


def numDecodings(s):
    if not s or s.startswith("0"):
        return 0
    dp = [0] * len(s)
    dp[0] = 1
    for i in range(1, len(s)):
        if s[i] != "0":
            dp[i] += dp[i-1]
        if s[i-1] != "0" and int(s[i-1:i+1]) <= 26:
            tmp = dp[i-2] if i-2 >= 0 else 1
            dp[i] += tmp
    return dp[-1]


if __name__ == '__main__':
    print(numDecodings("226"))
