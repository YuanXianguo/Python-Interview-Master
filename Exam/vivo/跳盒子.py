def solution(step_list):
    if len(step_list) == 1:
        return 0
    end, max_p, step = 0, 0, 0
    for i in range(len(step_list)):
        max_p = max(max_p, step_list[i] + i)
        if i == end:
            end = max_p
            step += 1
        if end < len(step_list):
            return -1
    return step


def solution2(step_list):
    n = len(step_list)
    if n == 1:
        return 0
    dp = [0] * n
    for i in range(n):
        for j in range(step_list[i], 0, -1):
            if i + j >= n - 1:
                return dp[i] + 1
            elif dp[i+j] == 0:
                dp[i+j] = dp[i] + i
            else:
                break
    return -1


step_list = [int(i) for i in input().split()]
print(solution(step_list))
