"""
题目：给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，
他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}，
{2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
"""


def maxInWindows(num, size):
    # write code here
    if len(num) < size or size <= 0:
        return []
    res = [max(num[:size])]
    for i in range(1, len(num) - size + 1):
        if num[i - 1] != res[i - 1]:
            res.append(max(res[i - 1], num[i + size - 1]))
        else:
            res.append(max(num[i:i + size]))
    return res


if __name__ == '__main__':
    print(maxInWindows([2,3,4,2,6,2,5,1],3))
