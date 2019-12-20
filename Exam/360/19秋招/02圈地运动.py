"""
圈地运动，就是用很多木棍摆在地上组成一个面积大于0的多边形～

小明喜欢圈地运动，于是他需要去小红店里面买一些木棍，期望圈出一块地来。小红想挑战一下小明，所以给小明设置了一些障碍。障碍分别是：

1.如果小明要买第i块木棍的话，他就必须把前i-1块木棍都买下来。

2.买了的木棍都必须用在圈地运动中。

那么请问小明最少买多少根木棍，才能使得木棍围成的图形是个面积大于0多边形呢？

输入描述:
第一行一个数n，表示木棍个数。
第二行n个数，第i个数表示第i个木棍的长度ai
1<=n<=10000
1<=ai<=10000

输出描述:
输出一个数，表示最少需要的木棍个数，如果无解输出-1

输入例子1:
4
6 8 2 2

输出例子1:
3

例子说明1:
用三根6，8，10的木棍可以组成一个直角三角形的图形。
"""

n = int(input())
if n < 3:
    print(-1)
else:
    data = input().split()
    data = list(map(int, data))
    i = 3
    max_ = max(data[:i])
    sum_ = sum(data[:i]) - max_
    while i < n and max_ >= sum_:
        sum_ = sum_ + min(data[i], max_)
        max_ = max(data[i], max_)
        # if data[i] > max_:
        #     sum_ += max_
        #     max_ = data[i]
        # else:
        #     sum_ += data[i]
        i += 1
    if max_ >= sum_:
        print(-1)
    else:
        print(i)
