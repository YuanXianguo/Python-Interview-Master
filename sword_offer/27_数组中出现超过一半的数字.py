"""
题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，
超过数组长度的一半，因此输出2。如果不存在则输出0。
"""


def count(array):
    d = {}
    for i in array:
        if i in d:
            d[i] += 1
            print(d)
            if d[i] > len(array) // 2:
                return i
        else:
            d[i] = 1


if __name__ == '__main__':
    array = [1,2,3,2,2,2,5,4,2]
    print(count(array))
