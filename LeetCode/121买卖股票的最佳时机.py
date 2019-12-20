"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。
"""
"""
状态转移方程：i，日期；k，剩余最大交易次数；0/1，是否持有
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
解释：今天我没有持有股票，有两种可能：
    要么是我昨天就没有持有，然后今天选择rest，所以今天还是没有；
    要么我昨天持有股票，但是今天选择sell了，所以今天没有持有。
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
解释：今天我持有股票，有两种可能：
    要么我昨天就持有股票，然后今天选择rest，所以今天还是持有；
    要么我昨天没有，今天选择buy，所以今天持有。
    在buy的时候更新k，也可以在sell时更新。
"""
"""
定义基例：
dp[-1][k][0] = 0，因为i从0开始，所以i=-1意味着还有开始，利润当然是0。
dp[-1][k][1] = float("-inf")，还没开始时是不可能持有股票的，用负无穷表示不可能。
dp[i][0][0] = 0，k=0意味着根本不允许交易，利润是0。
dp[i][0][1] = float("-inf")，不允许交易是不可能持有股票的。
"""


def maxProfit(prices):
    """k=1，根据基例可以做一些化简：
    dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
    dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - prices[i])
                = max(dp[i-1][1][1], -prices[i])
    解释：k = 0 的 base case，所以 dp[i-1][0][0] = 0。

    现在发现 k 都是 1，不会改变，即 k 对状态转移已经没有影响了。
    可以进行进一步化简去掉所有 k：
    dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
    dp[i][1] = max(dp[i-1][1], -prices[i])
    """
    if not prices:
        return 0
    n = len(prices)
    dp = []
    for i in range(n):
        dp.append([0, 0])
    # 穷举所有i
    for i in range(n):
        if i == 0:    # 定义基例
            dp[i][0] = 0  # dp[0][0] = max(dp[-1][0], dp[-1][1]+prices[0]) = max(0, -inf)
            dp[i][1] = -prices[0]  # dp[0][1] = max(dp[-1][1], -prices[0]) = max(-inf, -prices[0])
        else:
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])
    return dp[n-1][0]


def maxProfit2(prices):
    """
    上面处理基例很麻烦，而且注意到状态转移方程，新状态只和相邻的一个状态有关，
    只需要一个变量储存相邻的状态就够了，可以把空间复杂度降到O(1)
    """
    if not prices:
        return 0
    n = len(prices)
    dp_i_0 = 0
    dp_i_1 = float("-inf")
    for i in range(n):
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, -prices[i])
    return dp_i_0

