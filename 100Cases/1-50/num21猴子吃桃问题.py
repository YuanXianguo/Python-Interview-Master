def num(n):
    if n == 1:
        res = 1
    else:
        res = int((num(n-1)+1) * 2)
    return res

print(num(10))
