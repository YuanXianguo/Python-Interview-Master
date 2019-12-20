nums = ["bed", "abc", "adg", "adf"]
nums.sort(key=lambda s: s[::-1])
print(nums)

def main(num):
    map = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    res = 0
    for i in num:
        if i in map:
            i = map[i]
        else:
            i = int(i)
        res += res * 16 + i
    return res


while True:
    try:
        print(main(input()[2:]))
    except:
        break



