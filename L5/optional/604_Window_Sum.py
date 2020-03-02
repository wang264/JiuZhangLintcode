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
        if nums is None:
            return []
        n = len(nums)
        if n < k:
            return []
        if n == k:
            return [nums(k)]
        rslt = []
        slow = 0
        fast = 0
        sum_val = 0
        while fast < k:
            sum_val += nums[fast]
            fast += 1

        rslt.append(sum_val)

        while fast < n:
            sum_val = sum_val - nums[slow] + nums[fast]
            rslt.append(sum_val)
            fast += 1
            slow += 1

        return rslt


sol = Solution()
sol.winSum(nums=[1, 2, 7, 8, 5], k=3)
