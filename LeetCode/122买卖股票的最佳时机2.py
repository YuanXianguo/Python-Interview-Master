def maxProfit(prices):
    """
    如果k为正无穷：
    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
                = max(dp[i-1][k][1], dp[i-1][k][0] - prices[i])
    可简化为：
    dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
    dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
    """
    if not prices:
        return 0
    dp_i_0 = 0
    dp_i_1 = float("-inf")
    for i in range(len(prices)):
        tmp = dp_i_0
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, tmp - prices[i])
    return dp_i_0


