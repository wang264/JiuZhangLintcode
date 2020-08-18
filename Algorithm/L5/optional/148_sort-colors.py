# 148. Sort Colors
# 中文English
# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Example
# Example 1
#
# Input : [1, 0, 1, 2]
# Output : [0, 1, 1, 2]
# Explanation : sort it in-place
# Challenge
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
#
# Could you come up with an one-pass algorithm using only constant space?
#
# Notice
# You are not suppose to use the library's sort function for this problem.
# You should do it in-place (sort numbers in the original array).

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """

    def sortColors(self, nums):
        # write your code here
        # first separate 0 | 1,2
        s_1, e_1 = self.partition(nums, 0, 0, len(nums) - 1)
        # then separate 1 | 2
        self.partition(nums, 1, s_1, e_1)

    def partition(self, nums, flag, start, end):
        # separate and place
        left = start
        right = end
        while left <= right:
            while left <= right and nums[left] == flag:
                left += 1
            while left <= right and nums[right] != flag:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # the start index and end index for the value in nums
        # that are not equal to 'flag'
        return left, end