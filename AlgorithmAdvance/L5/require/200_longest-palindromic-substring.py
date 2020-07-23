# 200. Longest Palindromic Substring
# 中文English
# Given a string S, find the longest palindromic substring in S. You may assume that the
# maximum length of S is 1000, and there exists one unique longest palindromic substring.
#
# Example
# Example 1:
#
# Input:"abcdzdcab"
# Output:"cdzdc"
# Example 2:
#
# Input:"aba"
# Output:"aba"
# Challenge
# O(n2) time is acceptable. Can you do it in O(n) time.
class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """

    def longestPalindrome(self, s):
        # write your code here
        # 枚举中点
        if len(s) <=1:
            return s
        max_palindrome = ''
        for i in range(0, len(s) - 1):
            temp_palindrome = self.find_longest_palindrome_from_middle(s, i, i + 1)
            if len(temp_palindrome)>len(max_palindrome):
                max_palindrome = temp_palindrome

            temp_palindrome = self.find_longest_palindrome_from_middle(s, i, i)
            if len(temp_palindrome) > len(max_palindrome):
                max_palindrome = temp_palindrome

        return max_palindrome

    def find_longest_palindrome_from_middle(self, s, start_idx_to_left, start_idx_to_right):
        while start_idx_to_left >= 0 and start_idx_to_right <= len(s) - 1 \
                and s[start_idx_to_left] == s[start_idx_to_right]:
            start_idx_to_left -= 1
            start_idx_to_right += 1
        return s[start_idx_to_left + 1:start_idx_to_right]


sol = Solution()
a = 'aabbacc'
sol.find_longest_palindrome_from_middle(a, 2, 3)
assert sol.longestPalindrome(s='abcdzdcab') == 'cdzdc'
assert sol.longestPalindrome(s='aba') == 'aba'
assert sol.longestPalindrome(s='a') == 'a'
