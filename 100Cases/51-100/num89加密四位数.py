"""题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。"""
try:
    num = input("请输入四位整数:")
    nlist = []
    if isinstance(eval(num),int):
        for i in num:
            j = (int(i) + 5) % 10
            nlist.append(j)
        nlist[0], nlist[3] = nlist[3], nlist[0]
        nlist[1], nlist[2] = nlist[2], nlist[1]
        for n in nlist:
            print(n, end='')
    else:
        print('输入整数')
except:
    print('输入整数')
