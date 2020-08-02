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
# It is guaranteed that the length of nums doesn't exceed 20000
# The product of the largest subsequence of the product, less than 2147483647


class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """

    def maxProduct(self, nums):
        n = len(nums)
        # dp_min[i] = the minimum of the the product of the continuous subsequence which the last number is nums[i]
        # dp_max[i] = the maximum of the the product of the continuous subsequence which the last number is nums[i]

        dp_min = [0] * n
        dp_max = [0] * n

        dp_max[0] = dp_min[0] = nums[0]

        for i in range(1, n):
            if nums[i] < 0:
                # if nums[i] is negative,
                # the maximum product that ends in ith position is either the minimum product that
                # ends in (i-1) position times nums[i] or restart from nums[i].
                dp_max[i] = max(nums[i], nums[i] * dp_min[i - 1])
                dp_min[i] = min(nums[i], nums[i] * dp_max[i - 1])
            else:
                # if nums[i] is positive,
                # the maximum product that ends in ith position is either the maximum product that
                # ends in (i-1) position times nums[i] or restart from nums[i]
                dp_max[i] = max(nums[i], nums[i] * dp_max[i - 1])
                dp_min[i] = min(nums[i], nums[i] * dp_min[i - 1])

        return max(dp_max)


sol = Solution()
sol.maxProduct(nums=[2, 3, -2, 4])
sol.maxProduct(nums=[-1, 2, 4, 1])
