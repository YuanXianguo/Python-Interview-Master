list = []
n = eval(input(':'))
for i in range(0,7,2):
    list.append(i)
for j in list:
    if j > n:
        list.insert(list.index(j),n)
        break
print(list)
