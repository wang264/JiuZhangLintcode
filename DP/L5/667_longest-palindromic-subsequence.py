# 667. Longest Palindromic Subsequence
# 中文English
# Given a string s, find the longest palindromic subsequence's length in s.
# You may assume that the maximum length of s is 1000.
#
# 样例
# Example1
#
# Input: "bbbab"
# Output: 4
# Explanation:
# One possible longest palindromic subsequence is "bbbb".可以不连续
# Example2
#
# Input: "bbbbb"
# Output: 5

class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """

    # 要求s[i....j]的最长回文子序列。
    # 情况一： 如果s[i] == s[j]， 那需要知道s[i+1.....j-1]的最长回文字序列， 然后+2即可。
    # 情况二：如果s[i] != s[j],那s[i...j]的最长回文字序列就是s[i+1...j]或者s[i..j-1]的回文子序列的最长一个。

    # f[i][j] = s[i....j]的最长回文子序列的长度。
    def longestPalindromeSubseq(self, s):
        # write your code here
        n = len(s)
        if n ==0:
            return 0

        f = [[None] * n for _ in range(n)]

        # 长度为1的分段最长回文子序列为1
        for i in range(n):
            f[i][i] = 1

        for i in range(n):
            for j in range(n):
                if i > j:
                    f[i][j] = 0  # 不可能的情况，

        # 计算顺序，从分段的从短到长
        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                # 情况一：
                if s[i] == s[j]:
                    f[i][j] = f[i + 1][j - 1] + 2
                # 情况二：
                else:
                    f[i][j] = max(f[i + 1][j], f[i][j - 1])

        return f[0][n - 1]
