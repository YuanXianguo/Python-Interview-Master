"""
题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""


def change_turn(array):
    tmp = []
    cnt = 0
    for i in array:
        if i % 2 == 1:
            tmp.insert(cnt, i)
            cnt += 1
        else:
            tmp.append(i)
    return tmp


def reOrderArray(array):
    tmp = []
    index = 0
    for i in range(len(array)):
        if array[i] % 2 == 0:
            tmp.append(array[i])
        else:
            array[index] = array[i]
            index += 1
    for i in range(index, len(array)):
        array[i] = tmp[i - index]
    return array


if __name__ == '__main__':
    print(change_turn([2,4,6,1,3,5,7]))
