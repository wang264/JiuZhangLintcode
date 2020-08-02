# 564. Combination Sum IV
# 中文English
# Given an integer array nums with all positive numbers and no duplicates, find the number of
# possible combinations that add up to a positive integer target.
#
# Example
# Example1
#
# Input: nums = [1, 2, 4], and target = 4
# Output: 6
# Explanation:
# The possible combination ways are:
# [1, 1, 1, 1]
# [1, 1, 2]
# [1, 2, 1]
# [2, 1, 1]
# [2, 2]
# [4]
# Example2
#
# Input: nums = [1, 2], and target = 4
# Output: 5
# Explanation:
# The possible combination ways are:
# [1, 1, 1, 1]
# [1, 1, 2]
# [1, 2, 1]
# [2, 1, 1]
# [2, 2]
# Notice
# A number in the array can be used multiple times in the combination.
# Different orders are counted as different combinations.

# dp[target] number of combination that can sum to target with the numbers from 'nums'


class Solution:

    def backPackVI(self, nums, target):
        if not nums:
            return 0

        dp = [0] * (target + 1)
        dp[0] = 1

        for j in range(1, target + 1):
            for num in nums:
                if num > j:
                    continue
                dp[j] += dp[j - num]

        return dp[target]


sol = Solution()
sol.backPackVI(nums=[1, 2], target=4)
