# 步编辑 · K Edit Distance
# dfs
# Given a set of strings which just has lower case letters and a target string,
# output all the strings for each the edit distance with the target no greater than k.
#
# You have the following 3 operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character
# 样例
# Example 1:
#
# Given words = `["abc", "abd", "abcd", "adc"]` and target = `"ac"`, k = `1`
# Return `["abc", "adc"]`
# Input:
# ["abc", "abd", "abcd", "adc"]
# "ac"
# 1
# Output:
# ["abc","adc"]

# Explanation:
# "abc" remove "b"
# "adc" remove "d"


# Example 2:
# Input:
# ["acc","abcd","ade","abbcd"]
# "abc"
# 2

# Output:
# ["acc","abcd","ade","abbcd"]

# Explanation:
# "acc" turns "c" into "b"
# "abcd" remove "d"
# "ade" turns "d" into "b" turns "e" into "c"
# "abbcd" gets rid of "b" and "d"


class TrieNode:
    def __init__(self):
        # Initialize your data structure here.
        self.children = [None for i in range(26)]
        self.hasWord = False
        self.str = None

    @classmethod
    def addWord(cls, root, word):
        node = root
        for letter in word:
            child = node.children[ord(letter) - ord('a')]
            if child is None:
                child = TrieNode()
                node.children[ord(letter) - ord('a')] = child
            node = child

        node.hasWord = True
        node.str = word


class Solution:
    # @param {string[]} words a set of strings
    # @param {string} target a target string
    # @param {int} k an integer
    # @return {string[]} output all the stirngs that meet the requirements
    def kDistance(self, words, target, k):
        # Write your code here
        root = TrieNode()
        for word in words:
            TrieNode.addWord(root, word)

        result = []
        n = len(target)
        dp = [i for i in range(n + 1)]

        self.find(root, result, k, target, dp)
        return result

    def find(self, node, result, k, target, dp):
        n = len(target)

        if node.hasWord and dp[n] <= k:
            result.append(node.str)

        next = [0 for i in range(n + 1)]

        for i in range(26):
            if node.children[i] is not None:
                next[0] = dp[0] + 1
                for j in range(1, n + 1):
                    if ord(target[j - 1]) - ord('a') == i:
                        next[j] = min(dp[j - 1], min(next[j - 1] + 1, dp[j] + 1))
                    else:
                        next[j] = min(dp[j - 1] + 1, min(next[j - 1] + 1, dp[j] + 1))

                self.find(node.children[i], result, k, target, next)

sol = Solution()
sol.kDistance(["acc","abcd","ade","abbcd"], "abc", 2)
sol.kDistance(["abc", "abd", "abcd", "adc"], "ac", 1)
