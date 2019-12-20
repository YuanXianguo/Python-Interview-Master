"""
题目：一个整型数组里除了两个数字之外，其他的数字都出现了两次。
请写程序找出这两个只出现一次的数字。
"""


def count(lst):
    d = {}
    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


def print_1(lst):
    d = count(lst)
    lst = []
    for key in d:
        if d[key] == 1:
            lst.append(key)
            if len(lst) == 2:
                break
    return lst


def print_2(lst):
    from collections import Counter
    count = Counter(lst)
    return list(map(lambda c: c[0], count.most_common()[-2:]))


if __name__ == '__main__':
    lst = list(range(10))
    for i in range(8):
        lst.append(i)
    print(print_1(lst))
    print(print_2(lst))
