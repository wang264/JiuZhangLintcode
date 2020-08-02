# 最大矩阵II · Maximal Square II
# 动态规划
# 描述
# Given a 2D binary matrix filled with 0's and 1's, find the largest square which diagonal is all 1 and others is 0.
#
# Only consider the main diagonal situation.
# 样例
# Example 1:
#
# Input:
# [[1,0,1,0,0],[1,0,0,1,0],[1,1,0,0,1],[1,0,0,1,0]]
# Output:
# 9
# Explanation:
# [0,2]->[2,4]
# Example 2:
#
# Input:
# [[1,0,1,0,1],[1,0,0,1,1],[1,1,1,1,1],[1,0,0,1,0]]
# Output:
# 4
# Explanation:
# [0,2]->[1,3]

# 与436最大正方形相似，我们可以从头开始检查每个1的条目，并获得对角线均为1而其他均为0的矩阵的最大对角线长度。
# 我们用一个数组dp[i][j]代表对角线到此点的最大连续1的长度

# 我们分两种情况考虑
#
# 如果matrix[i][j] == 0，dp[i][j] = 0
# 如果matrix[i][j] == 1，dp[i][j]由其左上角，左边，和上面转移而来
# dp[i][j] = 1 + min {leftZeros[i][j], upZeros[i][j], dp[i - 1][j - 1] }
# left_zeros[i][j] 表示在matrix[i][j]左边连续0的最大数目
# up_zeros[i][j] 表示在matrix[i][j]上面连续0的最大数目
# 很显然，要求一个矩阵斜对角全为1，其余为0的矩阵，除了右下角，那么他的底边肯定全为0，斜边全为1，右侧边全为0，
# 三者长度相同才能保证这个矩阵是满足要求的，那么我们取三者中的最小值，就能保证所选的矩阵是一个满足条件的矩阵
class Solution:
    """
    @param matrix: a matrix of 0 an 1
    @return: an integer
    """

    def maxSquare2(self, matrix):
        if len(matrix) == 0:
            return 0
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        left_zeros = [[0] * num_cols for _ in range(num_rows)]
        up_zeros = [[0] * num_cols for _ in range(num_rows)]

        # 初始化leftZeros和upZeros，统计每个位置的左边和上面有多少连续0
        for i in range(num_rows):
            left_zeros[i][0] = 0  # 第一列左边没有连续的0
        for j in range(num_cols):
            up_zeros[0][j] = 0  # 第一行上面没有连续的0

        for i in range(num_rows):
            for j in range(1, num_cols):
                if matrix[i][j - 1] == 0:
                    left_zeros[i][j] = left_zeros[i][j - 1] + 1
                else:
                    left_zeros[i][j] = 0
        for i in range(1, num_rows):
            for j in range(num_cols):
                if matrix[i - 1][j] == 0:
                    up_zeros[i][j] = up_zeros[i - 1][j] + 1
                else:
                    up_zeros[i][j] = 0

        dp = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
        # 初始化dp数组
        for i in range(num_rows):
            dp[i][0] = matrix[i][0]
        for j in range(num_cols):
            dp[0][j] = matrix[0][j]

        # 状态转移。记录每个点对角线到此点的最大长度。
        for i in range(1, num_rows):
            for j in range(1, num_cols):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(left_zeros[i][j], up_zeros[i][j], dp[i - 1][j - 1]) + 1
        Max = 0
        # 遍历dp查找最大矩阵的对角线长度
        for i in range(num_rows):
            for j in range(num_cols):
                Max = max(Max, dp[i][j])
        # 案就是最长对角线长度的平方
        return Max * Max

sol = Solution()
assert sol.maxSquare2(matrix=[[1,0,1,0,0],[1,0,0,1,0],[1,1,0,0,1],[1,0,0,1,0]]) == 9
assert sol.maxSquare2(matrix=[[1,0,1,0,1],[1,0,0,1,1],[1,1,1,1,1],[1,0,0,1,0]]) == 4