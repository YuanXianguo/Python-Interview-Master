"""
有一个城市需要修建，给你N个民居的坐标X,Y，问把这么多民居全都包进城市的话，城市所需最小面积是多少（注意，城市为平行于坐标轴的正方形）


输入描述:
第一行为N，表示民居数目（2≤N≤1000）

输出描述:
城市所需最小面积

输入例子1:
2
0 0
2 2

输出例子1:
4

输入例子2:
2
0 0
0 3

输出例子2:
9
"""

n = int(input())
axis_li = list()
while n:
    tmp = input().split()
    tmp = list(map(int, tmp))
    axis_li.append(tmp)
    n -= 1

axis_li = list(zip(*axis_li))
bian = max(max(axis_li[0]) - min(axis_li[0]), max(axis_li[1]) - min(axis_li[1]))
print(bian ** 2)
