"""
一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。
"""


def isHappy(n):
    d = {n}  # 创建一个集合用于存储计算的结果，
    while n != 1:
        tmp = 0
        for i in str(n):
            tmp += int(i) ** 2
        if tmp in d:  # 如果重复出现某个结果，则进入循环，返回False
            return False
        d.add(tmp)
        n = tmp
    return True


if __name__ == '__main__':
    print(isHappy(19))
    print(isHappy(7))
