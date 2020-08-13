# 539. Move Zeroes
# 中文English
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Example
# Example 1:
#
# Input: nums = [0, 1, 0, 3, 12],
# Output: [1, 3, 12, 0, 0].
# Example 2:
#
# Input: nums = [0, 0, 0, 3, 1],
# Output: [3, 1, 0, 0, 0].
# Notice
# 1.You must do this in-place without making a copy of the array.
# 2.Minimize the total number of operations.

class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """

    def moveZeroes(self, nums):
        # write your code here
        if len(nums) == 0 or len(nums) == 1:
            return nums

        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1

        while slow < len(nums):
            nums[slow] = 0
            slow +=1


class Solution2:
    """
    @param nums: an integer array
    @return: nothing
    """

    def moveZeroes(self, nums):
        n = len(nums)
        left = 0  # store the index that point to zero.(we can overwrite zero in here)
        right = 0  # we iterate from 0 to n -1

        # find the first position of zero in the array
        while left < n and nums[left] != 0:
            left += 1
            right += 1

        # increase right to point to the next number
        right += 1

        # iterate right pointer from this location to end, and for every non zero element it encounter
        # put it in the left index position and increase left.
        while right < n:
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
            right += 1

        # fill in all zeros....
        while left < n:
            nums[left] = 0
            left += 1

sol = Solution2()
a = [4]
sol.moveZeroes(nums=a)
print(a)