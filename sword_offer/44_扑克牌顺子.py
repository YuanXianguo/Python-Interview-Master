"""
随机从扑克牌中抽出了5张牌,判断是不是顺子,
决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
"""


def is_lucky(numbers):
    if not numbers:
        return False

    # 统计王的个数，并将王从列表中去掉
    cnt0 = numbers.count(0)
    for i in range(cnt0):
        numbers.remove(0)

    # 集合去重，如果有0以外的重复数字，直接返回False
    if len(set(numbers)) != len(numbers):
        return False

    # 将A、J、Q、K转化
    d = {"A": 1, "J": 11, "Q": 12, "K": 13}
    for i in range(len(numbers)):
        if numbers[i] in d:
            numbers[i] = d[numbers[i]]

    # 将剩余数字排序，并逐个比较间隔，相邻间隔记为0
    numbers.sort()
    cnt = 0
    for i in range(len(numbers) - 1):
        cnt += numbers[i+1] - numbers[i] - 1

    # 如果间隔小于王数量，可以用王补充间隔，否则返回False
    if cnt0 >= cnt:
        return True
    return False


if __name__ == '__main__':
    print(is_lucky([1,3,5,0,0]))
    print(is_lucky(['A', 3, 2, 5, 0]))
