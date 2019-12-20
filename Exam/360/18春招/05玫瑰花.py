"""
有K种不同的玫瑰花，现在要摆放在N个位置上，要求每种颜色的花至少出现过一次，请问有多少种不同的方案数呢？，因为答案可能很大，你只需要输出它对772235取余后的结果.


输入描述:
输入只有1行，分别有两个整数N,K( 1 <= N <= 50000 , 1 <= K <= 30 )

输出描述:
输出一行表示答案

输入例子1:
3 2

输出例子1:
6
"""

datas = input().split()
n, k = int(datas[0]), int(datas[1])
dp = [[0] * (k+1) for i in range(n+1)]
dp[0][0] = 1
mod = 772235
for i in range(1, n+1):
    for j in range(1, k+1):
        dp[i][j] = (j * dp[i-1][j] % mod + (k-j+1) * dp[i-1][j-1] % mod) % mod
print(dp[n][k])


