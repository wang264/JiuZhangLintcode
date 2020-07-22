# 找峰值 II · Find Peak Element II
# 矩阵
# LintCode 版权所有
# 递归
# 二分法
# 描述
# Given an integer matrix A which has the following features :
#
# The numbers in adjacent positions are different.
# The matrix has n rows and m columns.
# For all i < n, A[i][0] < A[i][1] && A[i][m - 2] > A[i][m - 1].
# For all j < m, A[0][j] < A[1][j] && A[n - 2][j] > A[n - 1][j]
# We define a position [i, j] is a peak if:
#
#   A[i][j] > A[i + 1][j] && A[i][j] > A[i - 1][j] &&
#   A[i][j] > A[i][j + 1] && A[i][j] > A[i][j - 1]
# Find a peak element in this matrix. Return the index of the peak.
#
# Guarantee that there is at least one peak, and if there are multiple peaks, return any one of them.
# 样例
# Example 1:
#
# Input:
#     [
#       [1, 2, 3, 6,  5],
#       [16,41,23,22, 6],
#       [15,17,24,21, 7],
#       [14,18,19,20,10],
#       [13,14,11,10, 9]
#     ]
# Output: [1,1]
# Explanation: [2,2] is also acceptable. The element at [1,1] is 41, greater than every element adjacent to it.
# Example 2:
#
# Input:
#     [
#       [1, 5, 3],
#       [4,10, 9],
#       [2, 8, 7]
#     ]
# Output: [1,1]
# Explanation: There is only one peek.
# 挑战
# Solve it in O(n+m) time.
#
# If you come up with an algorithm that you thought it is O(nlogm) or O(mlogn), can you prove it is
# actually O(n+m) or propose a similar but O(n+m) algorithm?

#
# 找峰值 II · Find Peak Element II
# 给定一个整数矩阵 A, 它有如下特性:
#
# 相邻的整数不同
# 矩阵有 n 行 m 列。
# 对于所有的 i < n, 都有 A[i][0] < A[i][1] && A[i][m - 2] > A[i][m - 1]
# 对于所有的 j < m, 都有 A[0][j] < A[1][j] && A[n - 2][j] > A[n - 1][j]
# 我们定义一个位置 [i,j] 是峰值, 当且仅当它满足:
#
#   A[i][j] > A[i + 1][j] && A[i][j] > A[i - 1][j] &&
#   A[i][j] > A[i][j + 1] && A[i][j] > A[i][j - 1]
# 找到该矩阵的一个峰值元素, 返回它的坐标.
#
# 保证至少存在一个峰值, 而如果存在多个峰值, 返回任意一个即可.
# 样例
# 样例 1:
#
# 输入:
#     [
#       [1, 2, 3, 6,  5],
#       [16,41,23,22, 6],
#       [15,17,24,21, 7],
#       [14,18,19,20,10],
#       [13,14,11,10, 9]
#     ]
# 输出: [1,1]
# 解释: [2,2] 也是可以的. [1,1] 的元素是 41, 大于它四周的每一个元素 (2, 16, 23, 17).
# 样例 2:
#
# 输入:
#     [
#       [1, 5, 3],
#       [4,10, 9],
#       [2, 8, 7]
#     ]
# 输出: [1,1]
# 解释: 只有这一个峰值
# 挑战
# O(n+m) 的时间复杂度.
#
# 如果你 认为 你使用了 O(nlogm) 或 O(mlogn) 的算法, 能否证明它的复杂度其实是 O(n+m)?
# 或者想一个类似的算法但是复杂度是O(n+m)？


# 我们对行二分，每次二分时将该行的最大值位置求出来，并与同一列的上下行数值作比较，若比上一行和下一行都大，
# 那么该位置即答案，直接返回，否则移动上下边界，向比它大的的一侧移动（若两侧都比它大，向任意一个移动皆可）。
#
# 这里我们所讲的二分，其实与常规的二分有所不同，因为这里并不存在所谓的数据单调性，
# 这里更像是在找山峰时不断的减小搜索的范围，将搜索的上下边界逼近峰值所在行。

#
# 代码思路
# 设置上边界为0，下边界为N - 1
#
# 在mid找到最大值位置index（在下标为mid这一行的最大的列的下标，有多个最大值返回任意一个均可），
# 若A[mid][index] > A[mid + 1][index]且A[mid][index] > A[mid - 1][index]，则该位置就是峰值，直接返回答案；
# 否则若A[mid][index] < A[mid + 1][index]，那么上边界等于mid，若A[mid][index] 《 A[mid - 1][index]，下边界等于mid
#
# 重复2，直到上下边界距离小于1 比较上下边界所在行的最大值，返回最大值较大的那个位置
#
# 复杂度分析 N 表示行数，M表示列数
# 空间复杂度： O(1)
# 时间复杂度： O(M logN)


class Solution:
    """
    @param: A: An integer matrix
    @return: The index of the peak
    """

    def findPeakII(self, A):
        n = len(A)
        up = 0
        bottom = n - 1
        while up + 1 < bottom:
            mid = (up + bottom) // 2
            max_col_idx_in_row_mid = self.find_max_col(A, search_in_row_idx=mid)

            # 若上一行位置比当前位置值大，则下边界上移
            if A[mid][max_col_idx_in_row_mid] < A[mid - 1][max_col_idx_in_row_mid]:
                bottom = mid
            # 若下一行位置比当前位置值大，则上边界下移
            if A[mid][max_col_idx_in_row_mid] < A[mid + 1][max_col_idx_in_row_mid]:
                up = mid
            # 否则该位置为峰值，直接返回答案
            else:
                return [mid, max_col_idx_in_row_mid]

            # 比较上下边界上最大值，取较大的位置返回答案
            bottom_index = self.find_max_col(A, bottom)
            up_index = self.find_max_col(A, up)
            if A[up][up_index] < A[bottom][bottom_index]:
                return [bottom, bottom_index]
            else:
                return [up, up_index]

    def find_max_col(self, A, search_in_row_idx):
        max_col = 0
        m = len(A[0])
        for j in range(1, m):
            if A[search_in_row_idx][max_col] < A[search_in_row_idx][j]:
                max_col = j

        return max_col


sol = Solution()
A = [
    [1, 2, 3, 6, 5],
    [16, 41, 23, 22, 6],
    [15, 17, 24, 21, 7],
    [14, 18, 19, 20, 10],
    [13, 14, 11, 10, 9]
]
assert sol.findPeakII(A=A) in ([1, 1], [2, 2])
B = [
    [1, 5, 3],
    [4, 10, 9],
    [2, 8, 7]
]

assert sol.findPeakII(A=B) == [1, 1]

