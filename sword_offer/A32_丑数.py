"""
题目：把只包含因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含因子7。 习惯上我们把1当做是第一个丑数。
求按从小到大的顺序的第N个丑数
"""


def ugly(index):
    # write code here
    if not index:
        return 0
    tmp = [1]
    u2 = u3 = u5 = 0
    while len(tmp) < index:
        # 选出三个队列头最小的数
        min_head = min(tmp[u2] * 2, tmp[u3] * 3, tmp[u5] * 5)
        tmp.append(min_head)
        # 这三个if有可能进入一个或者多个，进入多个是三个队列头最小的数有多个的情况
        if min_head == tmp[u2] * 2:
            u2 += 1
        if min_head == tmp[u3] * 3:
            u3 += 1
        if min_head == tmp[u5] * 5:
            u5 += 1
        print(tmp, u2, u3, u5)
    return tmp[-1]


def ugly2(index):
    if not index:
        return 0
    u2, u3, u5 = 0, 0, 0
    stack = [1]
    while len(stack) < index:
        min_head = min(stack[u2] * 2, stack[u3] * 3, stack[u5] * 5)
        stack.append(min_head)
        if min_head == stack[u2] * 2:
            u2 += 1
        if min_head == stack[u3] * 3:
            u3 += 1
        if min_head == stack[u5] * 5:
            u5 += 1
    return stack[-1]


print(ugly2(20))
