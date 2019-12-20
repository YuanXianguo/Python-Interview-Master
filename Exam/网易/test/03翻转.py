"""
给定一个N*M的矩阵，在矩阵中每一块有一张牌，我们假定刚开始的时候所有牌的牌面向上。
现在对于每个块进行如下操作：
> 翻转某个块中的牌，并且与之相邻的其余八张牌也会被翻转。
XXX
XXX
XXX
如上矩阵所示，翻转中间那块时，这九块中的牌都会被翻转一次。
请输出在对矩阵中每一块进行如上操作以后，牌面向下的块的个数。

输入描述:
输入的第一行为测试用例数t(1 <= t <= 100000),
接下来t行，每行包含两个整数N,M(1 <= N, M <= 1,000,000,000)
"""


def main(num):
    n, m = num[0], num[1]
    if n == 1 and m == 1:
        return 1
    if n == 1:
        return m - 2
    if m == 1:
        return n - 2
    return (n - 2) * (m - 2)


t = int(input())
while t:
    print(main(list(map(int, input().split()))))
    t -= 1
