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