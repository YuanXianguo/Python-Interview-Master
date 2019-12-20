def revs(n,l):
    if l == 0:
        res = ''
    else:
        res = n[l-1]+ revs(n,l-1)
    return res

n = input("随意输入字符，我将打印逆序：")
l = len(n)
print(revs(n,l))
