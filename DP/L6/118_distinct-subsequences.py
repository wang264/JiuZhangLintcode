# 118. Distinct Subsequences
# 中文English
# Given two strings S and T. Count the number of distinct subsequences of S which equals T.
#
# A subsequence of a string is a new string which is formed from the original string by deleting some
# (can be none) of the characters without disturbing the relative positions of the remaining characters.
#  (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not)
#
# 样例
# Example 1:
# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation: You could remove any 'b' in S, so there are 3 ways to get T.

# Example 2:
# Input: S = "abcd", T = ""
# Output: 1
# Explanation: There is only 1 way to get T - remove all chars in S.
# 挑战
# Do it in O(n^2) time and O(n) memory.
#
# O(n^2) memory is also acceptable if you do not know how to optimize memory.


class Solution:
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    # A=S
    # B在A中出现多少次，B的每一个字符都要在A中出现。
    def numDistinct(self, S, T):
        # write your code here

        m = len(S)
        n = len(T)
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

        # dp[i][j]= B的前j个字符在A的前i个字符中出现多少次
        # 要看B的最后一个字符，是否和A的最后一个字符，结成对子

        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(0, m + 1):
            for j in range(0, n + 1):
                if j == 0:
                    dp[i][0] = 1
                    continue
                if i == 0:
                    dp[0][j] = 0
                    continue
                # B的尾巴和A的尾巴不相连，那看A的前面的部分和B能组成多少个。-
                dp[i][j] = dp[i - 1][j]
                # B的尾巴和A的尾巴相连，那看A的前面的部分和B前面的部分能组成多少个。
                if S[i - 1] == T[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[m][n]


sol = Solution()
S = "b"
T = "b"
sol.numDistinct(S, T)
