# 398. Longest Continuous Increasing Subsequence II
# 中文English
# Given an integer matrix. Find the longest increasing continuous subsequence in this matrix
# and return the length of it.
#
# The longest increasing continuous subsequence here can start at any position and go up/down/left/right.
#
# Example
# Example 1:
#
# Input:
#     [
#       [1, 2, 3, 4, 5],
#       [16,17,24,23,6],
#       [15,18,25,22,7],
#       [14,19,20,21,8],
#       [13,12,11,10,9]
#     ]
# Output: 25
# Explanation: 1 -> 2 -> 3 -> 4 -> 5 -> ... -> 25 (Spiral from outside to inside.)
# Example 2:
#
# Input:
#     [
#       [1, 2],
#       [5, 3]
#     ]
# Output: 4
# Explanation: 1 -> 2 -> 3 -> 5
# Challenge
# Assume that it is a N x M matrix. Solve this problem in O(NM) time and memory.

#
# 398. 最长上升连续子序列 II
# 中文English
# 给定一个整数矩阵. 找出矩阵中的最长连续上升子序列, 返回它的长度.
#
# 最长连续上升子序列可以从任意位置开始, 向上/下/左/右移动.
#
# Example
# 样例 1:
#
# 输入:
#     [
#       [1, 2, 3, 4, 5],
#       [16,17,24,23,6],
#       [15,18,25,22,7],
#       [14,19,20,21,8],
#       [13,12,11,10,9]
#     ]
# 输出: 25
# 解释: 1 -> 2 -> 3 -> 4 -> 5 -> ... -> 25 (由外向内螺旋)
# 样例 2:
#
# 输入:
#     [
#       [1, 2],
#       [5, 3]
#     ]
# 输出: 4
# 解释: 1 -> 2 -> 3 -> 5
# Challenge
# 假定这是一个 N x M 的矩阵. 在 O(NM) 的时间复杂度和空间复杂度内解决这个问题.

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


class Solution:
    """
    @param A: An integer matrix
    @return: an integer
    """

    def longestContinuousIncreasingSubsequence2(self, A):
        if len(A) == 0:
            return 0
        num_rows = len(A)
        num_cols = len(A[0])
        memo = {}  # (i,j) ---> length of longest increasing continuous subsequence start from here
        longest = 0
        for i in range(num_rows):
            for j in range(num_cols):
                longest = max(self.dfs(A, i, j, memo), longest)

        return longest

    def is_valid(self, A, x, y):
        return 0 <= x < len(A) and 0 <= y < len(A[0])

    def dfs(self, A, x, y, memo):
        if (x, y) in memo:
            return memo[(x, y)]

        longest_length = 1
        for dx, dy in DIRECTIONS:
            new_x, new_y = dx + x, dy + y
            if self.is_valid(A, new_x, new_y) and A[new_x][new_y] > A[x][y]:
                longest_length = max(longest_length, 1 + self.dfs(A, new_x, new_y, memo))

        return longest_length


sol = Solution()
A = [
    [1, 2, 3, 4, 5],
    [16, 17, 24, 23, 6],
    [15, 18, 25, 22, 7],
    [14, 19, 20, 21, 8],
    [13, 12, 11, 10, 9]
]

sol.longestContinuousIncreasingSubsequence2(A=A)


#
# 使用九章算法强化班，动态规划专题班中讲过的 序列性动态规划
# 我们把二维矩阵打散成为一位数组，数组中每个元素记录二维矩阵中的坐标和高度。 然后把一位数组按照从小到大排序。
# f[i] 表示第 i 个点结束的最长序列的长度，得到公式：
# f[i] = max{f[j] + 1 |  j < i && j 这个点比 i 要低，且i和j两个点相邻}

class Solution_DP:
    """
    @param A: An integer matrix
    @return: an integer
    """

    def longestContinuousIncreasingSubsequence2(self, A):
        if not A or not A[0]:
            return 0

        n, m = len(A), len(A[0])
        points = []
        for i in range(n):
            for j in range(m):
                points.append((A[i][j], i, j))

        points.sort()

        longest_hash = {}
        for i in range(len(points)):
            x, y = points[i][1], points[i][2]
            longest_hash[(x, y)] = 1
            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                if not self.is_valid(A, new_x, new_y):
                    continue
                if (new_x, new_y) in longest_hash and A[new_x][new_y] < points[i][0]:
                    longest_hash[(x, y)] = max(longest_hash[x, y], longest_hash[(new_x, new_y)] + 1)

        return max(longest_hash.values())

    def is_valid(self, A, x, y):
        return 0 <= x < len(A) and 0 <= y < len(A[0])
