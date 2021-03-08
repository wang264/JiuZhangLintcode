# 108. Palindrome Partitioning II
# 中文English
# Given a string s, cut s into some substrings such that every substring is a palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# Example
# Example 1:
#
# Input: "a"
# Output: 0
# Explanation: "a" is already a palindrome, no need to split.
# Example 2:
#
# Input: "aab"
# Output: 1
# Explanation: Split "aab" once, into "aa" and "b", both palindrome.

import sys


class Solution:
    """
    @param s: A string
    @return: An integer
    """

    # f[i] = minimum number of palindrome split from the  first i characters of S---> S[0:i] ( S[0], S[1],...S[n-1] )

    # f[i] = min(f[j] + 1| for all 0<=j<=i-1, condition that S[j:i] is a palindrome.

    def is_palindrome(self, s, start_idx, end_idx):
        if start_idx == end_idx:
            return True

        while start_idx < end_idx:
            if s[start_idx] != s[end_idx]:
                return False
            else:
                start_idx += 1
                end_idx -= 1
        return True

    def minCut_slow(self, s):
        # write your code here
        n = len(s)

        f = [sys.maxsize] * (n + 1)

        f[0] = 0  # 0 palindrome split from the  first i characters of S---> S[0:i] ( S[0], S[1],...S[n-1] )
        for i in range(1, n + 1):
            for j in range(0, i):
                if self.is_palindrome(s, j, i - 1):
                    f[i] = min(f[i], f[j] + 1)

        return f[n] - 1  # in order to split string into k slice, we need to cut k-1 times.

    # use O(n^2) time to pre calculate all possible palindrome
    def calc_palindrome(self, s):
        """
        :param s:
        :return: a list of of list rslt[i][j] means that is s[i:j] is palindrome
        """
        n = len(s)
        palin = [[False] * n for _ in range(n)]

        for mid_point in range(0, n):
            # odd-length
            i = j = mid_point
            while i >= 0 and j < n and s[i] == s[j]:
                palin[i][j] = True
                i -= 1
                j += 1
            # even-length
            i = mid_point - 1
            j = mid_point
            while i >= 0 and j < n and s[i] == s[j]:
                palin[i][j] = True
                i -= 1
                j += 1

        return palin

    def minCut(self, s):
        # write your code here
        n = len(s)
        palin = self.calc_palindrome(s)

        f = [sys.maxsize] * (n + 1)

        f[0] = 0  # 0 palindrome split from the  first i characters of S---> S[0:i] ( S[0], S[1],...S[n-1] )
        #  if i = 5  j = 0,1,2,3,4
        #  0  1  2  3  4
        #              i
        #              j
        for i in range(1, n + 1):
            for j in range(0, i):
                if palin[j][i - 1]:
                    f[i] = min(f[i], f[j] + 1)

        return f[n] - 1  # in order to split string into k slice, we need to cut k-1 times.


sol = Solution()
sol.minCut(s='aab')
