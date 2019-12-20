"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。
"""


def climbStairs(n):
    def climb_main(n, visited):
        if n in visited:
            return visited[n]
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            tmp = climb_main(n - 1, visited) + climb_main(n - 2, visited)
            visited[n] = tmp
            return tmp
    return climb_main(n, {})


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        dp0 = 1
        dp1 = 2
        for i in range(2, n):
            dp1, dp0 = dp1 + dp0, dp1
        return dp1


if __name__ == '__main__':
    print(climbStairs(35))
