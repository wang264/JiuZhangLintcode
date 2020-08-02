# 404. Subarray Sum II
# 中文English
# Given an positive integer array A and an interval. Return the number of subarrays whose sum is in the range of given interval.
#
# Example
# Example 1:
#
# Input: A = [1, 2, 3, 4], start = 1, end = 3
# Output: 4
# Explanation: All possible subarrays: [1](sum = 1), [1, 2](sum = 3), [2](sum = 2), [3](sum = 3).
# Example 2:
#
# Input: A = [1, 2, 3, 4], start = 1, end = 100
# Output: 10
# Explanation: Any subarray is ok.
# Notice
# Subarray is a part of origin array with continuous index and contain at least one number.




# 算法：二分
# 本题要求和在给定区间范围内的子数组数量，那么其实就是要我们求对于每一个右端点，满足条件的左端点个数和。
# 有了上面这个思路，我们就可以设法求出对于一个右端点的满足条件的左端点数量。
#
# 算法思路
# 我们求出数组的前缀和，那么对于一个右端点right，若他的前缀和为x，我们就要求出在[0 : right]中最后一个也就是
# 最大的一个小于等于x - start的位置和第一个也就是最小的一个大于等于x - end的位置。
# 因为均为正整数，所以前缀和数组是单调递增的，可以二分搜索求得位置。
# 求出对于每个右端点，满足条件左端点的数量，将它们累加起来就是满足条件的子数组数量。
#
#
# 代码思路
# 1.计算前缀和数组
# 2.右端点从1开始从左往右遍历
# 3.计算对于每一个右端点right，二分求在前缀和数组pre[0:right]中最后一个一个小于等于pre[right] -  start的位置leftEnd和
# 第一个一个大于等于pre[right] - end的位置leftStart，答案加上leftEnd - leftStart + 1
#
# 4.注意做第3步时，若pre[right] < start或A[right - 1] > end时，即不存在满足条件的子数组，则直接遍历下一个右端点
#
# 复杂度分析
# N表示数组长度
#
# 空间复杂度：
# O(N)
#   - 存前缀和数组
#
# 时间复杂度：
# O(NlogN)
#   - 对于每一个右端点二分需要O(logN)的时间复杂度，一共有N个点

class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """

    def subarraySumII(self, A, start, end):
        # write your code here
        n = len(A)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + A[i]

        count = 0
        for right_idx in range(1, len(prefix_sum)):
            if prefix_sum[right_idx] < start:
                continue
            if A[right_idx - 1] > end:
                continue

            # 二分求第一个一个大于等于prefix_sum[right_idx] - end的位置leftStart
            left_start_idx = self.find_interval_start(prefix_sum, 0, right_idx, target=prefix_sum[right_idx] - end)
            # 二分求最后一个一个小于等于prefix_sum[right_idx] - start的位置leftEnd
            left_end_idx = self.find_interval_end(prefix_sum, 0, right_idx, target=prefix_sum[right_idx] - start)
            num_this_right_end = left_end_idx - left_start_idx + 1

            count += num_this_right_end

        return count

    # find the index of first element larger or equal to 'target'
    def find_interval_start(self, prefix_sum, idx_start, idx_end, target):
        left = idx_start
        right = idx_end
        while left + 1 < right:
            mid = (left + right) // 2
            # if larger, the first answer must be on the left
            if prefix_sum[mid] >= target:
                right = mid
            # if smaller, the answer must be on the right
            else:
                left = mid

        if prefix_sum[left] >= target:
            return left
        elif prefix_sum[right] >= target:
            return right
        else:
            return None

    # find the index of the last element smaller or equal to 'target'
    def find_interval_end(self, prefix_sum, idx_start, idx_end, target):
        left = idx_start
        right = idx_end
        while left + 1 < right:
            mid = (left + right) // 2
            # if smaller, answer is still to the right
            if prefix_sum[mid] <= target:
                left = mid
            # if larger, the answer must be to the left
            else:
                right = mid

        if prefix_sum[right] <= target:
            return right
        elif prefix_sum[left] <= target:
            return left
        else:
            return None


sol = Solution()
sol.subarraySumII(A=[1,2,3,4],start=1,end=3)