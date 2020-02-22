# 159. 寻找旋转排序数组中的最小值
# 中文English
# Suppose a sorted array in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# 样例
# Example 1:
#
# Input：[4, 5, 6, 7, 0, 1, 2]
# Output：0
# Explanation：
# The minimum value in an array is 0.
# Example 2:
#
# Input：[2,1]
# Output：1
# Explanation：
# The minimum value in an array is 1.
# 注意事项
# 你可以假设数组中不存在重复元素。
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """

    def findMin(self, nums):
        # write your code here
        if not nums:
            return -1

        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid

        return min(nums[left], nums[right])

# sol = Solution()
# sol.findMin(nums=[4, 5, 6, 7, 0, 1, 2])