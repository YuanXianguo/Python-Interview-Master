char = input("随即输入一段字符，统计类别数量：")
a = 0
b = 0
c = 0
d = 0
for i in char:
    if i == ' ':
        a += 1
    elif i.isdigit():
        b += 1
    elif i.isalpha():
        c +=1
    d = len(char) - a - b - c
print("空格：{}，数字：{}，字母：{}，其他{}。".format(a,b,c,d))
