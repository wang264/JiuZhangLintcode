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
        for left in range(len(s)):
            # if distinct chat < k, keep increasing right
            while len(char_to_count) < k and right < len(s):
                char_to_count[s[right]] = char_to_count.get(s[right], 0) + 1
                right += 1
            # all the indices after current right is also valid
            if len(char_to_count) == k:
                ans += len(s) - right + 1
            # remove current left for the next possible starting point.
            char_to_count[s[left]] -= 1
            if char_to_count[s[left]] == 0:
                del char_to_count[s[left]]

        return ans

sol = Solution()
sol.kDistinctCharacters("abcabcabcabc", 3)
