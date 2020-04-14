# 154. 正则表达式匹配
# 中文English
# 实现支持'.'和'*'的正则表达式匹配。
#
# '.'匹配任意一个字母。
# '*'匹配零个或者多个前面的元素。
#
# 匹配应该覆盖整个输入字符串，而不仅仅是一部分。
#
# 需要实现的函数是：bool isMatch(string s, string p)
#
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true （0个或者多个'.' -> 可代表所有的字符串）
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true
#
# 样例

# 样例 1:
# 输入："aa"，"a"
# 输出：false
# 解释：
# 无法匹配

# 样例 2:
# 输入："aa"，"a*"
# 输出：true
# 解释：
# '*' 可以重复 a

class Solution:
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """

    # A=s B=p
    # A的长度是m, B长度是n
    # 最后一步：关注最后的B的字符
    # 正则表达式B中最后的字符B[n-1]对应A中的最后一堆字符。

    # 情况一：如果B[n-1]是一个正常字符，则如果A[m-1]=B[n-1],能否匹配取决于A[0..m-2]和B[0..n-2]能否匹配
    # 情况二：如果B[n-1]是'.'，则A[m-1]一定和'.'匹配，之后能否匹配取决于A[0..m-2]和B[0..n-2]是否匹配。
    # 情况三：如果B[n-1]是'*'，它代表B[n-2]=c可以重复0次或者多次，它们是一个整体c*,需要考虑A[m-1]是0个c，还是多个c中的最后一个
    # ---A[m-1]是0个c,能否匹配取决于A[0..m-1]和B[0..n-3]是否匹配
    # ---A[m-1]是多个c中的最后一个，能否匹配取决于A[0..m-2]和B[0..n-1]是否匹配.这种情况必须A[m-1]=c或者c='.'

    # f[i][j] = A的前i个字符和B的前j个字符能否匹配

    def isMatch(self, s, p):
        # write your code here
        A = s
        B = p
        m = len(A)
        n = len(B)
        f = [[None] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                # 空串和空的正则表达式匹配
                if i == 0 and j == 0:
                    f[i][j] = True
                    continue
                # 空的正则表达式不能匹配长度>0的串
                if j == 0:
                    f[i][j] = False
                    continue

                f[i][j] = False
                # 情况一, 情况二
                if B[j - 1] != '*':
                    if i > 0 and (B[j - 1] == '.' or B[j - 1] == A[i - 1]):
                        f[i][j] = f[i - 1][j - 1]
                else:
                    # c*
                    # 0 c's
                    if j > 1:
                        f[i][j] = f[i][j - 2]
                    # 1c or many c
                    if i > 0 and j > 1 and (B[j - 2] == '.' or B[j - 2] == A[i - 1]):
                        f[i][j] = f[i][j] or f[i - 1][j]
        return f[m][n]


sol =Solution()

s="aa"
p="a*"
sol.isMatch(s,p)