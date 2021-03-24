# 423. Valid Parentheses
# 中文English
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
#
# Example
# Example 1:
#
# Input: "([)]"
# Output: False
# Example 2:
#
# Input: "()[]{}"
# Output: True
# Challenge
# Use O(n) time, n is the number of parentheses.

class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """

    def isValidParentheses(self, s):
        # write your code here
        close_to_open = {")": "(", "]": "[", "}": "{"}
        stack = list()

        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] == close_to_open[char]:
                    stack.pop()
                    continue
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
