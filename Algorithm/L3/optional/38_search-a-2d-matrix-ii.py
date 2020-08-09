# 38. Search a 2D Matrix II
# 中文English
# Write an efficient algorithm that searches for a value in an m x n matrix, return the occurrence of it.
#
# This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# Integers in each column are sorted from up to bottom.
# No duplicate integers in each row or column.
# Example
# Example 1:
#
# Input:
# 	[[3,4]]
# 	target=3
# Output:1
# Example 2:
#
# Input:
#     [
#       [1, 3, 5, 7],
#       [2, 4, 7, 8],
#       [3, 5, 9, 10]
#     ]
#     target = 3
# Output:2
# Challenge
# O(m+n) time and O(1) extra space


class Solution2:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """

    # 从左下角开始，往右上角逼近
    def searchMatrix(self, matrix, target):
        if matrix == [] or matrix[0] == []:
            return 0

        row, column = len(matrix), len(matrix[0])
        i, j = row - 1, 0
        count = 0
        while i >= 0 and j < column:
            if matrix[i][j] == target:
                count += 1
                i -= 1
                j += 1
            elif matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
        return count


class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        # start from top right corner
        i = 0
        j = num_cols - 1

        count = 0
        while i < num_rows and j >= 0:
            # the other answers can not be in the same row and same column
            if matrix[i][j] == target:
                i += 1
                j -= 1
                count += 1
            # if matrix[i][j] is less than target, matrix[i][0] < matrix[i][1]< ...matrix[i][j]<target
            # so we search for the next row
            elif matrix[i][j] < target:
                i += 1
            # if matrix[i][j] is larger than target, target<matrix[i][j] < matrix[i+1][j]< ...matrix[num_rows-1][j]
            # so we search for the previous column
            elif matrix[i][j] > target:
                j -= 1

        return count


sol = Solution()
matrix = [[1, 3, 5, 7],
          [2, 4, 7, 8],
          [3, 5, 9, 10]]
sol.searchMatrix(matrix,3)
