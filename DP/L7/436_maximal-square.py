# 436. 最大正方形
# 中文English
# 在一个二维01矩阵中找到全为1的最大正方形, 返回它的面积.
#
# 样例
# 样例 1:
#
# 输入:
# [
#   [1, 0, 1, 0, 0],
#   [1, 0, 1, 1, 1],
#   [1, 1, 1, 1, 1],
#   [1, 0, 0, 1, 0]
# ]
# 输出: 4
# 样例 2:
#
# 输入:
# [
#   [0, 0, 0],
#   [1, 1, 1]
# ]
# 输出: 1


class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """

    # f[i][j] = 以i,j为右下角的全一正方形的最大边长
    def maxSquare(self, matrix):
        # write your code here
        A = matrix
        if A is None or len(A) == 0 or len(A[0]) == 0:
            return 0
        m = len(A)
        n = len(A[0])
        f = [[0] * n for _ in range(m)]
        rslt = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    f[i][j] = 0
                    continue
                f[i][j] = 1
                if i >= 1 and j >= 1:
                    f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1

                rslt = max(rslt, f[i][j] ** 2)

        return rslt
