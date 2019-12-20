"""题目：取一个整数a从右端开始的4〜7位。"""
a = 123456789
b = str(a)
c = b[::-1]
for i in c:
    if 3 <= c.index(i) <=6:
        print(i)
