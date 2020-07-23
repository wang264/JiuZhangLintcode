# 512. Decode Ways
# 中文English
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
#
# Example
# Example 1:
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as AB (1 2) or L (12).
# Example 2:
#
# Input: "10"
# Output: 1
# Notice
# 我们不能解码空串，因此若消息为空，你应该返回0。

class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """

    def numDecodings(self, s):
        # dp[i] = number of ways to decode first i numbers.
        # dp[i] = dp[i-1]|condition that s[i-1], the ith' chars is not '0'
        #  + dp[i-2]|condition that the if last two chars convert to numbers are in (10~26)
        if len(s) == 0:
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # 1 ways to decode first 0 numbers
        if s[0] == '0':
            dp[1] = 0
        else:
            dp[1] = 1  # 1 way to decode first 1 numbers.

        for i in range(2, len(s) + 1):
            # decode the last number into char
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            # decode the last two numbers into char
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[n]

sol=Solution()
assert sol.numDecodings('') == 0
assert sol.numDecodings('10') == 1
assert sol.numDecodings('123') == 3