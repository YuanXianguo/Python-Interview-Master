def get_num(num1, num2):
    res = {str(i): 0 for i in range(10)}
    sum_ = 0
    num2 = str(num2)[::-1]
    for i in str(num1):
        res[i] = res.get(i) + 1
    for i in range(len(num2)):
        res[num2[i]] = res.get(num2[i]) + 1
        tmp = int(num2[i]) * num1
        tmp_str = str(tmp)
        for j in tmp_str:
            res[j] = res.get(j) + 1
        sum_ += tmp * (10 ** i)
    for i in str(sum_):
        res[i] = res.get(i) + 1
    return res


n = int(input())
res = dict()
while n:
    nums = [int(i) for i in input().split()]
    tmp = get_num(nums[0], nums[1])
    for k, v in tmp.items():
        res[k] = res.get(k, 0) + v
    tmp = sorted(tmp.items())
    for k, v in tmp:
        if k != "0":
            print(v, end=" ")
    n -= 1
    print("")

res = sorted(res.items(), key=lambda s: s[1], reverse=True)
if res[0][0] != "0":
    print(res[0][0])
else:
    print(res[1][0])
