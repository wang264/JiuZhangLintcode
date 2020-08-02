# 139. Subarray Sum Closest
# 中文English
# Given an integer array, find a subarray with sum closest to zero. Return the indexes of
# the first number and last number.
#
# Example
# Example1
#
# Input:
# [-3,1,1,-3,5]
# Output:
# [0,2]
# Explanation: [0,2], [1,3], [1,1], [2,2], [0,4]
# Challenge
# O(nlogn) time
#
# Notice
# It is guaranteed that the sum of any numbers is in [-2^{31},2^{31}-1]

import sys


class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySumClosest_slow(self, nums):
        # write your code here
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        cloest = (sys.maxsize, (-1, -1))  # tuple of (max_value, (start_index, end_index))
        for start_idx in range(n):
            for end_idx in range(start_idx, n):
                closest_candidate = prefix_sum[end_idx + 1] - prefix_sum[start_idx]
                if abs(closest_candidate) < abs(cloest[0]):
                    cloest = (closest_candidate, (start_idx, end_idx))

        return [cloest[1][0], cloest[1][1]]

    # 前缀和优化 + 排序贪心
    # 先对数组求一遍前缀和，然后把前缀和排序，令排完序的前缀和是B数组
    # 题目要求子数组的和最接近0，也就是B数组两个值相减最接近0
    # 既然B数组两个值相减最接近0，也就是B数组两个最接近的数
    # 对B数组排序，最接近的数肯定是相邻的
    # 排完序后，我们只要找相邻元素做差就好了

    def subarraySumClosest(self, nums):
        # write your code here
        n = len(nums)
        prefix_sum = [[None, None]] * (n + 1)
        prefix_sum[0] = [0, -1]

        for i in range(1, n + 1):
            prefix_sum[i] = [prefix_sum[i - 1][0] + nums[i - 1], i - 1]

        prefix_sum.sort()
        closest_val = sys.maxsize
        closest_idx = [-1, -1]
        for i in range(len(prefix_sum) - 1):
            closest_candidate = prefix_sum[i + 1][0] - prefix_sum[i][0]
            if abs(closest_candidate) < abs(closest_val):
                closest_val = closest_candidate
                idx_1, idx_2 = prefix_sum[i + 1][1], prefix_sum[i][1]
                if idx_1 < idx_2:
                    closest_idx = [idx_1 + 1, idx_2]
                else:
                    closest_idx = [idx_2 + 1, idx_1]

        return closest_idx


sol = Solution()
sol.subarraySumClosest(nums=[-3, 1, 1, -3, 5])
sol.subarraySumClosest(nums=[6, -4, -8, 3, 1, 7]) == ([1, 5] or [4,4])
