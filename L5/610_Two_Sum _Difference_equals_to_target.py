# 610. Two Sum - Difference equals to target
# 中文English
# Given an array of integers, find two numbers that their difference equals to a target value.
# where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.
#
# 样例
# Example 1:
#
# Input: nums = [2, 7, 15, 24], target = 5
# Output: [1, 2]
# Explanation:
# (7 - 2 = 5)
# Example 2:
#
# Input: nums = [1, 1], target = 0
# Output: [1, 2]
# Explanation:
# (1 - 1 = 0)
# 注意事项

# It's guaranteed there is only one available solution


class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        return self.twoSum7FastSlow(nums, target)

    def twoSum7_hashset(self, nums, target):
        if not nums or len(nums) <= 1:
            return []

        hash_set = {}

        for i in range(len(nums)):
            if nums[i] - target in hash_set:
                return sorted([i+1, hash_set[nums[i] - target] + 1])
            if nums[i] + target in hash_set:
                return sorted([i+1, hash_set[nums[i] + target] + 1])
            else:
                hash_set[nums[i]] = i

        return []

    def twoSum7FastSlow(self, nums, target):
        if not nums or len(nums) < 2:
            return []

        numsWithIndex = [[nums[i], i] for i in range(len(nums))]

        if target < 0:
            target = -target
        numsWithIndex.sort()

        left, right = 0, 1
        while right < len(nums):
            if left == right:
                right += 1

            if numsWithIndex[right][0] - numsWithIndex[left][0] < target:
                right += 1
            elif numsWithIndex[right][0] - numsWithIndex[left][0] > target:
                left += 1
            else:
                return sorted([numsWithIndex[left][1] + 1, numsWithIndex[right][1] + 1])

        return []

sol=Solution()
sol.twoSum7([1,2,4,7,11,15,24], 8)