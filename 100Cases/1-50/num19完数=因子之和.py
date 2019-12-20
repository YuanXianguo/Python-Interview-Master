for n in range(2,1001):
    list = []
    for i in range(1,n):
        if n % i == 0:
            m = int(n / i)
            if i > m:
                break
            else:
                list.append(i)
                if m != n:
                    list.append(m)
    list.sort()
    count = 0
    for i in list:
        count += i
    if count == n:
        print(n)
        for i in list:
            print(i,end=' ')
        print('')

