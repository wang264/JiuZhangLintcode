# 41. Maximum Subarray
# 中文English
# Given an array of integers, find a contiguous subarray which has the largest sum.
#
# Example
# Example1:
#
# Input: [−2,2,−3,4,−1,2,1,−5,3]
# Output: 6
# Explanation: the contiguous subarray [4,−1,2,1] has the largest sum = 6.
# Example2:
#
# Input: [1,2,3,4]
# Output: 10
# Explanation: the contiguous subarray [1,2,3,4] has the largest sum = 10.
# Challenge
# Can you do it in time complexity O(n)?
#
# Notice
# The subarray should contain at least one number.

import sys

class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, nums):
        n = len(nums)
        dp = [None] * n
        # dp[i] = the sum of maximum subarray ending at nums[i]
        dp[0] = nums[0]

        for i in range(1, n):
            # if the sum of maximum subarray ending at nums[i-1] is smaller than zero, then we dont want to use those
            # numbers since it will make the sum including nums[i] smaller. we would rather start fresh.
            if dp[i - 1] < 0:
                dp[i] = nums[i]
            # we want to inlcude that number, it will make the sum larger.
            else:
                dp[i] = dp[i - 1] + nums[i]

        return max(dp)

    def maxSubArray_prefixsum(self, nums):
        # prefix_sum记录前i个数的和，max_Sum记录全局最大值，min_Sum记录前i个数中0-k的最小值
        min_prefix_sum, max_sum = 0, -sys.maxsize
        prefix_sum = 0

        for num in nums:
            # min_prefix_sum = (nums[0] + nums[1] +......)中最小的前缀和
            prefix_sum += num
            # 想要总和最大，那要减去前面的前缀和最小的。
            max_sum = max(max_sum, prefix_sum - min_prefix_sum)
            min_prefix_sum = min(min_prefix_sum, prefix_sum)

        return max_sum



sol = Solution()
sol.maxSubArray(nums=[-2, 2, -3, 4, -1, 2, 1, -5, 3])
sol.maxSubArray_prefixsum(nums=[-2, 2, -3, 4, -1, 2, 1, -5, 3])
