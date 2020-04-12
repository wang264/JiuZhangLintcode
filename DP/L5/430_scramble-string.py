# 430. Scramble String
# 中文English
# Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
#
# Below is one possible representation of s1 = "great":
#
#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
# To scramble the string, we may choose any non-leaf node and swap its two children.
#
# For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".
#
#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
# We say that "rgeat" is a scrambled string of "great".
#
# Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".
#
#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
# We say that "rgtae" is a scrambled string of "great".
#
# Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
#
# 样例
# Example 1:
#
# Input: s1 = "great", s2 = "rgeat"
# Output: true
# Explanation: As described above.
# Example 2:
#
# Input: s1 = "a", s2 = "b"
# Output: false
# 注意事项
# You can start scrambling from any binary tree legally built from s1, but you can not
# rebuild another binary tree while you are scrambling to get s2.


class Solution:
    """
    @param s1: A string
    @param s2: Another string
    @return: whether s2 is a scrambled string of s1
    """

    # convert from S --to----> T
    # 没有优化之前f[i][j][k][h] = 能否从S[i....j] 变换成 T[k...h]

    # 因为两个串的长度都一样，所以子串拿起始位置加上长度表示
    # f[i][j][k] 能否从S[i....i+k] 变换成 T[j...j+k]

    # 枚举两个，1）在哪里劈成两半 2）是否交换左右儿子
    def isScramble(self, s1, s2):
        S = s1
        T = s2
        # write your code here
        m = len(s1)
        n = len(s2)
        if m != n:  # 长度不同就不能换
            return False

        # f[n][n][n+1]
        f = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]

        # length =1
        for i in range(n):
            for j in range(n):
                f[i][j][1] = (S[i] == T[j])

        # 长度从2到N
        for length in range(2, n + 1):
            for i in range(0, n - length + 1):  # s[i.....i+length-1]
                for j in range(0, n - length + 1):  # s[j.....j+length-1]
                    # break into S1 and S2
                    # S1 has length w, S2 have length (length-w)
                    for w in range(1, length):
                        # no swap
                        # S1--->T1 and S2--->T2
                        if f[i][j][w] and f[i + w][j + w][length-w]:
                            f[i][j][length] = True
                            break
                        # swap
                        # S1--->T2 and S2--->T1
                        if f[i][j + length - w][w] and f[i + w][j][length - w]:
                            f[i][j][length] = True
                            break


        return f[0][0][n]
s1 = "rgeat"
s2 = "great"
