# 868. Maximum Average Subarray
# 中文English
# Given an array consisting of n integers, find the contiguous subarray of given length k
# that has the maximum average value. You need to output the maximum average value.
#
# Example
# Example1
#
# Input:  nums = [1,12,-5,-6,50,3] and k = 4
# Output: 12.75
# Explanation:
# Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
# Example2
#
# Input:  nums = [4,2,1,3,3] and k = 2
# Output: 3.00
# Explanation:
# Maximum average is (3+3)/2 = 6/2 = 3.00
# Notice
# 1. 1 <= k <= n <= 30,000.
# 2. Elements of the given array will be in the range [-10,000, 10,000].

import sys


class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: the maximum average value
    """

    # because k(window size) is fixed, maximum of average is the maximum sum / k
    def findMaxAverage(self, nums, k):
        # Write your code here
        if len(nums) == 0 or len(nums)<k:
            return None

        maximum_sum = -1 * sys.maxsize

        # put the first k-1 numbers into the curr_sum.
        curr_sum = sum(nums[0:k - 1])

        # iterate the right boundary of the window.
        for j in range(k - 1, len(nums)):
            curr_sum += nums[j]
            maximum_sum = max(maximum_sum, curr_sum)
            curr_sum -= nums[j - (k - 1)]

        return maximum_sum / k

sol = Solution()
sol.findMaxAverage(nums=[1,12,-5,-6,50,3], k=4)
