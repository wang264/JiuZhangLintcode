# 521. Remove Duplicate Numbers in Array
# 中文English
# Given an array of integers, remove the duplicate numbers in it.
#
# You should:
#
# 1. Do it in place in the array.
# 2. Move the unique numbers to the front of the array.
# 3. Return the total number of the unique numbers.

# Example
# Example 1:
#
# Input:
# nums = [1,3,1,4,4,2]
# Output:
# [1,3,4,2,?,?]
# 4
# Explanation:
#
# 1. Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
# 2. Return the number of unique integers in nums => 4.
# Actually we don't care about what you place in ?, we only care about the part which has no duplicate integers.

# Example 2:
#
# Input:
# nums = [1,2,3]
# Output:
# [1,2,3]
# 3
# Challenge
# 1. Do it in O(n) time complexity.
# 2. Do it in O(nlogn) time without extra space.

# Notice
# You don't need to keep the original order of the integers.


class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """

    def deduplication(self, nums):
        # write your code here
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        nums.sort()
        count = 1
        prev = 0
        for curr in range(1, len(nums)):
            if nums[curr] != nums[prev]:
                prev += 1
                nums[prev] = nums[curr]
                count += 1
        return count


class Solution2:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """

    def deduplication(self, nums):
        # write your code here
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        have_seen = set()
        count = 0

        prev = 0
        curr = 0
        while curr < len(nums):
            if nums[curr] not in have_seen:
                nums[prev] = nums[curr]
                prev += 1
                curr + 1
                have_seen.add(nums[curr])
                count += 1

            else:
                curr += 1
        return count


sol = Solution2()
nums = [1, 3, 1, 4, 4, 2]
sol.deduplication(nums)
