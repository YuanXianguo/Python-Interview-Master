"""
A、B两伙马贼意外地在一片沙漠中发现了一处金矿，双方都想独占金矿，但各自的实力都不足以吞下对方，经过谈判后，双方同意用一个公平的方式来处理这片金矿。处理的规则如下：他们把整个金矿分成n段，由A、B开始轮流从最左端或最右端占据一段，直到分完为止。

马贼A想提前知道他们能分到多少金子，因此请你帮忙计算他们最后各自拥有多少金子?（两伙马贼均会采取对己方有利的策略）

输入
测试数据包含多组输入数据。输入数据的第一行为一个正整数T(T<=20)，表示测试数据的组数。然后是T组测试数据，每组测试数据的第一行包含一个整数n，下一行包含n个数（n <= 500 ），表示每段金矿的含金量，保证其数值大小不超过1000。

样例输入
2
6
4 7 2 9 5 2
10
140 649 340 982 105 86 56 610 340 879

输出
对于每一组测试数据，输出一行"Case #id: sc1 sc2"，表示第id组数据时马贼A分到金子数量为sc1，马贼B分到金子数量为sc2。详见样例。

样例输出
Case #1: 18 11

Case #2: 3206 981

"""

t = int(input())
id = 1
while id <= t:
    n = int(input())
    data = input().split()
    data = list(map(int, data))
    left, right = 0, n - 1
    sc1, sc2 = 0, 0
    while left < right:
        if data[left] > data[right]:
            sc1 += data[left]
            left += 1
        else:
            sc1 += data[right]
            right -= 1
        if data[left] > data[right]:
            sc2 += data[left]
            left += 1
        else:
            sc2 += data[right]
            right -= 1
    print("Case #{}:{} {}".format(id, sc1, sc2))
    id += 1
