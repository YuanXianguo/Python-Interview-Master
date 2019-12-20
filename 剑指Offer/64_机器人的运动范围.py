"""
题目：地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，
每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
"""

class Solution:
    def movingCount(self, threshold, rows, cols):
        if not threshold or not rows or not cols:
            return 0
        self.visited = set()
        return self.move_main(threshold, rows, cols, 0, 0)

    def move_main(self, threshold, rows, cols, row, col):
        cnt = 0
        if 0 <= row < rows and 0 <= col < cols \
                and self.get_sum(row) + self.get_sum(col) <= threshold \
                and (row, col) not in self.visited:
            self.visited.add((row, col))
            cnt = 1 + self.move_main(threshold, rows, cols, row - 1, col) \
                  + self.move_main(threshold, rows, cols, row, col + 1) \
                  + self.move_main(threshold, rows, cols, row + 1, col) \
                  + self.move_main(threshold, rows, cols, row, col - 1)
        return cnt

    def get_sum(self, num):
        res = 0
        while num:
            res += num % 10
            num //= 10
        return res


class Solution2:
    def movingCount(self, threshold, rows, cols):
        self.visited = set()
        self.th = threshold
        self.rows = rows
        self.cols = cols
        self.cnt = 0
        self.main(0, 0)
        return self.cnt

    def main(self, row, col):
        if (row, col) not in self.visited and 0 <= row < self.rows and 0 <= col < self.cols and self.get_d(row) + self.get_d(col) <= self.th:
            self.visited.add((row, col))
            self.cnt += 1
            self.main(row + 1, col)
            self.main(row - 1, col)
            self.main(row, col + 1)
            self.main(row, col - 1)

    def get_d(self, d):
        c = 0
        while d:
            c += d % 10
            d //= 10
        return c


if __name__ == '__main__':
    s = Solution2()
    print(s.movingCount(5, 10, 10))
