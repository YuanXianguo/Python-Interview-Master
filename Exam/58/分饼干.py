n = int(input())
cnt = 0
nums = list()
while cnt < n:
    nums.append(int(input()))
    cnt += 1
def main(n, nums):
    if n == 0:
        return 0
    if n == 1:
        return 1
    res = [0] * n
    for i in range(1, n):
        if nums[i] < nums[i-1]:
            res[i] = res[i-1] - 1
        elif nums[i] > nums[i-1]:
            res[i] = res[i-1] + 1
        else:
            res[i] = res[i-1]
    min_ = min(res)
    dif = 1 - min_
    for i in range(n):
        res[i] = res[i] + dif
    res = res[::-1]
    dif = 1 - res[0]
    for i in range(n-1):
        if res[i+1] > res[i]:
            res[i] = res[i] + dif
        else:
            break
    return sum(res)

print(main(n, nums))
