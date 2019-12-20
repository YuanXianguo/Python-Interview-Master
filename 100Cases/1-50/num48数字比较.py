i,j = eval(input("输入两个数字，比较大小，以逗号隔开："))
if i < j:
    res = '小于'
elif i == j:
    res = '等于'
else:
    res = '大于'
print("{}{}{}".format(i,res,j))
