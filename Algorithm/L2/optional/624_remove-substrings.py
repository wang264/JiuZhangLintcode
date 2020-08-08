# 624. Remove Substrings
# 中文English
# Given a string s and a set of n substrings. You are supposed to remove every instance of those n
# substrings from s so that s is of the minimum length and output this minimum length.
#
# Example
# Example 1:
#
# Input:
# "ccdaabcdbb"
# ["ab","cd"]
# Output:
# 2
# Explanation:
# ccdaabcdbb -> ccdacdbb -> cabb -> cb (length = 2)
# Example 2:
#
# Input:
# "abcabd"
# ["ab","abcd"]
# Output:
# 0
# Explanation:
# abcabd -> abcd -> "" (length = 0)

import sys
from collections import deque


class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """

    def minLength(self, s, dict):
        # write your code here
        visited = set()
        visited.add(s)
        q = deque([s])
        min_len = sys.maxsize
        while q:
            substring = q.popleft()
            if len(substring) < min_len:
                min_len = len(substring)
            for successor in self.find_unvisit_successors(substring, dict):
                if successor not in visited:
                    q.append(successor)
                    visited.add(successor)

        return min_len

    def find_unvisit_successors(self, s, dictionary):
        successors = []
        for word in dictionary:
            idx = s.find(word)
            while idx != -1:
                successors.append(s[:idx] + s[idx + len(word):])
                idx = s.find(word, idx + 1)

        return successors


sol = Solution()
sol.find_unvisit_successors(s='abcdbdcde', dictionary=['cd'])
assert sol.minLength(s="abcabd", dict=["ab", "abcd"]) == 0
assert sol.minLength(s="ccdaabcdbb", dict=["ab", "cd"]) == 2
assert sol.minLength(s="twgbabcfw", dict=["ab", "bc", "gba", "ww", "gf", "tw"]) == 1
