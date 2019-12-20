"""
题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数
"""


def is_in(lst, n):
    """迭代查找，时间复杂度O(n^2)"""
    for row in lst:
        for column in row:
            if n == column:
                return True
    return False


def is_in_better(lst, n):
    """从右上或坐下开始查找，比如从右上：
    如果目标数大于右上，向下移动一位，
    如果目标数小于右上，向左移动一位"""
    rows = len(lst)
    cols = len(lst[0])
    row = 0
    col = cols - 1
    while row < rows and col >= 0:
        if n < lst[row][col]:
            col -= 1
        elif n > lst[row][col]:
            row += 1
        else:
            return True
    return False


if __name__ == '__main__':
    array = []
    for i in range(8):
        array.append(list(range(8)))

    for i in range(10):
        print(is_in(array, i), end=" ")
    print("")

    for i in range(10):
        print(is_in_better(array, i), end=" ")

