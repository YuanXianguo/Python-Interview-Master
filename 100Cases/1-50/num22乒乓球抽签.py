list = list('xyz')
a,b,c = 0,0,0
for i in list:
    if i != 'x' and i != 'z':
        c = i
    elif i != 'x' and i != 'c':
        a = i
    else:
        b = i
print(a,b,c)

