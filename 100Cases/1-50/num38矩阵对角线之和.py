"""题目：求一个3*3矩阵主对角线元素之和"""
"""row1,row2,row3 = [],[],[]
sum = 0
for i in range(3):
    m = eval(input("输入矩阵第一行："))
    row1.append(m)
for i in range(3):
    m = eval(input("输入矩阵第二行："))
    row2.append(m)
for i in range(3):
    m = eval(input("输入矩阵第三行："))
    row3.append(m)
sum = row1[0] + row2[1] + row3[2]
print(sum)"""

list = []
sum = 0
for i in range(3):
    list.append([])
    for j in range(3):
        list[i].append(eval(input()))
for i in range(3):
    print(list[i][i])
    sum += list[i][i]
print(sum)
