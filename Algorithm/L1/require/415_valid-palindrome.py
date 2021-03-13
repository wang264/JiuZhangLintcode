# 415. Valid Palindrome
# 中文English
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Example
# Example 1:
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama"
# Example 2:
#
# Input: "race a car"
# Output: false
# Explanation: "raceacar"
# Challenge
# O(n) time without extra memory.
#
# Notice
# Have you consider that the string might be empty? This is a good question to ask during an interview.
#
# For the purpose of this problem, we define empty string as valid palindrome.

class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """

    def isPalindrome(self, s):
        # write your code here
        if s is None:
            return False
        if len(s) == 0:
            return True

        start = 0
        end = len(s) - 1

        while start < end:
            while start < end and not self.valid_char(s[start]):
                start += 1
            while start < end and not self.valid_char(s[end]):
                end -= 1

            if start < end and s[start].upper() != s[end].upper():
                return False
            else:
                start += 1
                end -= 1

        return True

    def valid_char(self, c):
        if ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9'):
            return True
        else:
            return False


sol = Solution()
assert sol.isPalindrome(",.") == True
assert sol.isPalindrome('1a2') == False


class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """

    def isPalindrome(self, s):
        # write your code here
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and (not (s[left].isalpha() or  s[left].isnumeric())):
                left += 1
            while left < right and (not (s[right].isalpha() or  s[right].isnumeric())):
                right -= 1
            if left < right and s[left].upper() != s[right].upper():
                return False
            else:
                left+=1
                right-=1
        return True



sol = Solution()
sol.isPalindrome(s="ab")
