n, array = input().split()
n = int(n)
array = eval(array)
res = list()


def get_cnt(sum, array, path):
    for i in array:
        path.append(i)
        sum += i
        if sum == n:
            copy = sorted(path)
            if copy not in res:
                res.append(copy)
        elif sum < n:
            get_cnt(sum, array, path)
        path.pop()
        sum -= i


get_cnt(0, array, [])
print(res.count)


# 10 [2,3,5]
