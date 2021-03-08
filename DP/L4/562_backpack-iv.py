# 562. Backpack IV
# Description
# Given an integer array nums[] which contains n unique positive numbers, num[i] indicate the size of ith item.
# An integer target denotes the size of backpack. Find the number of ways to fill the backpack.
#
# Each item may be chosen unlimited number of times
#
# Have you met this question in a real interview?
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

class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """

    def backPackIV(self, nums, target):

        # dp[i][w] number of ways to form weight w using first i numbers
        n = len(nums)
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        for i in range(0, n + 1):
            dp[i][0] = 1  # 1 way to get the weight 0 using first i items, select nothing

        for w in range(1, target + 1):
            dp[0][w] = 0

        for i in range(1, n + 1):
            for w in range(1, target + 1):
                k = 0  # use the ith item k times, k=0,1,2,3,4
                while w - k * nums[i - 1] >= 0:
                    dp[i][w] += dp[i - 1][w - k * nums[i - 1]]
                    k += 1

        return dp[n][target]

