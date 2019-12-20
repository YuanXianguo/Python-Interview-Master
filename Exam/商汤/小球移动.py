def get_path(n, m):
    dp = [1] * m
    for j in range(1, n):
        for i in range(1, m):
            dp[i] += dp[i-1]
    return dp[-1]


nm = list(map(int, input().split()))
print(get_path(nm[0], nm[1]))
