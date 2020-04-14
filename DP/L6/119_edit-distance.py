# 119. Edit Distance
# 中文English
# Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2.
# (each operation is counted as 1 step.)
#
# You have the following 3 operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character
#
# 样例
# Example 1:
# Input:
# "horse"
# "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
#
# Example 2:
# Input:
# "intention"
# "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')

class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """

    # A = word1   B = word2
    # 假设A的长度是m, B的长度是n. 全部操作完成后A的长度也是n， 并且A[n-1]= B[n-1]
    # 于是最优策略（以及所有合法策略）最终都是让A的最后一个字符变成B的最后一个字符。

    # 请况一：增加，在A的最后插入B[n-1]这个字符,  要将A[0...m-1]变成B[0...n-2]
    # 请况二：替换，把A的最后一个字符变成B[n-1]这个字符， 要将A[0...m-2]变成B[0...n-2]
    # 请况三：删除，先把A的最后一个字符删掉，然后再说。 要将A[0...m-2]变成B[0...n-1]
    # 情况四：A[m-1]等于B[n-1],天然相等。要将A[0...m-2]变成B[0...n-２]

    # f[i][j] = A的前i个字符（A[0...i-1])和B的前j个字符（B[0...j-1])的最小编辑距离
    def minDistance(self, word1, word2):
        # write your code here
        m = len(word1)
        n = len(word2)
        A = word1
        B = word2
        f = [[None] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):

                if i == 0 and j == 0:
                    f[i][j] = 0
                    continue
                if i == 0:
                    f[i][j] = j
                    continue
                if j == 0:
                    f[i][j] = i
                    continue
                # 请况一：
                f[i][j] = f[i][j - 1] + 1
                # 请况二：
                f[i][j] = min(f[i][j], f[i - 1][j - 1] + 1)
                # 请况三：
                f[i][j] = min(f[i][j], f[i - 1][j] + 1)
                # 请况四：
                if A[i - 1] == B[j - 1]:
                    f[i][j] = min(f[i][j], f[i - 1][j - 1])

        return f[m][n]


sol = Solution()
word1 = "horse"
word2 = "ros"
sol.minDistance(word1, word2)
