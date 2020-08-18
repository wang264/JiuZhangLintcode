# 829. Word Pattern II
# 中文English
# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.(i.e if a corresponds to s, then b cannot correspond to s. For example, given pattern = "ab", str = "ss", return false.)
#
# Example
# Example 1
#
# Input:
# pattern = "abab"
# str = "redblueredblue"
# Output: true
# Explanation: "a"->"red","b"->"blue"
# Example 2
#
# Input:
# pattern = "aaaa"
# str = "asdasdasdasd"
# Output: true
# Explanation: "a"->"asd"
# Example 3
#
# Input:
# pattern = "aabb"
# str = "xyzabcxzyabc"
# Output: false
# Notice
# You may assume both pattern and str contains only lowercase letters.

class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """

    def wordPatternMatch(self, pattern, str):
        # write your code here
        if len(pattern) == 0:
            return False
        pattern_to_strs = dict()  # dictionary to store the patterns
        return self.dfs_helper(pattern, 0, str, 0, pattern_to_strs)

    def dfs_helper(self, pattern, start_idx_pattern, str, start_idx_str, pattern_to_strs):
        n = len(pattern)
        if n == start_idx_pattern:
            return True

        pattern_matched = False
        pattern_char = pattern[start_idx_pattern]
        # if we seen this pattern before
        if pattern_char in pattern_to_strs:
            pattern_str_length = len(pattern_to_strs[pattern_char])
            pattern_str = pattern_to_strs[pattern_char]
            # if pattern matched, we continue our search
            if pattern_str == str[start_idx_str:start_idx_str + pattern_str_length]:
                pattern_matched = self.dfs_helper(pattern, start_idx_pattern + 1, str,
                                                  start_idx_str + pattern_str_length,
                                                  pattern_to_strs)
            else:
                # if does not match, stop search and return
                pattern_matched = False
            return pattern_matched

        # we never set this pattern mapping before.
        else:
            # iterate over the ending index of str to try different pattern mapping.
            for end_idx_str in range(start_idx_str, len(str)):
                # different char can NOT map to same substring. ie 'a' maps to 'cde' but 'b' maps to 'cde' as well.
                if str[start_idx_str:end_idx_str + 1] in pattern_to_strs.values():
                    continue
                pattern_to_strs[pattern[start_idx_pattern]] = str[start_idx_str:end_idx_str + 1]
                try_this_pattern_rslt = self.dfs_helper(pattern, start_idx_pattern, str, start_idx_str, pattern_to_strs)
                del pattern_to_strs[pattern[start_idx_pattern]]
                pattern_matched = pattern_matched or try_this_pattern_rslt
                # if we find one answer, we are done searching
                if pattern_matched:
                    return True
            # after all possible search, we check if we find one answer.
            if pattern_matched:
                return True
            else:
                return False


sol = Solution()
sol.wordPatternMatch(pattern="abab", str="redblueredblue") == True

sol.wordPatternMatch(pattern="bdpbibletwuwbvh", str="aaaaaaaaaaaaaaa") == False
