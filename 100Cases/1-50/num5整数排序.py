list = []
for i in range(3):
    n = eval(input("请输入3个整数，以空格分开："))
    list.append(n)
list.sort()
for i in list:
    print(i,end=' ')
