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

class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """

    def backPackVI(self, nums, target):
        # write your code here
        # f[i] = 有多少种组合能拼出重量i
        # f[i] = 枚举最后一个包里的物品nums[0], nums[1] ... nums[n-1]。
        # f[i] = f[i - nums[0]] + f[i - nums[1]] ... + f[i - nums[n-1]]

        f = [None] * (target + 1)
        f[0] = 1
        for i in range(1, target + 1):
            f[i] = 0
            for j in range(len(nums)):
                # 如果最后一个物品为j, 有多少种组合能组成 i-nums[j] 的重量。
                if i - nums[j] < 0:
                    continue
                f[i] += f[i - nums[j]]

        return f[target]


sol = Solution()
nums = [1, 2, 4]
target = 4
sol.backPackVI(nums, target)
