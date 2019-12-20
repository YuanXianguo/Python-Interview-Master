def fact(n):
    if n == 1:
        jc = 1
    else:
        jc = n * fact(n-1)
    return jc

def main():
    n = eval(input())
    res = 0
    for i in range(1,n+1):
        res += fact(i)
    print(res)

main()
