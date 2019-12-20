num = input("输入十六进制：").upper()
count = len(num)
res_num = 0
nlist = ['A','B','C','D','E','F']
n_dict = {}

for j in range(6):
    n_dict[nlist[j]] = j + 10
for i in num:
    count -= 1
    if i in nlist:
        i = n_dict[i]
    res_num += int(i) * pow(16,count)
print(res_num)
