# 633. Find the Duplicate Number
# 中文English
# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
# guarantee that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
#
# Example
# Example 1:
#
# Input:
# [5,5,4,3,2,1]
# Output:
# 5
# Example 2:
#
# Input:
# [5,4,4,3,2,1]
# Output:
# 4
# Notice
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n^2).
# There is only one duplicate number in the array, but it could be repeated more than once.

class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """

    def findDuplicate(self, nums):
        # write your code here
        pass

sol = Solution()
sol.findDuplicate(nums=[5,4,4,3,2,1])
sol.findDuplicate(nums=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])