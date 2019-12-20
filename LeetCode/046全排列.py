"""
给定一个没有重复数字的序列，返回其所有可能的全排列。
"""


class Solution:
    def permute(self, nums):
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        # 对字符串遍历，每次取出一个字符，其它的字符串进行递归
        for i in range(len(nums)):
            tmp = self.permute(nums[:i]+nums[i+1:])
            # 对递归结果进行遍历，将取出的字符插入每个字符串列表中
            for j in tmp:
                j.insert(0, nums[i])
                res.append(j)
        return res  # 返回当前字符串所有可能排列列表


class Solution2:
    def permute(self, nums):
        res = []

        def back_track(nums, track):
            """track: 某条路径"""
            if not nums:
                res.append(track)
                return
            for i in range(len(nums)):
                back_track(nums[:i] + nums[i+1:], track + [nums[i]])
        back_track(nums, [])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))
    s2 = Solution2()
    print(s2.permute([1,2,3]))
    print(s2.permute([2,2]))
