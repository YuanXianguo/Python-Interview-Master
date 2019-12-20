def age(n):
    if n == 1:
        ag = 10
    else:
        ag = age(n-1) + 2
    return ag
for i in range(5):
    print(age(i+1))
