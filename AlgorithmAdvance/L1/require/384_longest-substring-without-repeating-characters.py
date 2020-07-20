# Description
# English
# Given a string, find the length of the longest substring without repeating characters.
#
# Example
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The longest substring is "abc".
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The longest substring is "b".
# Challenge
# time complexity O(n)
#
#
# 给定一个字符串，请找出其中无重复字符的最长子字符串。
# 样例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 最长子串是 "abc".
# 样例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 最长子串是 "b".
# Challenge
# O(n) 时间复杂度


class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        # two pointer, 'left_ptr' and 'right_ptr'
        # when left_ptr move towards to the right
        # the right_ptr can not move to the left
        unique_chars = set([])
        n = len(s)
        right_ptr = 0
        longest_length = 0
        for left_ptr in range(n):
            # right_ptr is not out of bound and we did not see s[right_ptr] before
            while right_ptr < n and s[right_ptr] not in unique_chars:
                unique_chars.add(s[right_ptr])
                right_ptr += 1
            # right now, the right_ptr is already point to a bad location.
            longest_length = max(longest_length, right_ptr - left_ptr)
            unique_chars.remove(s[left_ptr])

        return longest_length

sol = Solution()
sol.lengthOfLongestSubstring(s=['a', 'b', 'b', 'a', 'c'])
