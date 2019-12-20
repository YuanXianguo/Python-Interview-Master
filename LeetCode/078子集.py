"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
"""


def subsets(nums):
    if not nums:
        return [[]]
    if len(nums) == 1:
        return [nums, []]
    res = [[]]
    for i in range(len(nums)):
        tmp = subsets(nums[i+1:])
        for j in tmp:
            j.insert(0, nums[i])
            res.append(j)

    return res


if __name__ == '__main__':
    print(subsets([1, 2, 3]))
