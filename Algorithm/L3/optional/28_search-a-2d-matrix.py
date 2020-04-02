# 28.
# 搜索二维矩阵
# 中文English
# 写出一个高效的算法来搜索
# m × n矩阵中的值。
#
# 这个矩阵具有以下特性：
#
# 每行中的整数从左到右是排序的。
# 每行的第一个数大于上一行的最后一个整数。
# 样例
# 样例
# 1:
# 输入: [[5]], 2
# 输出: false
#
# 样例解释:
# 没有包含，返回false。
#
# 样例
# 2:
# 输入:
# [
#     [1, 3, 5, 7],
#     [10, 11, 16, 20],
#     [23, 30, 34, 50]
# ], 3
# 输出: true
#
# 样例解释:
# 包含则返回true。
#
# 挑战
# O(log(n) + log(m))
# 时间复杂度

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        if len(matrix) == 0:
            return False
        row_idx = self.find_correct_row_index(matrix, target)

        return self.element_exist_in_row(matrix, row_idx, target)

    def find_correct_row_index(self, matrix, target):
        # binary search one, find the correct row
        last_col = len(matrix[0]) - 1
        start = 0
        end = len(matrix) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if matrix[mid][last_col] < target:
                start = mid
            elif matrix[mid][last_col] > target:
                end = mid
            else:
                return mid  # hmm, we find that number lol
        if matrix[start][0] <= target <= matrix[start][last_col]:
            return start
        elif matrix[end][0] <= target <= matrix[end][last_col]:
            return end
        else:
            return -1
        # binary search two, find the element in the correct row.

    def element_exist_in_row(self, matrix, row, target):
        if row == -1:
            return False
        start = 0
        end = len(matrix[0]) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if matrix[row][mid] < target:
                start = mid
            elif matrix[row][mid] > target:
                end = mid
            else:
                return True

        if matrix[row][start] == target or matrix[row][end] == target:
            return True
        else:
            return False