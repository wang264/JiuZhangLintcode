# 402. Continuous Subarray Sum
# 中文English
# Given an integer array, find a continuous subarray where the sum of numbers is the biggest. Your code should
# return the index of the first number and the index of the last number. (If their are duplicate answer, return
#  the minimum one in lexicographical order)
#
# Example
# Example 1:
#
# Input: [-3, 1, 3, -3, 4]
# Output: [1, 4]
# Example 2:
#
# Input: [0, 1, 0, 1]
# Output: [0, 3]
# Explanation: The minimum one in lexicographical order.
import sys


class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def continuousSubarraySum(self, A):
        # write your code here
        # 使用 prefixsum 来做
        max_sub_array_sum_val = -sys.maxsize
        result = []
        prefixsum = [0 for _ in range(len(A) + 1)]

        for i in range(1, len(prefixsum)):
            prefixsum[i] = prefixsum[i - 1] + A[i - 1]

        min_prefix = prefixsum[0]
        min_start = 0  # this is the index for actual array
        for i in range(1, len(prefixsum)):
            # the largest subarray sum ending in ith index must be the prefixsum[i] minus the minimum prefix sum.
            subarray_sum = prefixsum[i] - min_prefix
            if subarray_sum > max_sub_array_sum_val:
                max_sub_array_sum_val = subarray_sum
                result = [min_start, i - 1]  # the ith index in prefix sum, match the i-1 index in actual array.
            if prefixsum[i] < min_prefix:
                min_prefix = prefixsum[i]
                min_start = i

        return result


sol = Solution()
sol.continuousSubarraySum(A=[-3, 1, 3, -3, 4])

sol.continuousSubarraySum(A=[0, 1, 0, 1])
