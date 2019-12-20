nums = list(map(int, input().split(",")))
tmp = dict()
cnt = 0
for i in nums:
    if i not in tmp:
        cnt += 1
        tmp[i] = 1
print(cnt)
