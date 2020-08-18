# 425. Letter Combinations of a Phone Number
# 中文English
# Given a digit string excluded 0 and 1, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
#
#
# Example
# Example 1:
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
# Explanation:
# '2' could be 'a', 'b' or 'c'
# '3' could be 'd', 'e' or 'f'
# Example 2:
#
# Input: "5"
# Output: ["j", "k", "l"]
# Notice
# Although the answer above is in lexicographical order, your answer could be in any order you want.

num_to_chars = {'2': 'abc', '3': 'def',
                '4': 'ghi', '5': 'jkl',
                '6': 'mno', '7': 'pqrs',
                '8': 'tuv', '9': 'wxyz'}


class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """

    def letterCombinations(self, digits):
        # write your code here
        if len(digits) == 0:
            return []

        rslt = []
        curr_path = []
        self.dfs_helper(digits, 0, curr_path, rslt)
        return rslt

    def dfs_helper(self, digits, index, curr_path, rslt):
        if index == len(digits):
            rslt.append(''.join(curr_path))
            return
        for char in list(num_to_chars[digits[index]]):
            curr_path.append(char)
            self.dfs_helper(digits, index + 1, curr_path, rslt)
            curr_path.pop()


sol = Solution()
sol.letterCombinations(digits="23")
