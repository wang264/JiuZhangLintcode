# 401. Kth Smallest Number in Sorted Matrix
# 中文English
# Find the kth smallest number in a row and column sorted matrix.
#
# Each row and each column of the matrix is incremental.
#
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

import heapq


# 用堆解决:
# 定义一个小根堆, 起始仅仅放入第一行第一列的元素.
# 循环k次, 每一次取出一个元素, 然后把该元素右方以及下方的元素放入堆中, 第k
# 次取出的元素即为答案.其中,要注意一个元素不能重复入堆, 需要记录.

class Solution:
    def kthSmallest(self, matrix, k):
        # m rows, n columns
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        if n_rows == 0 or n_cols == 0:
            return None

        # a tuple of (value, row_index, column_index)
        min_heap = []
        heapq.heappush(min_heap, (matrix[0][0], 0, 0))
        visited = {(0, 0)}
        num = None
        for _ in range(k):
            num, i, j = heapq.heappop(min_heap)
            if i + 1 < n_rows and (i + 1, j) not in visited:
                heapq.heappush(min_heap, (matrix[i + 1][j], i + 1, j))
                visited.add((i + 1, j))
            if j + 1 < n_cols and (i, j + 1) not in visited:
                heapq.heappush(min_heap, (matrix[i][j + 1], i, j + 1))
                visited.add((i, j + 1))

        return num


sol = Solution()
assert sol.kthSmallest(matrix=[[1, 5, 7], [3, 7, 8], [4, 8, 9]], k=4) == 5
assert sol.kthSmallest(matrix=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
                       k=1) == 1
