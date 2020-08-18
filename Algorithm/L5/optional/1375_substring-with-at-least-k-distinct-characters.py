# 1375. Substring With At Least K Distinct Characters
# 中文English
# Given a string S with only lowercase characters.
#
# Return the number of substrings that contains at least k distinct characters.
#
# Example
# Example 1:
#
# Input: S = "abcabcabca", k = 4
# Output: 0
# Explanation: There are only three distinct characters in the string.
# Example 2:
#
# Input: S = "abcabcabcabc", k = 3
# Output: 55
# Explanation: Any substring whose length is not smaller than 3 contains a, b, c.
#     For example, there are 10 substrings whose length are 3, "abc", "bca", "cab" ... "abc"
#     There are 9 substrings whose length are 4, "abca", "bcab", "cabc" ... "cabc"
#     ...
#     There is 1 substring whose length is 12, "abcabcabcabc"
#     So the answer is 1 + 2 + ... + 10 = 55.
# Notice
# 1. 10 ≤ length(S) ≤ 1,000,000
# 2. 1 ≤ k ≤ 26


class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """

    def kDistinctCharacters(self, s, k):
        ans = 0
        char_to_count = {}
        right = 0
        # like sliding window
        # all valid_substring = (total number of substrings that contains at least k distinct character)
        # all_valid_substrings = substrings start at index 0, index 1, ...index n-1
        for left in range(len(s)):
            # if distinct chat < k, keep increasing right
            while len(char_to_count) < k and right < len(s):
                char_to_count[s[right]] = char_to_count.get(s[right], 0) + 1
                right += 1
            # all the indices after current right is also valid
            # we need the if statement here because we might end up exit the while loop because we are
            # done iterating but dont have k distinct character yet.
            if len(char_to_count) == k:
                ans += len(s) - right + 1
            # remove current left for the next possible starting point.
            char_to_count[s[left]] -= 1
            if char_to_count[s[left]] == 0:
                del char_to_count[s[left]]

        return ans



sol = Solution()
assert sol.kDistinctCharacters("abcabcabcabc", 3) == 55
