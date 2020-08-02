# 562. Backpack IV
# 中文English
# Given an integer array nums[] which contains n unique positive numbers, num[i] indicate the size of ith item.
# An integer target denotes the size of backpack. Find the number of ways to fill the backpack.
#
# Each item may be chosen unlimited number of times
#
# Example
# Example1
#
# Input: nums = [2,3,6,7] and target = 7
# Output: 2
# Explanation:
# Solution sets are:
# [7]
# [2, 2, 3]
# Example2
#
# Input: nums = [2,3,4,5] and target = 7
# Output: 3
# Explanation:
# Solution sets are:
# [2, 5]
# [3, 4]
# [2, 2, 3]

# dp[i][w] = number of ways to fill backpack to weight w with first i items.
class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """

    def backPackIV_slow(self, nums, target):
        # write your code here
        n = len(nums)
        dp = [[None] * (target + 1) for _ in range(n + 1)]

        dp[0][0] = 1  # 1 way to achieve weight 0, do not select anything
        for w in range(1, target + 1):
            dp[0][w] = 0  # can not achieve weight w with no items

        for i in range(1, n + 1):
            dp[i][0] = 1  # 1 way to achieve weight 0 with first i items. do not select anything.

        for i in range(1, n + 1):
            for w in range(1, target + 1):
                dp[i][w] = 0  # assume we can not get to weight w with first i items.
                k = 0
                while w - k * nums[i - 1] >= 0:
                    dp[i][w] += dp[i - 1][w - k * nums[i - 1]]  # option 1: we pick K times ith item.
                    k = k + 1

        return dp[n][target]

    def backPackIV(self, nums, target):
        # write your code here
        n = len(nums)
        dp = [[None] * (target + 1) for _ in range(2)]

        dp[0][0] = 1  # 1 way to achieve weight 0, do not select anything
        for w in range(1, target + 1):
            dp[0][w] = 0  # can not achieve weight w with no items

        for i in range(1, 2):
            dp[i][0] = 1  # 1 way to achieve weight 0 with first i items. do not select anything.

        for i in range(1, n + 1):
            for w in range(1, target + 1):
                dp[i % 2][w] = 0  # assume we can not get to weight w with first i items.
                k = 0
                while w - k * nums[i - 1] >= 0:
                    dp[i % 2][w] += dp[(i - 1) % 2][w - k * nums[i - 1]]  # option 1: we pick K times ith item.
                    k = k + 1

        return dp[n % 2][target]


sol = Solution()
assert sol.backPackIV(nums=[2, 3, 6, 7], target=7) == 2
assert sol.backPackIV(nums=[2, 3, 4, 5], target=7) == 3
