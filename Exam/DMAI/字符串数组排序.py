def str_sort(str):
    strs = str.split(",")
    strs.sort()
    return ",".join(strs)


def str_sort2(str):
    strs = str.split(",")

    def main(strs):
        n = len(strs)
        if n <= 1:
           return strs
        mid = n // 2
        lefts = main(strs[:mid])
        rights = main(strs[mid:])

        left, right = 0, 0
        res = list()
        while left < len(lefts) and right < len(rights):
            if lefts[left] <= rights[right]:
                res.append(lefts[left])
                left += 1
            else:
                res.append(rights[right])
                right += 1
        res.extend(lefts[left:])
        res.extend(rights[right:])

        return res
    return main(strs)

str = "apple,orange,cat"
print(str_sort2(str))
