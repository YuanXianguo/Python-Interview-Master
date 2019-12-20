"""
节日到啦，牛牛和妞妞邀请了好多客人来家里做客。
他们摆出了一座高高的香槟塔，牛牛负责听妞妞指挥，往香槟塔里倒香槟。
香槟塔有个很优雅的视觉效果就是如果这一层的香槟满了，就会从边缘处往下一层流去。
妞妞会发出两种指令，指令一是往第x层塔内倒体积为v的香槟，指令二是询问第k层塔香槟的体积为多少。
告诉你香槟塔每层香槟塔的初始容量，你能帮牛牛快速回答妞妞的询问吗？

输入描述:
第一行为两个整数n，m。表示香槟塔的总层数和指令条数。
第二行为n个整数ai，表示每层香槟塔的初始容量。
第三行到第2+m行有两种输入，一种输入是“2 x v”表示往第x层倒入体积为v的香槟；另一种输入是“1 k”表示询问第k层当前有多少香槟。
1 <= n, m <= 1000。
1 <= n ,m <= 200000，1 <= ai ,v <= 1000000000。

输出描述:
对于每个询问，输出一个整数，表示第k层香槟的容量。
"""


def main(nums, res, order):
    if order[0] == 1:
        print(res[order[1]])
    else:
        index = order[1]
        while index < len(nums):
            if res[index] < nums[index]:
                if res[index] + order[2] <= nums[index]:
                    res[index] += order[2]
                    break
                else:
                    res[index] = nums[index]
                    order[2] -= res[index]
            index += 1


nm = input().split()
n, m = int(nm[0]), int(nm[1])
nums = list(map(int, input().split()))
res = [0] * len(nums)

while m:
    order = list(map(int, input().split()))
    order[1] = order[1] - 1
    main(nums, res, order)
    m -= 1
