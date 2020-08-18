# 680. Split String
# 中文English
# Give a string, you can choose to split the string after one character or two adjacent characters, and make the string to be composed of only one character or two characters. Output all possible results.
#
# Example
# Example1
#
# Input: "123"
# Output: [["1","2","3"],["12","3"],["1","23"]]
# Example2
#
# Input: "12345"
# Output: [["1","23","45"],["12","3","45"],["12","34","5"],["1","2","3","45"],["1","2","34","5"],["1","23","4","5"],["12","3","4","5"],["1","2","3","4","5"]]

class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        rslt = []
        curr_pos = 0
        self.bfs_helper(s, curr_pos, [], rslt)
        return rslt

    def bfs_helper(self, s, curr_pos, curr_split, rslt):
        if curr_pos >= len(s):
            rslt.append(curr_split[:])
            return
        # step of 1 char or 2 chars
        for i in range(1, 3):
            if curr_pos + i <= len(s):
                curr_split.append(s[curr_pos:curr_pos + i])
                self.bfs_helper(s, curr_pos + i, curr_split, rslt)
                curr_split.pop()


class Solution2:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        if len(s) == 0:
            return [[]]

        rslt = []
        curr_path = []
        self.dfs_helper(s, start_idx=0, curr_path=curr_path, rslt=rslt)
        return rslt

    def dfs_helper(self, s, start_idx, curr_path, rslt):
        n = len(s)
        if start_idx >= n:
            rslt.append(curr_path[:])
        # one char
        if start_idx < n:
            temp_str = s[start_idx]
            curr_path.append(temp_str)
            self.dfs_helper(s, start_idx + 1, curr_path, rslt)
            curr_path.pop()
        # two chars
        if start_idx < n - 1:
            temp_str = s[start_idx:start_idx + 2]
            curr_path.append(temp_str)
            self.dfs_helper(s, start_idx + 2, curr_path, rslt)
            curr_path.pop()


sol = Solution2()
s = '123'
sol.splitString(s)
