def solution(N, M):
    if N < 1 or M < 1:
        return
    tmp = [i+1 for i in range(N)]
    res = list()
    while len(tmp) > M:
        this = list()
        f = M - 1
        while f < len(tmp):
            print(f, tmp)
            this.append(tmp[f])
            f += M
        res.extend(this)
        for i in this:
            tmp.remove(i)
    res = list(map(str, res))
    print(" ".join(res))


N,M = [int(i) for i in input().split()]
solution(N,M)
