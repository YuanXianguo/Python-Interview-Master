"""题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。"""
count = 0
for i in range(1,5):
    for m in range(1,5):
        for n in range(1,5):
            if i != m and i != n and m != n:
                num = str(i)+str(m)+str(n)
                count += 1
                print(int(num))
print(count)
