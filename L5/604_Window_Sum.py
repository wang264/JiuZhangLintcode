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
        n = len(nums)
        if n < k or k == 0:
            return []
        if n == k:
            return [sum(nums)]

        slow = 0
        fast = k # one index to the right of the current window


        sum_val = 0
        for i in range(k):
            sum_val+=nums[i]

        rslt = [sum_val]

        while fast < n:
            sum_val = sum_val - nums[slow] + nums[fast]
            rslt.append(sum_val)
            slow += 1
            fast += 1

        return rslt

sol = Solution()
sol.winSum([1,2,7,8,5],3)