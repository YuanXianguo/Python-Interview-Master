"""
题目：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323
"""


def bubble_sort(array):
    if not array or not len(array):
        return ""
    array = list(map(str, array))
    print(array)
    for i in range(len(array)-1, 0, -1):
        flag = 1
        for j in range(i):
            # 如果字符串n+m>m+n，则认为n更大
            if array[j] + array[j+1] > array[j+1] + array[j]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = 0
        if flag:
            break
    return eval("".join(array))


if __name__ == '__main__':
    print(bubble_sort([3, 32, 321]))
    print(bubble_sort([32, 34, 35, 352, 343]))
