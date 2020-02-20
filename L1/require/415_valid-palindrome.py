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