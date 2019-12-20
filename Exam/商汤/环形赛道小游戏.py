def get_sum(nums):
    n = len(nums)
    nums.extend(nums)
    dp = [nums[0]] * len(nums)
    for i in range(2 * n):
        dp[i] = max(dp[i]+nums[i], nums[i])

    return dp[-1]


n = int(input())
nums = list(map(int, input().split()))
print(get_sum(nums))
