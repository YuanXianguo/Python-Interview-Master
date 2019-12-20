"""
题目：输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
"""


def find_s(array, s):
    if not array or not len(array) or array[-1] + array[-2] < s:
        return []
    left = 0
    right = len(array) - 1
    while left <= right:
        if array[left] + array[right] < s:
            left += 1
        elif array[left] + array[right] > s:
            right -= 1
        else:  # 此方法找到的第一组等于s的两个数字，其乘积也是最小的
            return [array[left], array[right]]
    return []


if __name__ == '__main__':
    print(find_s(list(range(10)), 11))
