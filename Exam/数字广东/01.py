def bubble_sort(nums):
    for i in range(len(nums)-1, -1, -1):
        flag = 1
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = 0
        if flag:
            break
    return nums
