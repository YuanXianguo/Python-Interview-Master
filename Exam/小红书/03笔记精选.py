n = int(input())
data = list(map(int, input().split()))
dp = [0] * n
dp[0] = data[0]
dp[1] = max(dp[0], data[1])
for i in range(n-2):
    dp[i+2] = max(dp[i] + data[i+2], dp[i+1])

path = list()
for i in range(1, n):
    if dp[i] != dp[i-1]:
        if dp[i-1] + data[i] == dp[i]:
            try:
                if path[-1] == i-1:
                    path.pop()
            except:
                pass
            path.append(i)
cnt = len(path)
if sum(path) != dp[-1]:
    cnt += 1
print(dp[-1], cnt)
print(dp, path)


