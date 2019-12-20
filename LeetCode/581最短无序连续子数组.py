"""
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。
"""


def findUnsortedSubarray(nums) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        if nums[left] > min(nums[left:]):
            break
        left += 1
    while right >= left:
        if nums[right] < max(nums[left:right]):
            break
        right -= 1
    return right - left + 1


def findUnsortedSubarray2(nums):
    left, right = -1, -1

    # 找出局部最大值
    dp_max = [0] * len(nums)
    dp_max[0] = nums[0]
    for i in range(1, len(nums)):
        dp_max[i] = max(dp_max[i-1], nums[i])

    # 逆序找出局部最小值
    dp_min = [0] * len(nums)
    dp_min[-1] = nums[-1]
    for i in range(len(nums)-2, -1, -1):
        dp_min[i] = min(dp_min[i+1], nums[i])

    # 将局部最小值与数组对比，找出第一个不同的即为left
    for i in range(len(nums)):
        if nums[i] != dp_min[i]:
            left = i
            break

    # 逆序将局部最大值与数组对比，找出第一个不同的即为right
    for i in range(len(nums)-1, -1, -1):
        if nums[i] != dp_max[i]:
            right = i
            break
    if right == -1:  # 如果为有序数组
        return 0
    return right - left + 1


class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        if not nums:
            return 0
        n = len(nums)
        # 正序遍历，根据局部最大值，更新最右端索引
        max_ = nums[0]
        right = 0
        for i in range(n):
            if nums[i] > max_:
                max_ = nums[i]
            elif nums[i] < max_:
                right = i

        # 逆序遍历，根据局部最小值，更新最左端索引
        min_ = nums[-1]
        left = n - 1
        for i in range(n - 1, -1, -1):
            if nums[i] < min_:
                min_ = nums[i]
            elif nums[i] > min_:
                left = i

        if left >= right:
            return 0
        return right - left + 1


if __name__ == '__main__':
    s = Solution()
    print(s.findUnsortedSubarray([2,1]))
    print(findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
    print(findUnsortedSubarray2([2, 6, 4, 8, 10, 9, 15]))
    print(findUnsortedSubarray2([1,2,3,4]))

