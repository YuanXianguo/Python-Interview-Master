n = 0
while n < 7:
    n += 1
    num = eval(input(':'))
    if 0 < num < 51:
        res = '*' * num
        print(res)
    else:
        continue
