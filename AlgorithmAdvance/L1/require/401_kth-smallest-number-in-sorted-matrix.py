# Description
# 中文
# English
# Find the kth smallest number in a row and column sorted matrix.
#
# Each row and each column of the matrix is incremental.
#
# Have you met this question in a real interview?
# Example
# Example 1:
#
# Input:
# [
#   [1 ,5 ,7],
#   [3 ,7 ,8],
#   [4 ,8 ,9],
# ]
# k = 4
# Output: 5
# Example 2:
#
# Input:
# [
#   [1, 2],
#   [3, 4]
# ]
# k = 3
# Output: 3
# Challenge
# O*(klogn*) time, n is the maximum of the width and height of the matrix.

# 中文
# 在一个排序矩阵中找从小到大的第 k 个整数。
#
# 排序矩阵的定义为：每一行递增，每一列也递增。
#
# Have you met this question in a real interview?
# Example
# 样例 1:
#
# 输入:
# [
#   [1 ,5 ,7],
#   [3 ,7 ,8],
#   [4 ,8 ,9],
# ]
# k = 4
# 输出: 5
# 样例 2:
#
# 输入:
# [
#   [1, 2],
#   [3, 4]
# ]
# k = 3
# 输出: 3
# Challenge
# 时间复杂度 O(klogn), n 是矩阵的宽度和高度的最大值

import heapq


class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """

    # 用堆解决:
    # 定义一个小根堆, 起始仅仅放入第一行第一列的元素.
    # 循环k次, 每一次取出一个元素, 然后把该元素右方以及下方的元素放入堆中, 第k
    # 次取出的元素即为答案.其中,要注意一个元素不能重复入堆, 需要记录.

    def kthSmallest(self, matrix, k):
        # m rows, n columns
        m = len(matrix)
        if m == 0:
            return None
        n = len(matrix[0])
        if n == 0:
            return None

        # a tuple of (matrix_element, row_number, col_number)
        minheap = []
        heapq.heappush(minheap, (matrix[0][0], 0, 0))
        visited = {(0, 0)}
        num = None
        for _ in range(k):
            num, i, j = heapq.heappop(minheap)
            # print(f'{i}-{j}')
            # search for next row
            if i + 1 < m and (i + 1, j) not in visited:
                heapq.heappush(minheap, (matrix[i + 1][j], i + 1, j))
                visited.add((i + 1, j))
            # search for next column
            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(minheap, (matrix[i][j + 1], i, j + 1))
                visited.add((i, j + 1))

        return num


sol = Solution()
assert sol.kthSmallest(matrix=[[1, 5, 7], [3, 7, 8], [4, 8, 9]], k=4) == 5

assert sol.kthSmallest(matrix=[[1], [2], [3], [100], [101], [1000], [9999]], k=5) == 101
