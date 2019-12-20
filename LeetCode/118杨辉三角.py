"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。
"""


def generate(numRows: int):
    if not numRows:
        return []
    # 初始化为[[1][11][101][1001]]
    dp = [[1]] + [([1] + [0 for _ in range(row)] + [1]) for row in range(numRows-1)]
    for i in range(2, numRows):  # 从第三行开始循环
        for j in range(1, i):  # 跳过每行第一个和最后一个数字
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]  # 每个数字等于上一行前一列数字加当前列数字
    return dp


class Solution:
    def generate(self, numRows: int):
        res = [[1], [1,1]]
        if numRows <= 2:
            return res[:numRows]
        while len(res) < numRows:
            tmp = [1]
            for i in range(len(res[-1])-1):
                tmp.append(res[-1][i] + res[-1][i+1])
            tmp.append(1)
            res.append(tmp)
        return res

if __name__ == '__main__':
    print(generate(5))
