def majorityElement(nums) -> int:
    nums.sort()
    return nums[(len(nums)//2)]


class Solution:
    def majorityElement(self, nums) -> int:
        tmp = dict()
        for i in nums:
            tmp[i] = tmp.get(i, 0) + 1
        for i, v in tmp.items():
            if v > len(nums) / 2:
                return i
