"""题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数"""
m,n = eval(input("请输入两个数字(m<n),以逗号隔开："))
getList = []
for x in range(n):
    getList.append(x)
print(getList)

list = getList[-m:]
for i in range(1,n-m+1):
    j = -i
    getList[j] = getList[j-m]
for y in range(m):
    getList[y] = list[y]
print(getList)
