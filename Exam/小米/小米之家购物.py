def solution(prices, budget):
    prices.sort(reverse=True)
    cnt = 0
    index = 0
    n = len(prices)
    if not n or budget < prices[0]:
        return -1
    while budget and index < n:
        cnt += budget // prices[index]
        budget %= prices[index]
        index += 1
    return cnt


print(solution([400,220, 8, 1], 1000))
