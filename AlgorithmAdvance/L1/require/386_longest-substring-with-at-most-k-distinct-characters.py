# Description
# English
# Given a string S, find the length of the longest substring T that contains at most k distinct characters.
#
# Have you met this question in a real interview?
# Example
# Example 1:
#
# Input: S = "eceba" and k = 3
# Output: 4
# Explanation: T = "eceb"
# Example 2:
#
# Input: S = "WORLD" and k = 4
# Output: 4
# Explanation: T = "WORL" or "ORLD"
# Challenge
# O(n) time

# 给定字符串S，找到最多有k个不同字符的最长子串T。
#
# Example
# 样例 1:
#
# 输入: S = "eceba" 并且 k = 3
# 输出: 4
# 解释: T = "eceb"
# 样例 2:
#
# 输入: S = "WORLD" 并且 k = 4
# 输出: 4
# 解释: T = "WORL" 或 "ORLD"
# Challenge
# O(n) 时间复杂度


class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """

    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if k == 0 or len(s) == 0:
            return 0

        char_to_count = {}
        left, right = 0, 0
        n = len(s)
        unique_char_count, ans_length, ans_string = 0, 0, ''
        for left in range(n):
            # 'right pointer' is not out of bound,
            # 1. if unique_char_count <k, we continue our search no matter what.
            # 2. if unique_char_count ==k, we only continue our search, if the new char will not result in the
            # situation that the unique_char_count will be k+1, which mean, we already see this char before.
            while right < n and (unique_char_count < k or (unique_char_count == k and s[right] in char_to_count)):
                char = s[right]
                # we never seen that before
                if char not in char_to_count:
                    unique_char_count += 1
                    char_to_count[char] = 1
                else:
                    char_to_count[char] = char_to_count[char] + 1

                right += 1

            # fixing left, 'right pointer' is pointing to one index to right of the position such that we could have
            # at most k unique chars. if counting the char pointed by 'right pointers' it would be k+1 unique chars
            if right - left > ans_length:
                ans_length = right - left
                ans_string = s[left: right]  # in python, this does not count s[right]

            # prepare to move the 'left pointer' towards to the right.
            char = s[left]
            char_to_count[char] -= 1
            if char_to_count[char] == 0:
                _ = char_to_count.pop(char)
                unique_char_count -= 1

        return ans_length


sol = Solution()
assert sol.lengthOfLongestSubstringKDistinct(s='eceba', k=3) == 4

assert sol.lengthOfLongestSubstringKDistinct(s='zbcaaccdde', k=3) == 7
