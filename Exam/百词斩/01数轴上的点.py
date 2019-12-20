def count_(nums):
    res = set()
    for i in nums:
        if i[0] > i[1]:
            i[0], i[1] = i[1], i[0]
        for j in range(i[0], i[1]+1):
            res.add(j)
    return len(res)


n = int(input())
nums = list()
while n:
    nums.append([int(i) for i in input().split()])
    n -= 1
print(count_(nums))
