list = []
li = ''
for i in range(10):
    list.append(i)
for j in list:
    li += str(j)
st = ','.join(li)
print(st)
