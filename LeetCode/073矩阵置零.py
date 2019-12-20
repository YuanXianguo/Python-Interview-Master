"""
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
"""


def setZeroes(matrix):
    if not matrix or not matrix[0]:
        return []

    def set_row(row, matrix, tmp_d):
        """将某一行置为0"""
        for i in range(len(matrix[0])):
            if tmp_d.get((row, i)) == "rc":
                # 表示当前行已经置为0，不再考虑，但列还需要处理
                tmp_d[(row, i)] = "c"
            matrix[row][i] = 0

    def set_col(col, matrix, tmp_d):
        """将某一列置为0"""
        for i in range(len(matrix)):
            if tmp_d.get((i, col)) == "rc":
                # 表示当前列已经置为0，不再考虑，但行还需要处理
                tmp_d[(i, col)] = "r"
            matrix[i][col] = 0

    tmp_d = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                tmp_d[(i, j)] = "rc"

    while tmp_d:
        key, value = tmp_d.popitem()
        if value == "rc":
            set_row(key[0], matrix, tmp_d)
            set_col(key[1], matrix, tmp_d)
        elif value == "c":
            set_col(key[1], matrix, tmp_d)
        else:
            set_row(key[0], matrix, tmp_d)


if __name__ == '__main__':
    m = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
    setZeroes(m)
    print(m)
