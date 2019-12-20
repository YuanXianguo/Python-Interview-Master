"""
你有3个需要完成的任务，完成这3个任务是需要付出代价的。
首先，你可以不花任何代价的完成一个任务；然后，在完成了第i个任务之后，你可以花费|Ai - Aj|的代价完成第j个任务。|x|代表x的绝对值。
计算出完成所有任务的最小代价。

输入描述:
一行3个整数A1,A2,A3，每个数字之间用一个空格分隔。所有数字都是整数，并且在[1,100]范围内。
"""


def main(nums):
    nums.sort()
    res = 0
    for i in range(1, len(nums)):
        res += abs(nums[i] - nums[i-1])
    return res


nums = list(map(int, input().split()))
print(main(nums))
