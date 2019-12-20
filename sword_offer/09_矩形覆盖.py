"""
题目：我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""
"""
依旧是斐波那契数列
2*n的大矩形，和n个2*1的小矩形
其中 2*target 为大矩阵的大小
有以下几种情形：
1⃣️target <= 0 大矩形为<= 2*0,直接return 1；
2⃣️target = 1大矩形为2*1，只有一种摆放方法，return1；
3⃣️target = 2 大矩形为2*2，有两种摆放方法，return2；
4⃣️target = n 分为两步考虑：
第一次摆放一块 2*1 的小矩阵，则摆放方法总共为f(target - 1)
√
√
第一次摆放一块1*2的小矩阵，则摆放方法总共为f(target-2)
因为，摆放了一块1*2的小矩阵（用√√表示），
对应下方的1*2（用××表示）摆放方法就确定了，所以为f(target-2)
√	√
×	×
target >= 3  f(n) = f(target - 1) + f(target-2)
"""


def rect_cover(n):
    res = [0, 1, 2]
    while len(res) <= n:
        res.append(res[-1] + res[-2])
    return res[n]


if __name__ == '__main__':
    for i in range(10):
        print(rect_cover(i), end=" ")
