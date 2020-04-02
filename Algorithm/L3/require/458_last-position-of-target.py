# 给一个升序数组，找到 target 最后一次出现的位置，如果没出现过返回 -1
#
# 样例
# 样例 1：
#
# 输入：nums = [1,2,2,4,5,5], target = 2
# 输出：2
# 样例 2：
#
# 输入：nums = [1,2,2,4,5,5], target = 6
# 输出：-1

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if target == nums[0] else -1

        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left+right) // 2
            if nums[mid] == target:
                left = mid
            elif nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid

        if nums[right] == target:
            return right
        elif nums[left] == target:
            return left
        else:
            return -1