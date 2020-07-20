# Description
# English
# Given an array of n positive integers and a positive integer s, find the minimal length of a subarray
# of which the sum >= s. If there isn't one, return -1 instead.
# Have you met this question in a real interview?
#
# Example 1:
# Input: [2,3,1,2,4,3], s = 7
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:
# Input: [1, 2, 3, 4, 5], s = 100
# Output: -1
# Challenge
# If you have figured out the O(nlog n) solution, try coding another solution of which the time complexity is O(n).
#
# 给定一个由n个正整数组成的数组和一个正整数 s ，请找出该数组中满足其和 >= s 的最小长度子数组。如果无解，则返回 - 1。
#
# 样例1:
# 输入: [2, 3, 1, 2, 4, 3], s = 7
# 输出: 2
# 解释: 子数组[4, 3]
# 是该条件下的最小长度子数组。
#
# 样例2:
# 输入: [1, 2, 3, 4, 5], s = 100
# 输出: -1
#
# Challenge 如果你已经完成了O(nlogn) 时间复杂度的编程，请再试试O(n)时间复杂度。

class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """

    def minimumSize(self, nums, s):
        # write your code here
        # 同向双指针
        # 每次删除左指针左边的数字。
        # 只要当前和小于S, 右指针继续向右移动
        # 时间复杂度O(N)

        if nums is None or len(nums) == 0:
            return -1

        n = len(nums)
        min_length = n + 1
        subarray_sum = 0
        left = 0
        for right in range(len(nums)):
            subarray_sum += nums[right]
            # we have one solution
            if subarray_sum >= s:
                min_length = min(min_length, right - left + 1)
                # try to find the shortest solution when fix 'right'
                while subarray_sum - nums[left] >= s:
                    subarray_sum -= nums[left]
                    left += 1
                    min_length = min(min_length, right - left + 1)

        return min_length if min_length != n + 1 else -1

sol = Solution()
sol.minimumSize(nums=[2, 3, 1, 2, 4, 3], s=7)
