# 107.
# Word Break Given a string s and a dictionary of words dict, determine if s can be
# broken into a space - separated sequence of one or more dictionary words.
#
# 样例
# Example
# 1:
# Input: "lintcode", ["lint", "code"]
# Output: true
#
# Example
# 2:
# Input: "a", ["a"]
# Output: true

# https://zxi.mytechroad.com/blog/leetcode/leetcode-139-word-break/


class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """

    # divide problems into sub-problems(first i letters)
    # for each sub-problem, iterate all possible breaking point to break the first i letters into two part
    # if that point to break is j. and j less than i
    # if we can break that string in first j letters, and the right part of the string is in dictionary
    # then we find a way to break first i letters.
    def wordBreak(self, s, dict):
        n = len(s)
        s = ' ' + s
        # dp[i]=1 means that we can break first i letters using dict
        dp = [False for _ in range(len(s))]
        dp[0] = True
        for i in range(1, n + 1):  # (1, 2, ....n) # divide into sub problems
            for j in range(0, i):  # (0, 1, 2, .... i-1) # find the place that we want to break.
                if dp[j] == 1:
                    str_new = s[j + 1:i + 1]
                    if str_new in dict:
                        dp[i] = True
                        break

        return dp[n]

#
# sol = Solution()
# s = 'lintcode'
# dic = ['lint', 'code']
# sol.wordBreak(s, dic)
