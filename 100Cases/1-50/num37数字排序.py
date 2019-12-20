list = []
while True:
    num = input("输入一串数字，我将排序:")
    if num == ' ':
        break
    else:
        list.append(num)

list.sort()
print(list)
