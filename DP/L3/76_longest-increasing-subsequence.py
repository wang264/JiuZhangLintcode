# 76.
# Longest Increasing Subsequence
# 中文English
# Given a sequence of integers, find the longest increasing subsequence(LIS).
#
# You code should return the length of the LIS.
#
# 样例
# Example
# 1:
# Input: [5, 4, 1, 2, 3]
# Output: 3
#
# Explanation:
# LIS is [1, 2, 3]
#
# Example
# 2:
# Input: [4, 2, 4, 5, 3, 7]
# Output: 4
#
# Explanation:
# LIS is [2, 4, 5, 7]
# 挑战
# Time
# complexity
# O(n ^ 2) or O(nlogn)
#
# 说明
# What's the definition of longest increasing subsequence?
#
# The longest increasing subsequence problem is to find a subsequence of a given
# sequence in which the subsequence's elements are in sorted order, lowest to highest,
# and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous, or unique.
#
# https: // en.wikipedia.org / wiki / Longest_increasing_subsequence

class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    # Dp[i] 表示以第i个数字为结尾的最长上升子序列的长度。
    # 对于每个数字，枚举前面所有小于自己的数字j，
    # Dp[i] = max{Dp[j]} + 1 如果没有比自己小的，Dp[i] = 1;
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if nums is None or not nums:
            return 0
        dp = [1] * len(nums)
        for curr, val in enumerate(nums):
            for prev in range(curr):
                if nums[prev] < val:
                    dp[curr] = max(dp[curr], dp[prev] + 1)
        return max(dp)