# 609. Two Sum - Less than or equal to target
# 中文English
# Given an array of integers, find how many pairs in the array such that their sum is less than or equal to a specific target number. Please return the number of pairs.
#
# Example
# Example 1:
#
# Input: nums = [2, 7, 11, 15], target = 24.
# Output: 5.
# Explanation:
# 2 + 7 < 24
# 2 + 11 < 24
# 2 + 15 < 24
# 7 + 11 < 24
# 7 + 15 < 24
# Example 2:
#
# Input: nums = [1], target = 1.
# Output: 0.lo

class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """

    def twoSum5(self, nums, target):
        if len(nums) <= 1:
            return 0

        nums.sort()

        n = len(nums)
        left = 0
        right = n - 1
        ans_count = 0

        while left < right:
            # right pointer is not out of bound and the two sum is still less than or equal to target
            # we try to find ONE SINGLE answer while we fix the 'left pointer'
            value = nums[left] + nums[right]
            if value > target:
                right -= 1
            else:  # we find the first answer. then we find ALL the answers while we fix the 'left pointer'
                ans_count += right - left
                # then we are moving the left pointer.-->
                left += 1
        return ans_count


class Solution2:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """

    def twoSum5(self, nums, target):
        # write your code here
        # we have left pointer and right pointer,
        # as left pointer move to the right ....
        # the right pointer only move to the left ....
        nums.sort()
        n = len(nums)
        if n <= 1:
            return 0

        left = 0
        right = 1
        count = 0
        # find the first answer
        while right < n and nums[left] + nums[right] <= target:
            count += 1
            right += 1

        right -= 1
        left += 1
        # find the other answers
        while left < n and right >= 0 and left < right:
            while left < right and nums[left] + nums[right] > target:
                right -= 1
            if left < right:
                count += right - left

            left += 1

        return count


sol = Solution2()
assert sol.twoSum5(nums=[2, 7, 11, 15], target=24) == 5
assert sol.twoSum5(nums=[1], target=1) == 0
assert sol.twoSum5(nums=[1, 0, -1], target=0) == 2
assert sol.twoSum5(nums=[-1, -2, -3, -4, -5, -6, -100, -98, -111, -11], target=-111) == 11
