"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
"""


def max_sub_array(nums):
    if max(nums) <= 0:  # 如果数组全为非正数，直接返回最大值
        return max(nums)
    sum_max = 0  # 存储最大值
    tmp = 0  # 存储当前和
    for i in nums:
        tmp += i
        if tmp > sum_max:  # 如果当前和大于最大值，更新最大值
            sum_max = tmp
        elif tmp < 0:  # 如果当前和小于0，重置当前和为0
            tmp = 0
    return sum_max


def max_sub2(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    tmp = [0] * len(nums)
    for i in range(len(nums)):
        tmp[i] = max(tmp[i-1] + nums[i], nums[i])
    return max(tmp)


class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return
        n = len(nums)
        dp = [nums[0] for _ in range(n)]
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)


if __name__ == '__main__':
    print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))
    print(max_sub2([-2,1,-3,4,-1,2,1,-5,4]))
