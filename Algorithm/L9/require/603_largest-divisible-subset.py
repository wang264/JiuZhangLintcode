# 603. Largest Divisible Subset
# 中文English
# Given a set of distinct positive integers, find the largest subset such
# that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.
#
# 样例
# Example 1:
#
# Input: nums =  [1,2,3],
# Output: [1,2] or [1,3]
# Example 2:
#
# Input: nums = [1,2,4,8],
# Output: [1,2,4,8]
# 注意事项
# If there are multiple solutions, return any subset is fine.

class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset
    """

    def largestDivisibleSubset(self, nums):
        # write your code here
        if len(nums) < 2:
            return nums
        # record the index of the previous divisible number
        prev_index = [-1] * len(nums)

        # record the count of divisible number for number less than/ equal to nums[i]
        counts = [1] * len(nums)

        # sort the array to increasing
        nums.sort()

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and counts[j] + 1 > counts[i]:
                    counts[i] = counts[j] + 1
                    prev_index[i] = j

        # find the element with the most counts
        # then get hte result array with the previous number indicies in a loop
        index = counts.index(max(counts))
        res = []
        while index != -1:
            res.append(nums[index])
            index = prev_index[index]

        return res


sol = Solution()
nums = [1, 2, 3, 4, 5, 6, 7, 8]
sol.largestDivisibleSubset(nums)