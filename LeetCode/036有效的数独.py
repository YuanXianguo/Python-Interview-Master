"""
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
数独部分空格内已填入了数字，空白格用 '.' 表示。
"""


class Solution:
    def isValidSudoku(self, board):
        # 判断行
        for row in board:
            if row.count(".") + len(set(row)) - 1 != 9:
                return False
        # 判断列
        for col in zip(*board):
            if col.count(".") + len(set(col)) - 1 != 9:
                return False
        # 判断9宫格
        visited = {}  # 一个子数独只访问一次
        return self.is_valid(0, 0, board, visited)

    def is_valid(self, row, col, board, visited):
        # 该子数独访问过直接返回，否则更新访问字典
        if visited.get((row, col)):
            return True
        visited[(row, col)] = 1
        tmp = []
        if col + 3 <= 9 and row + 3 <= 9:
            for i in range(row, row+3):
                for j in range(col, col+3):
                    if board[i][j] not in tmp and board[i][j] != ".":
                        tmp.append(board[i][j])
                    elif board[i][j] in tmp:
                        return False
            # 回溯法递归判断周围子数独
            return self.is_valid(row, col + 3, board, visited) and self.is_valid(row + 3, col, board, visited)
        return True


def isValid(board):
    """
    子数独划分图
    0, 1, 2,
    3, 4, 5,
    6, 7, 8
    """
    rows = []  # 统计行元素
    cols = []  # 统计列元素
    box = []  # 统计子数独元素
    for i in range(9):
        rows.append({})
        cols.append({})
        box.append({})
    # 通过一次遍历统计行、列和子数独元素
    for row in range(9):
        for col in range(9):
            cur = board[row][col]
            if cur != ".":  # 不统计"."的个数
                box_index = row // 3 * 3 + col // 3  # 子数独索引
                # 如果某个字典内有1-9的数字与当前数字重复，直接返回false,否则就将当前数字分别添加到三个字典中
                if rows[row].get(cur) or cols[col].get(cur) or box[box_index].get(cur):
                    return False
                else:
                    rows[row][cur] = 1
                    cols[col][cur] = 1
                    box[box_index][cur] = 1
    return True


if __name__ == '__main__':
    b = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    s = Solution()
    print(s.isValidSudoku(b))

    print(isValid(b))
