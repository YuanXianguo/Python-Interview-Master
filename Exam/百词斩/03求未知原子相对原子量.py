def get_m(string, m, nums):
    flag = 0
    tmp = 0
    index = 0
    n = len(string)
    res = 0
    cnt = 0
    flag2 = 0
    while index < n:
        if string[index] == "(":
            flag = 1
            index += 1
        elif string[index].isalpha():
            if flag:
                if string[index+1].isdigit():
                    tmp += nums[string[index]] * int(string[index+1])
                    index += 2
                else:
                    tmp += nums[string[index]]
                    index += 1
            else:
                if string[index+1].isdigit():
                    res += nums[string[index]] * int(string[index+1])
                    index += 2
                else:
                    res += nums[string[index]]
                    index += 1
        elif string[index] == ")":
            res += tmp * int(string[index+1])
            if flag2:
                cnt *= int(string[index+1])
            index += 2
        else:
            cnt = 1
            if flag:
                flag2 = 1
            if string[index+1].isdigit():
                cnt *= int(string[index+1])
                index += 2
            else:
                index += 1
    return (m-res) // cnt


t = input().split()
string, m = t[0], int(t[1])
n = int(input())
nums = dict()
while n:
    tmp = input().split()
    nums[tmp[0]] = int(tmp[1])
    n -= 1
print(get_m(string, m, nums))
