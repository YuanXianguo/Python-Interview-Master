"""
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。
"""


def findDisappearedNumbers(nums):
    """
    利用索引把数组自身当作字典处理；
    将数组中所有正数作为索引i，置nums[i]为负值，最后仍未正数的位置即为（未出现过）消失的数字；
    原始数组：[4,3,2,7,8,2,3,1]
    重置后为：[-4,-3,-2,-7,8,2,-3,-1]
    结论：[8,2]分别对应的index为[5,6]，即为消失的数字
    """
    for i in nums:
        nums[abs(i)-1] = - abs(nums[abs(i)-1])
    return [i+1 for i in range(len(nums)) if nums[i] > 0]


if __name__ == '__main__':
    print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
