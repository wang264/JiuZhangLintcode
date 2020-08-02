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

    # dp[j-1] 表示以第i个数字（nums[j-1]为结尾的最长上升子序列的长度。
    # 对于每个数字，枚举前面所有小于自己的数字j，
    # dp[j] = max{dp[i] +1 | for all i<j and nums[i]<nums[j]}    如果前面没有比自己小的，dp[j] = 1;
    def longestIncreasingSubsequence(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        dp = [0] * n
        dp[0] = 1
        for j in range(1, n):
            max_length = 1
            for i in range(0, j):  # i<j
                if nums[i] < nums[j]:
                    max_length = max(max_length, dp[i] + 1)
            dp[j] = max_length

        return max(dp)


sol = Solution()
assert sol.longestIncreasingSubsequence(nums=[4, 2, 4, 5, 3, 7]) ==4
assert sol.longestIncreasingSubsequence([]) == 0
assert sol.longestIncreasingSubsequence([1]) ==1
