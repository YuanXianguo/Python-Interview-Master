"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
"""


def rotate(nums, k):
    while k:
        tmp = nums.pop()
        nums.insert(0, tmp)
        k -= 1


if __name__ == '__main__':
    nums = [i for i in range(1, 8)]
    k = 3
    rotate(nums, k)
    print(nums)
