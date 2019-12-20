"""
题目：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
例如
a b c e
s f c s
a d e e
矩阵中包含一条字符串"bcced"的路径，
但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""

"""
回溯法。任选一个格子作为路径的起点。假设矩阵中某个格子的字符为c并且这个格子将对应于路径上的第i个字符。
如果路径上的第i个字符不是c，那么这个格子不可能处在路径上的第i个位置。
如果路径上的第i个字符正好是c，那么往相邻的格子寻找路径上的第i+1个字符。
除在矩阵边界上的格子外，其他各自都有4个相邻的格子。
重复这个过程直到路径上的所有字符都在矩阵中找到相应的位置。
"""


class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if not matrix or not len(matrix) or rows <= 0 or cols <= 0 or not path:
            return
        length = 0
        visited = [0] * len(matrix)
        for row in range(rows):
            for col in range(cols):
                if self.get_path_main(matrix, rows, cols, row, col, path, length, visited):
                    return True
        return False

    def get_path_main(self, matrix, rows, cols, row, col, path, length, visited):
        if len(path) == length:
            return True
        has_path = False
        if 0 <= row < rows and 0 <= col < cols \
                and matrix[row * cols + col] == path[length] \
                and not visited[row * cols + col]:
            visited[row * cols + col] = 1
            length += 1
            has_path = self.get_path_main(matrix, rows, cols, row - 1, col, path, length, visited) \
                       or self.get_path_main(matrix, rows, cols, row, col + 1, path, length, visited) \
                       or self.get_path_main(matrix, rows, cols, row + 1, col, path, length, visited) \
                       or self.get_path_main(matrix, rows, cols, row, col - 1, path, length, visited)

            if not has_path:
                visited[row * cols + col] = 0
                length -= 1
        return has_path


class Solution2:
    def hasPath(self, matrix, rows, cols, path):
        self.matrix = matrix
        self.rows = rows
        self.cols = cols
        self.path = path
        self.index = 0
        self.visited = [0] * len(matrix)
        for row in range(rows):
            for col in range(cols):
                if self.find(row, col):
                    return True

    def find(self, row, col):
        if self.index == len(self.path):
            return True
        has_path = False
        if 0 <= row < self.rows and 0 <= col < self.cols and self.visited[row * self.cols + col] == 0 and self.matrix[row * self.cols + col] == self.path[self.index]:
            self.index += 1
            self.visited[row * self.cols + col] = 1
            has_path = self.find(row + 1, col) or self.find(row - 1, col) or self.find(row, col + 1) or self.find(row, col - 1)
            if not has_path:
                self.index -= 1
                self.visited[row * self.cols + col] = 0
        return has_path


if __name__ == '__main__':
    matrix = ["a", "b", "c", "e", "s", "f", "c", "s", "a", "d", "e", "e"]
    path = "bcced"
    s = Solution()
    print(s.hasPath(matrix, 3, 4, path))

    path = "abcb"
    print(s.hasPath(matrix, 3, 4, path))
