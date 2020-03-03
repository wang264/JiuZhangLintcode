class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """

    def letterCombinations(self, digits):
        # write your code here
        if not digits:
            return []

        num_to_chars = {'2': 'abc', '3': 'def',
                        '4': 'ghi', '5': 'jkl',
                        '6': 'mno', '7': 'pqrs',
                        '8': 'tuv', '9': 'wxyz'}
        curr_pos = 0
        curr_path = []
        rslt = []
        self.dfs_helper(digits, curr_pos, curr_path, rslt, num_to_chars)
        return rslt

    def dfs_helper(self, digits, curr_pos, curr_path, rslt, num_to_chars):
        # if curr_pos is not a valid index any more
        if curr_pos > len(digits) - 1:
            rslt.append(''.join(curr_path))
            return

        # if it is a valid index
        if curr_pos <= len(digits) - 1:
            for char in num_to_chars[digits[curr_pos]]:
                curr_path.append(char)
                self.dfs_helper(digits, curr_pos + 1, curr_path, rslt, num_to_chars)
                curr_path.pop()