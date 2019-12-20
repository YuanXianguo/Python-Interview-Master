"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

"""


def rob(nums):
    """
    动态规划：当前收益=max(前一家收益，前前一家收益+当前家收益)
    动态转移方程：dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    基例：dp[0] = nums[0]，dp[1] = max(nums[0],nums[1])
    """
    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]
    dp0 = nums[0]
    dp1 = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp2 = max(dp1, dp0 + nums[i])
        dp1, dp0 = dp2, dp1
    return dp1


if __name__ == '__main__':
    print(rob([1,2,3,1]))
    print(rob([2,7,9,3,1]))
