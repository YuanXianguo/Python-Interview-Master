"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
"""


def moveZeroes(nums) -> None:
    index = 0
    zero = 0
    no_zero = 0
    while no_zero < len(nums) and zero < len(nums) and index < len(nums):
        if nums[zero] != 0:
            zero += 1
        elif nums[no_zero] == 0:
            no_zero += 1
        else:
            if no_zero > zero:
                nums[zero], nums[no_zero] = nums[no_zero], nums[zero]
            index += 1
            zero = index
            no_zero = index


def moveZeroes2(nums) -> None:
    index = 0
    no_zero = 0
    while no_zero < len(nums) and index < len(nums):
        while not nums[no_zero]:
            no_zero += 1
        if nums[index] == 0:
            nums[index] = nums[no_zero]
            no_zero += 1
        index += 1


class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in nums:
            if i != 0:
                nums[index] = i
                index += 1
        for i in range(index, len(nums)):
            nums[i] = 0


if __name__ == '__main__':
    nums = [0,1,0,3,12]
    moveZeroes2(nums)
    print(nums)
