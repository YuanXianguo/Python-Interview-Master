s = input()
tmp = dict()
for i in s:
    tmp[i] = tmp.get(i, 0) + 1
print(max(tmp.values()))
