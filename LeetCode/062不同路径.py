"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？
"""
matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],
print(list(map(list, zip(*matrix))))


def uniquePaths(m, n):

    def get_path(row, col, visited):
        if (row, col) in visited:  # 如果从当前位置有多少条路径已经计算过了，直接返回
            return visited[(row, col)]
        if row > m - 1 or col > n - 1:  # 当前位置超出最大行或列，无解
            return 0
        elif row == m - 1 or col == n - 1:  # 当前位于最大行或最大列，只有一条
            return 1
        else:  # 递归向下进一步或向右进一步
            # 将从当前位置有多少路径添加到字典中
            res = get_path(row + 1, col, visited) + get_path(row, col + 1, visited)
            visited[(row, col)] = res
            return res

    return get_path(0, 0, {})


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]


if __name__ == '__main__':
    print(uniquePaths(7, 3))
    print(uniquePaths(23, 13))
