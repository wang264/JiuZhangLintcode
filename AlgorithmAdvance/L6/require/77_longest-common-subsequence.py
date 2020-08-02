# 77. Longest Common Subsequence
# 中文English
# Given two strings, find the longest common subsequence(LCS).
#
# Your code should return the length of LCS.
#
# 样例
# Example
# 1: Input: "ABCD" and "EDCA"
# Output: 1
#
# Explanation:
# LCS is 'A' or 'D' or 'C'
#
# Example 2:
# Input: "ABCD" and "EACB"
# Output: 2
#
# Explanation:
# LCS is "AC"
# 说明 What 's the definition of Longest Common Subsequence?
#
# https://en.wikipedia.org / wiki / Longest_common_subsequence_problem
# http://baike.baidu.com / view / 2020307.htm

class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """

    # f[i][j] = A 的前i个字符 A[0...i-1]和B的前j个字符 B[0...j-1]的最长公共子序列的长度
    # 最长公共子序列也是公共子序列：长度是L -> 选定了L个对应的对子
    # 情况一：对子中没有A的第i个字符，A[i-1].那A和B的最长公共子序列就是A的前i-1个字符和B的前j个字序的最长公共子序列。
    # 情况二：对子中没有B的第j个字符，B[j-1].那A和B的最长公共子序列就是A的前i个字符和B的前j-1个字序的最长公共子序列。
    # 情况三：对子中有A的第i个字符 A[i-1] 和 B的第j个字符 B[j-1]. 而且A[i-1] = B[j-1]， 那A和B的最长公共子序列长度
    # 就是A的前i-1个字符和B的前j-1个字序的最长公共子序列的长度加一。
    def longestCommonSubsequence(self, A, B):
        m = len(A)
        n = len(B)
        f = [[None] * (n + 1) for _ in range(m + 1)]

        # 空串和任何串的最长公共子序列的长度都为0
        for i in range(m + 1):
            f[i][0] = 0

        for j in range(n + 1):
            f[0][j] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 情况一,  情况二
                f[i][j] = max(f[i - 1][j], f[i][j - 1])
                if A[i - 1] == B[j - 1]:
                    # 情况三
                    f[i][j] = max(f[i][j], f[i - 1][j - 1] + 1)

        return f[m][n]


sol = Solution()
A = "ABCD"
B = "EACB"
sol.longestCommonSubsequence(A, B)