def singleNumber(nums):
    if len(nums) == 1:
        return nums[0]
    tmp = sorted(nums)
    for i in range(0, len(nums)-1, 2):
        if tmp[i] != tmp[i+1]:
            return tmp[i]
    return tmp[-1]


if __name__ == '__main__':
    print(singleNumber([1,2,2]))
