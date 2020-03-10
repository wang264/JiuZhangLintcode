# 582. Word Break II
# 中文English
# Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
#
# Return all such possible sentences.
#
# Example
# Example 1:
#
# Input："lintcode"，["de","ding","co","code","lint"]
# Output：["lint code", "lint co de"]
# Explanation：
# insert a space is "lint code"，insert two spaces is "lint co de".
# Example 2:
#
# Input："a"，[]
# Output：[]
# Explanation：dict is null.

# using memorization search,
# break each problem into all possible smaller problems,
# them gather the answers

class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """

    def wordBreak(self, s, wordDict):
        # write your code here
        return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, memo):
        # if we solve this problem before
        if s in memo.keys():
            return memo[s]

        ans = []
        # special case, we split the word into 2 part, but one part have length 0
        if s in wordDict:
            ans.append(s)
        # different place to split
        # s= a   p   p   l   e
        #      |   |   |   |
        # i=   1   2   3   4
        for i in range(1, len(s)):
            right_part = s[i:]
            if right_part not in wordDict:
                continue
            left_parts = self.dfs(s[:i], wordDict, memo)
            for l_part in left_parts:
                ans.append(l_part + ' ' + s[i:])

        memo[s] = ans
        return ans

#
# s = 'catsanddog'
# dic = ['cat', 'cats', 'and', 'sand', 'dog']
# sol = Solution()
# sol.wordBreak(s, dic)
#
# sol2 = Solution()
# sol2.wordBreak(s='a', wordDict=[''])
