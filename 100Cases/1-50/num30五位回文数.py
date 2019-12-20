"""题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。"""
num = input("输入一个数:")
leight = len(num)
for i in range(int(leight / 2)):
    if num[i] != num[leight - i - 1]:
        print("{}不是回文数".format(num))
        break
else:
    print("{}是回文数".format(num))
