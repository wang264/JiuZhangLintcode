# 676. 解码方式 II
# 中文English
# 使用以下映射方式将 A-Z 的消息编码为数字:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 除此之外, 编码的字符串也可以包含字符 *, 它代表了 1 到 9 的数字中的其中一个.给出包含数字和字符 * 的编码消息,
# 返回所有解码方式的数量. 因为结果可能很大, 所以结果需要对 10^9 + 7 取模
#
# 样例
# 样例1
#
# 输入: "*"
# 输出: 9
# 说明: 你可以译码为 "A", "B", "C", "D", "E", "F", "G", "H", "I".
# 样例2
#
# 输入: "1*"
# 输出: 18
# 注意事项
# 输入的字符串在范围 [1, 10^5] 内.
# 输入的字符串只能包含字符 * 和数字 0 - 9.
class Solution:
    """
    @param s: a message being encoded
    @return: an integer
    """

    def numDecodings(self, s):
        # write your code here
        if s is None or s == "" or s[0] == 0:
            return 0
        mod = 1000000007
        n = len(s)
        # dp is how many ways the first i characters
        dp = [1]
        for i in range(1, len(s) + 1):
            count1 = (dp[i - 1] * self.cnt1(s[i - 1])) % mod
            count2 = 0
            if i > 1:
                count2 = (dp[i - 2] * self.cnt2(s[i - 2], s[i - 1])) % mod
            dp.append((count1 + count2) % mod)
        return dp[-1]

    def cnt1(self, ch):
        if ch == '0':
            return 0
        if ch == "*":
            return 9
        else:
            # ch: 1 - 9
            return 1

    def cnt2(self, ch1, ch2):
        if ch1 == '0':
            return 0

        if ch1 == '1':
            if ch2 == '*':
                return 9
            else:
                # ch2: 1-9
                return 1

        if ch1 == '2':
            if ch2 == '*':
                return 9
            if 0 <= int(ch2) <= 6:
                return 1
            else:
                return 0

        if '2' < ch1:
            return 0

            # now ch1 == '*'
        if ch2 == '*':
            return 15
        if 0 <= int(ch2) <= 6:
            return 2
        else:
            return 1
