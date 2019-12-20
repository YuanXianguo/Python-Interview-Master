"""
题目：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵：
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""


def print_clock(array):
    if not len(array):
        return
    row_l = 0  # 行索引最小值
    row_h = len(array) - 1  # 行索引最大值
    column_l = 0  # 列索引最小值
    column_h = len(array[0]) - 1  # 列索引最大值
    if column_l == column_h or row_l == row_h:  # 只有一列或1行，直接遍历输出
        for row in array[row_l:row_h+1, column_l:column_h+1]:
            for i in row:
                print(i, end=" ")
        return
    for i in range(column_l, column_h+1):
        print(array[row_l][i], end=" ")
    row_l += 1
    for i in range(row_l, row_h+1):
        print(array[i][column_h], end=" ")
    column_h -= 1
    for i in range(column_h, column_l-1, -1):
        print(array[row_h][i], end=" ")
    row_h -= 1
    for i in range(row_h, row_l-1, -1):
        print(array[i][column_l], end=" ")
    column_l += 1
    # 将未遍历的数组切片继续递归
    print_clock(array[row_l:row_h+1, column_l:column_h+1])


def printMatrix(self, matrix):
    # write code here
    res = []
    if not matrix or not matrix[0]:
        return res
    low_row = 0
    high_row = len(matrix) - 1
    low_col = 0
    high_col = len(matrix[0]) - 1
    while high_row > low_row and high_col > low_col:
        print(low_row, high_row, low_col, high_col)

        for col in range(low_col, high_col+1):
            res.append(matrix[low_row][col])
        low_row += 1
        for row in range(low_row, high_row+1):
            res.append(matrix[row][high_col])
        high_col -= 1
        for col in range(high_col, low_col-1, -1):
            res.append(matrix[high_row][col])
        high_row -= 1
        for row in range(high_row, low_row-1, -1):
            res.append(matrix[row][low_col])
        low_col += 1
    if high_row == low_row or high_col == low_col:
        for row in matrix[low_row:high_row+1]:
            for col in row[low_col:high_col+1]:
                res.append(col)
    return res

def printMatrix2(matrix):
    # write code here
    if not matrix or not matrix[0]:
        return []
    res = []
    row_low, row_high = 0, len(matrix) - 1
    col_low, col_high = 0, len(matrix[0]) - 1
    while row_high > row_low and col_high > col_low:
        for col in range(col_low, col_high + 1):
            res.append(matrix[row_low][col])
        row_low += 1
        for row in range(row_low, row_high + 1):
            res.append(matrix[row][col_high])
        col_high -= 1
        for col in range(col_high, col_low - 1, -1):
            res.append(matrix[row_high][col])
        row_high -= 1
        for row in range(row_high, row_low - 1, -1):
            res.append(matrix[row][col_low])
        col_low += 1
    if row_high == row_low or col_high == col_low:
        for row in range(row_low, row_high + 1):
            for col in range(col_low, col_high + 1):
                res.append(matrix[row][col])
    return res


if __name__ == '__main__':
    import numpy as np
    array = np.array(np.arange(12)).reshape((3, 4))
    print(array)
    print_clock(array)
    print("")

    array = np.array(np.arange(16)).reshape((4, 4))
    print(array)
    print_clock(array)
    print("")

    array = np.array(np.arange(4)).reshape((1, 4))
    print(array)
    print_clock(array)
    print("")

    array = np.array(np.arange(4)).reshape((4, 1))
    print(array)
    print_clock(array)
    print("")

    array = []
    print(array)
    print_clock(array)
    print("")


    l = [[1]]
    print(printMatrix2(l))


