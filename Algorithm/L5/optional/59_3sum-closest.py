# 59. 3Sum Closest
# 中文English
# Given an array S of n integers, find three integers in S such that the sum is closest to a given number,
#  target. Return the sum of the three integers.
#
# Example
# Example 1:
#
# Input:[2,7,11,15],3
# Output:20
# Explanation:
# 2+7+11=20
# Example 2:
#
# Input:[-1,2,1,-4],1
# Output:2
# Explanation:
# -1+2+1=2
# Challenge
# O(n^2) time, O(1) extra space
#
# Notice
# You may assume that each input would have exactly one solution.
import sys


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """

    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers.sort()
        closest_diff = sys.maxsize
        closest_sum = sys.maxsize
        # a+ b + c closest to target ------> a+b closest to    target - c
        # we assume a < b < c to prevent duplicate answer
        for idx_c, c in enumerate(numbers):
            two_sum_closest_diff, two_sum_closest_sum = self.two_sum_closest(numbers, start=0, end=idx_c - 1,
                                                                           target=target - c)
            if two_sum_closest_diff < closest_diff:
                closest_diff = two_sum_closest_diff
                closest_sum = two_sum_closest_sum + c
        return closest_sum

    def two_sum_closest(self, numbers, start, end, target):
        if start >= end:
            return sys.maxsize, sys.maxsize
        left = start
        right = end
        closest_diff = sys.maxsize
        closest_sum = sys.maxsize
        while left < right:
            two_sum = numbers[left] + numbers[right]
            if abs(two_sum - target) < closest_diff:
                closest_diff = abs(two_sum - target)
                closest_sum = two_sum
            if two_sum < target:
                left += 1
            elif two_sum > target:
                right -= 1
            else:
                return 0, two_sum

        return closest_diff, closest_sum


sol = Solution()
sol.threeSumClosest(numbers=[2, 7, 11, 15], target=3)
