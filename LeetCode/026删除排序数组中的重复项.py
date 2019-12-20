"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
"""


def removed(nums):
    if not nums:
        return 0
    index = 0  # 记录遍历索引
    tmp = 0  # 记录当前有效值索引
    while index < len(nums):
        if nums[index] != nums[tmp]:  # 如果当前索引对应值不等于当前有效值
            tmp += 1  # 更新有效值索引及有效值
            nums[tmp] = nums[index]
        index += 1
    return tmp + 1  # 返回有效值长度


class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0
        index = 0
        for i in nums:
            if i != nums[index]:
                index += 1
                nums[index] = i
        return index + 1


if __name__ == '__main__':
    nums =  [0,0,1,1,1,2,2,3,3,4]
    print(removed(nums))
    print(nums)

    nums =  [0,0,1]
    print(removed(nums))
    print(nums)
