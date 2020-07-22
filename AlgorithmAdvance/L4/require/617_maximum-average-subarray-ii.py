# 617. Maximum Average Subarray II
# 中文English
# Given an array with positive and negative numbers, find the maximum average subarray
# which length should be greater or equal to given length k.
#
# 617. 子数组的最大平均值 II
# 中文English
# 给出一个整数数组，有正有负。找到这样一个子数组，他的长度大于等于 k，且平均值最大。
#
# Example
# Example 1:
#
# Input:
# [1,12,-5,-6,50,3]
# 3
# Output:
# 15.667
# Explanation:
#  (-6 + 50 + 3) / 3 = 15.667
# Example 2:
#
# Input:
# [5]
# 1
# Output:
# 5.000
# Notice
# It's guaranteed that the size of the array is greater or equal to k.

# 如果要求和最大，可以用前缀和数组。但是平均值最大不好求。

# 那么如果最大平均值是T, 那么我们的目标是找到
# - （A[left]+......A[right]/(right - left +1)>=T, 且right - left +1 >= k
# -  把(right-left+1)乘过去 即 (A[left] - T) + .....(A[right - T) >= 0
#
# 换句话说, 对于一个T, 把每个元素A[i]减去T得到B[i]
# 希望找到最大的 B[left] + ....+ B[right] >= 0 , 且right - left +1 >= k
#
# 这可以通过前缀和实现。
# 如果找不到这样的 (left, right) 说明答案小于T--->二分答案。
# 如果找的到这样的 (left, right) 说明答案大于或等于T。
#
#
class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """

    def maxAverage(self, nums, k):
        # the maximum of the average is less than the maximum.
        # the minimum of the average is larger than the minimum
        start = min(nums)
        stop = max(nums)

        while start + 1e-5 < stop:
            mid = (start + stop) / 2  # T=mid
            if self.can_find(nums, k, mid):
                start = mid  # 如果找的到这样的 (left, right) 说明答案大于或等于T。
            else:
                stop = mid  # 如果找不到这样的 (left, right) 说明答案小于T--->二分答案。

        return start

    def can_find(self, nums, k, T):
        # return whether we can find (A[left]+......A[right]/(right - left +1)>=T, and (right - left +1) >= k
        # right_sum: S[j]= B[0]+B[1]+...B[i]+...B[j-1]+B[j]
        # left_sum: S[i] = B[0]+B[1]+...B[i-1]+B[i]
        # min_left_sum: move along with left_sum, record the minimum it have seen so far
        # it will equal to min(S[0], S[1], S[i])

        right_sum, left_sum, min_left_sum = 0, 0, 0

        # for i in range(0, k):
        #     right_sum += nums[i] - T
        right_sum = sum(nums[0:k]) - k * T

        for j in range(k, len(nums) + 1):
            if right_sum - min_left_sum >= 0:
                return True

            if j < len(nums):
                right_sum += nums[j] - T  # B[j]
                left_sum += nums[j - k] - T
                min_left_sum = min(left_sum, min_left_sum)

        return False


sol = Solution()
sol.maxAverage(nums=[1, 12, -5, -6, 50, 3], k=3)
