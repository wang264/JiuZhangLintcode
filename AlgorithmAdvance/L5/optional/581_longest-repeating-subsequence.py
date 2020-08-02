# 最长重复子序列 · Longest Repeating Subsequence
# LintCode 版权所有
# 动态规划
# 描述
# Given a string, find length of the longest repeating subsequence such that the two subsequence don’t have same
#  string character at same position, i.e., any ith character in the two subsequences shouldn’t have the same
# index in the original string.
#
# 样例
# Example 1:
#
# Input:"aab"
# Output:1
# Explanation:
# The two subsequence are a(first) and a(second).
# Note that b cannot be considered as part of subsequence as it would be at same index in both.
# Example 2:
#
# Input:"abc"
# Output:0
# Explanation:
# There is no repeating subsequence
# Example 2:
#
# Input:"aabb"
# Output:2
# Explanation:
# There are two subsequence "ab". for example, the first subsequence is s[0]+s[2], the second subsequence
# is s[1] + s[3], so the length of  repeating subsequence is 2.


