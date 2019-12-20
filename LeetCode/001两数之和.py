"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
"""
def twoSum(nums, target):
    left = 0
    right = len(nums) - 1
    # 新建一个临时排序列表，创建左右两个指针：小于目标，左指针加1，大于目标，右指针减1
    tmp_lst = sorted(nums)
    while left < right:
        if tmp_lst[left] + tmp_lst[right] < target:
            left += 1
        elif tmp_lst[left] + tmp_lst[right] > target:
            right -= 1
        else:  # 此时left,right分别对应两个值在临时数组的索引
            res_left = nums.index(tmp_lst[left])
            # 如果两个值相等，求第二个值索引要从第一个索引后一位开始
            if tmp_lst[left] == tmp_lst[right]:
                return [res_left, nums.index(tmp_lst[right], res_left+1)]
            else:
                return [res_left, nums.index(tmp_lst[right])]


def twoSum2(nums, target):
    # 判断是否出现两个相等的值为所求
    if target % 2 == 0 and nums.count(target // 2) == 2:
        index1 = nums.index(target // 2)
        index2 = nums.index(target // 2, index1+1)
        return [index1, index2]
    else:
        res_dict = {}
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in res_dict:
                return [i, res_dict[tmp]]
            res_dict[nums[i]] = i


if __name__ == '__main__':
    print(twoSum([3, 3], 6))
    print(twoSum([2, 3, 5, 1, 0], 4))
    print(twoSum2([3, 3], 6))
    print(twoSum2([2, 3, 5, 1, 0], 4))

