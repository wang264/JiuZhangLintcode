#
# 585. 山脉序列中的最大值
# 中文English
# 给 n 个整数的山脉数组，即先增后减的序列，找到山顶（最大值）
#
# 样例
# 例1:
#
# 输入: nums = [1, 2, 4, 8, 6, 3]
# 输出: 8
# 例2:
#
# 输入: nums = [10, 9, 8, 7],
# 输出: 10
# 注意事项
# 数组严格递增，严格递减

class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):

        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid+1]:
                right = mid
            elif nums[mid] < nums[mid+1]:
                left = mid
            else:
                raise Exception('can not happen because of monton')

        return max(nums[left:right+1])