"""
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
"""


def containsDuplicate(nums):
    for i in nums:
        if nums.count(i) > 1:
            return False
    return True


def con2(nums):
    d = set()
    for i in nums:
        if i in d:
            return True
        d.add(i)
    return False


if __name__ == '__main__':
    print(containsDuplicate([1,2,3,1]))
    print(containsDuplicate([1,2,3,4]))
    print(con2([1,2,3,1]))
    print(con2([1,2,3,4]))
