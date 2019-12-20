"""try:
    n = eval(input("输入正整数："))
    res = 0
    while n > 0:
        for i in range(1,n+1):
            if pow(2,i) > n:
                res += pow(10,i-1)
                n -= pow(2,i-1)
                break
    res_num = '0b' + str(res)
    print(res_num)
except:
    print("输入错误")"""

n = eval(input("输入正整数："))
blist = []
while n > 0:
    m = n % 2
    blist.append(m)
    n //= 2
res_num = '0b'
for i in blist[::-1]:
    res_num += str(i)
print("转换为二进制为：{}".format(res_num))
