from collections import deque
import sys


class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """

    def minLength(self, s, dict):
        # write your code here
        # try every possible delete and get the minimum length

        q = deque([s])
        str_have_seen = {s}
        min_len = sys.maxsize

        while q:
            curr_s = q.popleft()
            if len(curr_s) < min_len:
                min_len = len(curr_s)

            successors = self.find_successors(s=curr_s, dict=dict)
            for successor in successors:
                if successor not in str_have_seen:
                    str_have_seen.add(successor)
                    q.append(successor)

        return min_len

    def find_successors(self, s, dict) -> list:
        successors = []
        for sub_s in dict:
            idx = s.find(sub_s)
            while idx != -1:
                successor = s[0:idx] + s[idx + len(sub_s):]
                successors.append(successor)
                idx = s.find(sub_s, idx + 1)
        return successors

# sol = Solution()
# sol.minLength(s="abcabd", dict=["ab","abcd"])