# 29. Interleaving String
# 中文English
# Given three strings: s1, s2, s3, determine whether s3 is formed by the interleaving of s1 and s2.
#
# 样例
# Example 1:
#
# Input:
# "aabcc"
# "dbbca"
# "aadbbcbcac"
# Output:
# true
#
# Example 2:
# Input:
# ""
# ""
# "1"
# Output:
# false
#
# Example 3:
# Input:
# "aabcc"
# "dbbca"
# "aadbbbaccc"
# Output:
# false
#
# 挑战
# O(n2) time or better

class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """

    # A=s1, B=s2, X=s3
    # f[i][j] = X的前i+j个字符是否为A的前i个字符和B的前j个字符交替组成。
    # A的长度为m, B的长度为n,X的长度是m+n
    # 我们看最后一步，假设X是由A和B交错形成的，那么X的最后一个字符X[m+n-1]有两种情况。
    # 情况一：X的最后一个字符X[m + n - 1] 是由A的最后一个字符A[m-1]组成的，那么
    # X[0.....m+n-2] 则由A[0...m-2] 和 B[0...n-1]交错形成的
    # 情况二：X的最后一个字符X[m + n - 1] 是由的最后一个字符B[n-1]组成的，那么
    # X[0.....m+n-2] 则由A[0...m-1] 和 B[0...n-2]交错形成的
    def isInterleave(self, s1, s2, s3):
        # write your code here
        m = len(s1)
        n = len(s2)
        A = s1
        B = s2
        X = s3
        if m + n != len(X):
            return False
        f = [[None] * (n + 1) for _ in range(m + 1)]

        for i in range(0, m + 1):
            for j in range(0, n + 1):
                # print(f'i:{i} j:{j}')
                if i == 0 and j == 0:
                    f[0][0] = True
                    continue
                f[i][j] = False
                # 情况一
                if i > 0 and X[i + j - 1] == A[i - 1] and f[i - 1][j]:
                    f[i][j] = True
                # 情况二
                if j > 0 and X[i + j - 1] == B[j - 1] and f[i][j - 1]:
                    f[i][j] = True

        return f[m][n]


sol = Solution()
s1 = "abc"
s2 = "a"
s3 = "b"
sol.isInterleave(s1, s2, s3)

sol = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
sol.isInterleave(s1, s2, s3)


class Solution2:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """

    def isInterleave(self, s1, s2, s3):
        # write your code here
        l_1 = len(s1)
        l_2 = len(s2)
        if l_1 + l_2 != len(s3):
            return False

        dp = [[False] * (l_2 + 1) for _ in range(l_1 + 1)]

        for i in range(0, l_1 + 1):
            for j in range(0, l_2 + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                    continue
                if i == 0:
                    dp[0][j] = s2[0:j] == s3[0:j]
                    continue
                if j == 0:
                    dp[i][0] = s1[0:i] == s3[0:i]
                    continue
                if s3[i + j - 1] == s1[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]

                if s3[i + j - 1] == s2[j - 1]:
                    dp[i][j] = dp[i][j] or dp[i][j - 1]

        return dp[l_1][l_2]
