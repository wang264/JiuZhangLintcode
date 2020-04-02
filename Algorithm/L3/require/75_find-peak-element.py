# 75.
# 寻找峰值
# 中文English
# 你给出一个整数数组(size为n)，其具有以下特点：
#
# 相邻位置的数字是不同的
# A[0] < A[1] 并且 A[n - 2] > A[n - 1]
# 假定P是峰值的位置则满足A[P] > A[P - 1]
# 且A[P] > A[P + 1]，返回数组中任意一个峰值的位置。
#
# 样例1:
# 输入: [1, 2, 1, 3, 4, 5, 7, 6]
# 输出: 1 or 6
#
# 解释:
# 返回峰顶元素的下标
#
# 样例2:
# 输入: [1, 2, 3, 4, 1]
# 输出: 3
#
# 挑战
# Time complexity O(logN)
#
# 注意事项
# 数组保证至少存在一个峰
# 如果数组存在多个峰，返回其中任意一个就行
# 数组至少包含 3 个数
class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        left = 0
        right = len(A) - 1

        while left+2 < right:  # exist when there are three element
            mid = (left+right) // 2
            if A[mid-1]<A[mid]<A[mid+1]:  # strictly increasing means at least one peak at right
                left = mid
            elif A[mid-1]>A[mid]>A[mid+1]:  # strictly decreasing means at least one peak at left.
                right = mid
            elif A[mid-1]<A[mid]>A[mid+1]: # found a peak
                return mid
            else:  # A[mid-1]>A[mid]<A[mid+1] , we found a bottom, peak at either place
                left = mid
        return left+1