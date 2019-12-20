num, n = eval(input("输入数字和次数，以逗号分隔："))
count = 0
for i in range(1,n+1):
    res = int(str(num)*i)
    count += res
    print("{:>4}".format(res))
print(count)
