# 192. 通配符匹配
# 中文English
# 判断两个可能包含通配符“？”和“*”的字符串是否匹配。匹配规则如下：
#
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
# 两个串完全匹配才算匹配成功。
#
# 样例
# 样例1
#
# 输入:
# "aa"
# "a"
# 输出: false
# 输出2
#
# 输入:
# "aa"
# "aa"
# 输出: true
# 输出3
#
# 输入:
# "aaa"
# "aa"
# 输出: false
# 输出4
#
# 输入:
# "aa"
# "*"
# 输出: true
# 说明: '*' 可以替换任何字符串
# 输出5
#
# 输入:
# "aa"
# "a*"
# 输出: true
# 样例6
#
# 输入:
# "ab"
# "?*"
# 输出: true
# 说明: '?' -> 'a' '*' -> 'b'
# 样例7
#
# 输入:
# "aab"
# "c*a*b"
# 输出: false
# 注意事项
# 1<=|s|, |p| <= 1000
# s仅包含小写英文字母
# p包含小写英文字母，？和 *

class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """

    # 情况一：如果B[n-1]是个正常字符，则如果A[m-1]=B[n-1],能否匹配取决于A[0..m-2]和B[0..n-2]是否匹配。
    # 情况二：如果B[n-1]是'?',则A[m-1]一定是和'?'匹配，之后能否匹配取决于A[0...m-2]和B[0..n-2]是否匹配
    # 情况三：如果B[n-1]是'*',它可以匹配0个或任意多个字符，需要考虑A[m-1]有没有被这个*匹配
    # ---A[m-1]不被*匹配，能否匹配取决于A[0...m-1]和B[0..n-2]是否匹配
    # ---A[m-1]被*匹配，能否匹配取决于A[0...m-2]和B[0..n-1]是否匹配

    # f[i][j] 为A前i个字符A[0..i-1]和B前j个字符B[0..j-1]能否匹配。
    def isMatch(self, s, p):
        # write your code here
        A = s
        B = p
        m = len(A)
        n = len(B)

        f = [[None] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    f[i][j] = True
                    continue
                if j == 0:
                    f[i][j] = False
                    continue

                # here, j>0
                f[i][j] = False
                if B[j - 1] != '*':
                    if i > 0 and (B[j - 1] == '?' or B[j - 1] == A[i - 1]):
                        f[i][j] = f[i - 1][j - 1]
                else:
                    # * represent 0 character
                    f[i][j] = f[i][j - 1]
                    if i > 0:
                        # * represent 1 or more characters
                        f[i][j] = f[i][j] or f[i - 1][j]

        return f[m][n]

sol = Solution()
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
p = "*aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa*"
import time
start_time = time.time()
sol.isMatch(s=s, p=p)
print("--- %s seconds ---" % (time.time() - start_time))
