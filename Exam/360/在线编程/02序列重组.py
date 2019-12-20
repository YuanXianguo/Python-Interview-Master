n, m = list(map(int, input().split()))
n1 = list(map(int, input().split()))
n2 = list(map(int, input().split()))
n2.sort()


def bin_search(array, num):
    if not array:
        return -1
    left, right = 0, len(array)-1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < num:
            left = mid + 1
        elif array[mid] > num:
            right = mid - 1
        else:
            return num
    return -1


res = list()
for j in range(1, m):
    if len(res) == n:
        break
    for i in n1:
        num = bin_search(n2, m - j - i)
        if num != -1:
            n2.remove(num)
            res.append(m - j)
        else:
            num2 = bin_search(n2, 2 * m - j - i)
            if num2 != -1:
                n2.remove(num2)
                res.append(2 * m - j)

res = list(map(lambda d: str(d % m), res))
print(" ".join(res))
