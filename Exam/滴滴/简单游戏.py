def min_sum(nums, m):
    left, right = 0, m-1
    min_ = sum(nums[left: right+1])
    right += 1
    res = [min_]
    while right < len(nums):
        min_ = min_-nums[left]+nums[right]
        res.append(min_)
        left += 1
        right += 1
        print(res)

    return min(res)


nm = list(map(int, input().split()))
n, m = nm[0], nm[1]
nums = list(map(int, input().split()))
print(min_sum(nums, m))
