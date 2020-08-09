# 460. 在排序数组中找最接近的K个数
# 中文English
# 给一个目标数 target, 一个非负整数 k, 一个按照升序排列的数组 A。在A中找与target最接近的k个整数。返回这k个数并按照与target的接近程度从小到大排序，如果接近程度相当，那么小的数排在前面。
#
# 样例
# 样例 1:
#
# 输入: A = [1, 2, 3], target = 2, k = 3
# 输出: [2, 1, 3]
# 样例 2:
#
# 输入: A = [1, 4, 6, 8], target = 3, k = 3
# 输出: [4, 1, 6]
# 挑战
# O(logn + k) 的时间复杂度
#
# 注意事项
# k是一个非负整数，并且总是小于已排序数组的长度。
# 给定数组的长度是正整数, 不会超过 10^4
# 数组中元素的绝对值不会超过 10^4


class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """

    def kClosestNumbers(self, A, target, k):
        if k == 0 or len(A) == 0:
            return []
        closest_idx = self.find_closest_index(A, target)
        rslt = []
        rslt.append(A[closest_idx])
        left = closest_idx - 1
        right = closest_idx + 1

        # need to find the k-1 additional closest number
        for _ in range(k - 1):
            if left < 0:
                rslt.append(A[right])
                right += 1
                continue
            if right >= len(A):
                rslt.append(A[left])
                left -= 1
                continue

            if self.is_left_closer(A, left, right, target):
                rslt.append(A[left])
                left -= 1
            else:
                rslt.append(A[right])
                right += 1

        return rslt

    def is_left_closer(self, nums, left_idx, right_idx, target):
        left_distance = abs(nums[left_idx] - target)
        right_distance = abs(nums[right_idx] - target)
        if left_distance <= right_distance:
            return True
        else:
            return False

    def find_closest_index(self, nums, target):
        """
        find the closest index from nums compare with target
        """
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                return mid

        if self.is_left_closer(nums, left, right, target):
            return left
        else:
            return right


sol = Solution()
sol.kClosestNumbers(A=[1, 4, 6, 8], target=3, k=3)
