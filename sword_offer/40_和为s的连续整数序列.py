"""
题目：有一天小明在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
"""


def FindContinuousSequence(tsum):
    # 根据等差数列的求和公式：S = (1 + n) * n / 2，得到n < 2S平方根
    if tsum < 3:
        return []
    n = int(pow(tsum * 2, 0.5))  # 可能的最大项数
    res = []
    for i in range(2, n + 1):
        left = tsum // i - i // 2
        right = tsum // i + i // 2
        print(left, right)
        if i % 2 == 0:
            left += 1
        tmp = []
        for j in range(left, right + 1):
            tmp.append(j)
        if sum(tmp) == tsum:
            res.append(tmp)

    return sorted(res, key=lambda x: x[0])


print(FindContinuousSequence(9))
