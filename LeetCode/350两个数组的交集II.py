def intersect(nums1, nums2):
    res = []
    tmp = {}
    for i in nums1:
        tmp[i] = tmp.get(i, 0) + 1
    for i in nums2:
        if tmp.get(i, 0) > 0:
            res.append(i)
            tmp[i] -= 1
    return res


if __name__ == '__main__':
    print(intersect([1,2,2,1],[2,2]))
    print(intersect([4,9,5],[9,4,9,4,8]))
