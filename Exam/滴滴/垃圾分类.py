def max_num(n, nums, d):
    d = sorted(d.items(), key=lambda s: s[1], reverse=True)
    cnt = 0
    for i in d:
        flag = 1
        flag2 = 0
        for j in nums:
            if len(j) == 2:
                flag = 0
                if i[0] in j:
                    flag2 = 1
                    j.remove(i[0])
        if flag:
            break
        if flag2:
            cnt += 1

    return n - cnt


nm = list(map(int, input().split()))
n, m = nm[0], nm[1]
nums = list()
d = dict()
while m:
    tmp = list(map(int, input().split()))
    for i in tmp:
        d[i] = d.get(i, 0) + 1
    nums.append(tmp)
    m -= 1
print(max_num(n, nums, d))
