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
                self.bfs_helper(s, curr_pos+i, curr_split, rslt)
                curr_split.pop()


# sol = Solution()
# s = '123'
# sol.splitString(s)