# 191. Maximum Product Subarray
# 中文English
# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# Example
# Example 1:
#
# Input:[2,3,-2,4]
# Output:6
# Example 2:
#
# Input:[-1,2,4,1]
# Output:8
# Notice
# The product of the largest subsequence of the product, less than 2147483647


class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """

    def maxProduct(self, nums):
        # write your code here
        # max_arr[i] = maximum product that ends in ith position.
        # min_arr[i] = minimum product that ends in ith position.

        max_arr = [None] * len(nums)
        min_arr = [None] * len(nums)
        max_arr[0] = min_arr[0] = nums[0]

        for i in range(1, len(nums)):
            if nums[i] >= 0:
                # if nums[i] is positive,
                # the maximum product that ends in ith position is either the maximum product that
                # ends in (i-1) position times nums[i] or restart from nums[i]
                max_arr[i] = max(nums[i], nums[i] * max_arr[i - 1])
                min_arr[i] = min(nums[i], nums[i] * min_arr[i - 1])
            else:
                # if nums[i] is negative,
                # the maximum product that ends in ith position is either the minimum product that
                # ends in (i-1) position times nums[i] or restart from nums[i].
                max_arr[i] = max(nums[i], nums[i] * min_arr[i - 1])
                min_arr[i] = min(nums[i], nums[i] * max_arr[i - 1])

        return max(max_arr)
