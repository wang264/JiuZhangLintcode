# 604. Window Sum
# 中文English
# Given an array of n integers, and a moving window(size k), move the window at each iteration from the start of
# the array, find the sum of the element inside the window at each moving.
#
# 样例
# Example 1
#
# Input：array = [1,2,7,8,5], k = 3
# Output：[10,17,20]
# Explanation：
# 1 + 2 + 7 = 10
# 2 + 7 + 8 = 17
# 7 + 8 + 5 = 20

class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    def winSum(self, nums, k):
        # write your code here
        if k == 0:
            return []

        rslt = []
        window_sum = 0
        # add the first k element
        for i in range(k):
            window_sum += nums[i]

        rslt.append(window_sum)
        i = k  # the k+1 th element
        kick_out = 0
        while i < len(nums):
            window_sum += nums[i]
            window_sum -= nums[kick_out]
            rslt.append(window_sum)
            i += 1
            kick_out += 1

        return rslt


sol = Solution()
sol.winSum(nums=[1, 2, 7, 8, 5], k=3)
