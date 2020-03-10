# 683. Word Break III
# 中文English
# Give a dictionary of words and a sentence with all whitespace removed, return the number of sentences you can form by inserting whitespaces to the sentence so that each word can be found in the dictionary.
#
# Example
# Example1
#
# Input:
# "CatMat"
# ["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
# Output: 3
# Explanation:
# we can form 3 sentences, as follows:
# "CatMat" = "Cat" + "Mat"
# "CatMat" = "Ca" + "tM" + "at"
# "CatMat" = "C" + "at" + "Mat"
# Example1
#
# Input:
# "a"
# []
# Output: 0
# Notice
# Ignore case

class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    # divide problems into sub-problems(first i letters)
    # for each sub-problem, iterate all possible breaking point to break the first i letters into two part
    # if that point to break is j. and j less than i
    # if we can break that string in first j letters, and the right part of the string is in dictionary
    # then we find a way to break first i letters.

    def wordBreak3(self, s, dict):
        # Write your code here
        n = len(s)
        s = ' ' + s.lower()
        dict = set([x.lower() for x in dict])
        # dp[i]=3 means that there are three ways for us to break first i letters using dict
        dp = [0 for _ in range(len(s))]
        dp[0] = 1
        # s=  c   a   t   m   a   t
        #       |   |   |   |   |   |
        # i=    1   2   3   4   5   6
        #   |   |   |   |   |   |   |
        # j=0   1   2   3   4   5
        for i in range(1, n + 1):  # (1, 2, ....n) # divide into sub problems
            for j in range(0, i):  # (0, 1, 2, .... i-1) # find the place that we want to break.
                # if we split the string s into two parts,
                # left---> first j th letters,  right ---> j+1 to end
                if dp[j] > 0:
                    str_new = s[j + 1:i + 1]
                    if str_new in dict:
                        dp[i] = dp[i] + dp[j]

        return dp[n]

#
# sol = Solution()
# s = 'CatMat'
# dic = ["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
# sol.wordBreak3(s, dic)
