"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。
"""


def searchRange(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            while nums[left] != target:
                left += 1
            while nums[right] != target:
                right -= 1
            return [left, right]
    return [-1, -1]


class Solution:
    def searchRange(self, nums, target):
        left = self.search_point(nums, target, True)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = self.search_point(nums, target, False)
        return [left, right-1]

    def search_point(self, nums, target, flag):
        """flag标记，中间值等于目标值时是否向左区间搜索"""
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target or (nums[mid] == target and flag):
                right = mid
            else:
                left = mid + 1
        return left


class Solution2:
    def searchRange(self, nums, target: int):
        n = len(nums)
        if not n:
            return [-1, -1]
        left = self.search_left(nums, target)
        if left == -1:
            return [-1, -1]
        right = self.search_right(nums, target)
        return [left, right]

    def search_left(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] != target:
            return -1
        return left

    def search_right(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right + 1) >> 1
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        if nums[left] != target:
            return -1
        return left

if __name__ == '__main__':
    print(searchRange([5,7,7,8,8,10], 8))
    print(searchRange([5,7,7,8,8,10], 6))
    print(searchRange([1],1))
