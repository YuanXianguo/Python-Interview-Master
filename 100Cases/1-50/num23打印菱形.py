def lx(n):
    for i in range(n):
        if i <= n / 2:
            print(('*'*2*i+'*').center(n,' '))
        else:
            print(('*'*2*(n-i-1)+'*').center(n,' '))
print(lx(10))
