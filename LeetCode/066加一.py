"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。
"""


def plusOne(digits):
    flag = 1  # 判断是否进位
    index = len(digits) - 1  # 从高到低加1
    while index >= 0:
        if flag:  # 如果上一位进位，当前位加1
            digits[index] += 1
            flag = 0  # 将进位标记置为假，如果当前位不进位，下次循环将结束
            if digits[index] == 10:  # 如果当前位加一等于10，需进位
                digits[index] = 0
                flag = 1  # 将进位标记置为真
            index -= 1  # 更新索引
        else:  # 如果进位标记为假，循环结束
            return digits
    if flag:  # 首位也需要进位，如99
        digits.insert(0, 1)
    return digits


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            if digits[i] >= 10:
                digits[i] %= 10
            else:
                break
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    print(plusOne([1,2,3]))
    print(plusOne([9,9]))
    print([0])
