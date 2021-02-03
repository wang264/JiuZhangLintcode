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
        # write your code here
        # dp[i] = number of ways to Decode first i number
        # dp[i] = dp[i-1]|condition that s[i-1], the ith' chars is not '0' + dp[i-2]|condition that the if last two chars convert to numbers are in (10~26)
        if len(s) == 0:
            return 0

        dp = [0] * (len(s) + 1)

        dp[0] = 1  # there are 1 way to decode nothing
        if s[0] == '0':  # we can not decode a single character 0
            dp[1] = 0
        else:
            dp[1] = 1

        for i in range(2, len(s) + 1):
            # decode last number in to char
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]

sol=Solution()
sol.numDecodings('10')
sol.numDecodings('123')
