# 14. First Position of Target
# For a given sorted array(ascending order) and a target number, find the first index of this number in
# O(log n) time complexity.
#
# If the target number does not exist in the array, return -1.
#
# Example
# 1:
# Input: [1, 4, 4, 5, 7, 7, 8, 9, 9, 10]，1
# Output: 0
#
# Explanation: the first index of 1 is 0.
#
# Example 2:
# Input: [1, 2, 3, 3, 4, 5, 10]，3
# Output: 2
#
# Explanation:
# the first index of 3 is 2.
#
# Example 3:
# Input: [1, 2, 3, 3, 4, 5, 10]，6
# Output: -1


class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        # write your code here
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        return -1
