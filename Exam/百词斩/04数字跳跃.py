def get_cnt(nums):
    for i in nums:
        cnt = 0
        for j in range(i[0]+1):
            if str(i[1]) in str(j):
                cnt += 1
        print(cnt)


n = int(input())
nums = list()
while n:
    nums.append([int(i) for i in input().split()])
    n -= 1
get_cnt(nums)
