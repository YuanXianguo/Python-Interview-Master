"""
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
"""


def missingNumber(nums):
    n = len(nums)
    if n not in nums:
        return n
    for i in nums:
        if abs(i) == n:
            continue
        nums[abs(i)] = - nums[abs(i)]
    for i, v in enumerate(nums):
        if v > 0:
            return i
    return nums.index(0)


if __name__ == '__main__':
    print(missingNumber([2,0]))
    print(missingNumber([8,6,4,2,3,5,7,0,1]))
