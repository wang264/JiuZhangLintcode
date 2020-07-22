# 510. Maximal Rectangle
# 中文English
# Given a 2D boolean matrix filled with False and True, find the largest rectangle containing all True and return its area.
#
# 510. 最大矩形
# 中文English
# 给你一个二维矩阵，权值为False和True，找到一个最大的矩形，使得里面的值全部为True，输出它的面积


# Example
# Example 1
#
# Input:
# [
#   [1, 1, 0, 0, 1],
#   [0, 1, 0, 0, 1],
#   [0, 0, 1, 1, 1],
#   [0, 0, 1, 1, 1],
#   [0, 0, 0, 0, 1]
# ]
# Output: 6
# Example 2
#
# Input:
# [
#     [0,0],
#     [0,0]
# ]
# Output: 0

# 利用题 122 的直方图算法。
# 枚举每一行为直方图的底部，通过1确定每个柱形的高度。


class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """

    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        max_rectangle = 0
        heights = [0] * len(matrix[0])
        for row in matrix:
            for index, num in enumerate(row):
                heights[index] = heights[index] + 1 if num else 0
            max_rectangle = max(
                max_rectangle,
                self.find_max_rectangle(heights),
            )

        return max_rectangle

    def find_max_rectangle(self, heights):
        indices_stack = []
        max_rectangle = 0
        for index, height in enumerate(heights + [-1]):
            while indices_stack and heights[indices_stack[-1]] >= height:
                popped = indices_stack.pop(-1)
                left_bound = indices_stack[-1] if indices_stack else -1
                max_rectangle = max(
                    max_rectangle,
                    (index - left_bound - 1) * heights[popped],
                )
            indices_stack.append(index)
            print(indices_stack)

        return max_rectangle
