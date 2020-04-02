# 51. Previous Permutation
# 中文English
# Given a list of integers, which denote a permutation.
#
# Find the previous permutation in ascending order.
#
# 样例
# Example 1:
#
# Input:[1]
# Output:[1]
# Example 2:
#
# Input:[1,3,2,3]
# Output:[1,2,3,3]
# Example 3:
#
# Input:[1,2,3,4]
# Output:[4,3,2,1]
#
# 注意事项
# The list may contains duplicate integers.

######################################
# same logic as #52, next permutation#
######################################


class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers that's previous permuation
    """

    def previousPermuation(self, nums):
        # find the first non decreasing number from right to left
        for i in reversed(range(0, len(nums) - 1)):
            if nums[i] > nums[i + 1]:
                # from right to left, find the first number that smaller than nums[i]
                for j in reversed(range(i + 1, len(nums))):
                    if nums[j] < nums[i]:
                        break
                # swap the two numbers
                nums[i], nums[j] = nums[j], nums[i]
                self.reverse_helper(nums, i + 1, len(nums) - 1)
                return nums

        self.reverse_helper(nums, 0, len(nums) - 1)
        return nums

    def reverse_helper(self, nums, left, right):
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


a = [1, 3, 1, 2, 4, 7]
sol = Solution()
sol.previousPermuation(nums=a)


