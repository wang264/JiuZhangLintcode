# 138. Subarray Sum
# 中文English
# Given an integer array, find a subarray where the sum of numbers is zero.
# Your code should return the index of the first number and the index of the last number.
#
# Example
# Example 1:
#
# Input:  [-3, 1, 2, -3, 4]
# Output: [0, 2] or [1, 3].
# Explanation: return anyone that the sum is 0.
# Example 2:
#
# Input:  [-3, 1, -4, 2, -3, 4]
# Output: [1,5]
# Notice
# There is at least one subarray that it's sum equals to zero.

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySum_1(self, nums):
        result = []
        # 初始化
        hash = {0: -1}
        sum = 0
        for i, num in enumerate(nums):
            # 累加前缀和
            sum += num
            # 前缀和曾经出现，即这个区间的和为0
            if sum in hash:
                result.append(hash[sum] + 1)
                result.append(i)
                break
            # 前缀和第一次出现，存入hash
            hash[sum] = i
        return result

    def subarraySum(self, nums):
        # write your code here
        subarray_dict = {}
        current_sum = 0
        subarray_dict[0] = -1  # sum of first 0 th element is 0

        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum in subarray_dict:
                rslt = [subarray_dict[current_sum] + 1, i]
                return rslt
            else:
                subarray_dict[current_sum] = i


sol = Solution()
sol.subarraySum([-3, 1, 2, -3, 4])
sol.subarraySum([1, 0, 1])
