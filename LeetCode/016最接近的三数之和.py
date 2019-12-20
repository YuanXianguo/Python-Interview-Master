"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

"""


class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = float("inf")
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            # dif = float("inf")
            while j < k:
                cur = nums[i] + nums[j] + nums[k]
                if abs(cur - target) < abs(res - target):
                    res = cur
                # tmp = abs(cur - target)
                # if tmp <= dif:
                #     dif = tmp
                # else:
                #     break
                if cur < target:
                    j += 1
                elif cur > target:
                    k -= 1
                else:
                    return target
        return res
