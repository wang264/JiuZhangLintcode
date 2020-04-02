class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        hash_set = set()
        
        for c in s:
            if c in hash_set:
                hash_set.remove(c)
            else:
                hash_set.add(c)
        
        #after iterating, the number of elements in hash_set would be the number
        #that appear odd number of times. 
        # we could put one of them in the middle. 
        n = len(hash_set)
        if n > 0:
            return len(s) - n + 1 
        else:
            return len(s) - n