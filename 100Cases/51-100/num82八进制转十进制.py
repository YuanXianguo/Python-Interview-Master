num = input("输入八进制数：")
count = len(num)
res_num = 0
for i in num:
    count -= 1
    res_num += int(i) * pow(8,count)
print("转换为十进制是：{}".format(res_num))
