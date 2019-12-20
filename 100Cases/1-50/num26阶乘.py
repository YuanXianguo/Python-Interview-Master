def fact(n):
    if n == 1:
        jc = 1
    else:
        jc = n * fact(n-1)
    return jc

print(fact(5))
