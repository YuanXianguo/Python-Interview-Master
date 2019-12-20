"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
"""


def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []
    res = []
    # 定义矩形四个端点
    low_row, high_row = 0, len(matrix) - 1
    low_col, high_col = 0, len(matrix[0]) - 1
    # 在矩形未遍历区域还剩下大于2行2列时候持续循环
    while high_row > low_row and high_col > low_col:
        for i in range(low_col, high_col + 1):
            res.append(matrix[low_row][i])
        low_row += 1
        for i in range(low_row, high_row + 1):
            res.append(matrix[i][high_col])
        high_col -= 1
        for i in range(high_col, low_col - 1, -1):
            res.append(matrix[high_row][i])
        high_row -= 1
        for i in range(high_row, low_row - 1, -1):
            res.append(matrix[i][low_col])
        low_col += 1
    # 只剩下一行或一列，直接添加到结果集中
    if high_row == low_row or high_col == low_col:
        for i in range(low_row, high_row + 1):
            for j in range(low_col, high_col + 1):
                res.append(matrix[i][j])
    return res


class Solution:
    def spiralOrder(self, matrix):
        res = list()
        while matrix:
            res += matrix.pop(0)
            matrix = list(map(list, zip(*matrix)))[::-1]
        return res


if __name__ == '__main__':
    print(spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))
    print(spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]))
