# 200. Longest Palindromic Substring
# 中文English
# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000,
# and there exists one unique longest palindromic substring.
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
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        
        longest = ''
        for middle in range(len(s)):
            sub_pali = self.find_palindrom(s,middle,middle)
            if len(sub_pali) > len(longest):
                longest = sub_pali
            
            sub_pali = self.find_palindrom(s,middle,middle+1)
            if len(sub_pali) > len(longest):
                longest = sub_pali
            
        return longest
        
    def find_palindrom(self, s, left, right):
        while left>=0 and right<=len(s)-1 and s[left]==s[right]:
            left-=1 
            right+=1 
        
        # because right now both left and right is one position extreme from the answer
        return s[left+1: right]