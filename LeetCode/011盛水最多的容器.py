"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
"""


def maxArea(height):
    max_a = 0
    for i in range(len(height)- 1):
        for j in range(i, len(height)):
            this = (j - i) * min(height[i], height[j])
            if this > max_a:
                max_a = this
    return max_a


class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_a = (right - left) * min(height[left], height[right])
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            this = (right - left) * min(height[left], height[right])
            if this > max_a:
                max_a = this
        return max_a


if __name__ == '__main__':
    print(maxArea([1,8,6,2,5,4,8,3,7]))
