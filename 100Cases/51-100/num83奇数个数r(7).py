"""题目：求0—7所能组成的奇数个数。"""
count = 0
number = 0

for i in range(8):
    if i % 2 != 0:
        count += 1
# 一位数
num = count
# 最高位不为0
for j in range(7):
    number += pow(8,j)
num += number * count * 7
print(num)
