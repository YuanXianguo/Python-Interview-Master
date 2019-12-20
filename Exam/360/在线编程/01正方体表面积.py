n, m = list(map(int, input().split()))

cnt = n * m * 2  # 上下面

data = list()

while n:
    row = list(map(int, input().split()))
    data.append(row)

    cnt += row[0]  # 每行端面
    cnt += row[-1]

    for i in range(1, len(row)):
        cnt += abs(row[i]-row[i-1])  # 每行内部
    n -= 1

new_data = list(zip(*data))  # 转置列表

for col in new_data:
    cnt += col[0]  # 每列端面
    cnt += col[-1]

    for i in range(1, len(col)):
        cnt += abs(col[i]-col[i-1])  # 每列内部

print(cnt)
