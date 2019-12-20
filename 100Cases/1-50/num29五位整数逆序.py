def revs(char, n):
    if n == 0:
        res = ''
    else:
        res = char[n-1] + revs(char, n-1)
    return res

char = input()
n = len(char)
print(n, revs(char, n))
