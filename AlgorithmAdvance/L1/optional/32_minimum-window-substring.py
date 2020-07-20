# Description
# English
# Given two strings 'source' and 'target'. Return the minimum substring of source which contains each char of 'target'.
#
# 1. If there is no answer, return "".
# 2. You are guaranteed that the answer is unique.
# 3. 'target' may contain duplicate char, while the answer need to contain at least the same number of that char.
#
# Example
# Example 1:
#
# Input: source = "abc", target = "ac"
# Output: "abc"
# Example 2:
#
# Input: source = "adobecodebanc", target = "abc"
# Output: "banc"
# Explanation: "banc" is the minimum substring of source string which contains each char of target "abc".
# Example 3:
#
# Input: source = "abc", target = "aa"
# Output: ""
# Explanation: No substring contains two 'a'.
# Challenge
# O(n) time

# 中文
# 给定两个字符串 source 和 target. 求 source 中最短的包含 target 中每一个字符的子串.
#
# 1.如果没有答案, 返回 "".
# 2.保证答案是唯一的.
# 3.target 可能包含重复的字符, 而你的答案需要包含至少相同数量的该字符.
# Example
# 样例 1:
#
# 输入: source = "abc", target = "ac"
# 输出: "abc"
# 样例 2:
#
# 输入: source = "adobecodebanc", target = "abc"
# 输出: "banc"
# 解释: "banc" 是 source 的包含 target 的每一个字符的最短的子串.
# 样例 3:
#
# 输入: source = "abc", target = "aa"
# 输出: ""
# 解释: 没有子串包含两个 'a'.
# Challenge
# O(n) 时间复杂度

class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """

    def minWindow(self, source, target):
        # write your code here
        if source is None:
            return ""

        # init
        # maps of 'char'---> # of appear
        target_dic, source_dic = self.calc_target_dic(target=target), {}

        # source_unique_char_len keeps tracks of the number of character we need to collect.
        target_unique_char_len, source_unique_char_len = len(target_dic), 0
        left, right = 0, 0
        n = len(source)
        min_ans_len = n + 1
        ans = ''

        for left in range(n):
            # 还没到头而且还没集齐。。right要继续走。
            while right < n and source_unique_char_len < target_unique_char_len:
                curr_char = source[right]
                # 这个字母我们要计数
                if curr_char in target_dic:
                    source_dic[curr_char] = source_dic.get(curr_char, 0) + 1
                    # 如果我们集齐了这个字母
                    if source_dic[curr_char] == target_dic[curr_char]:
                        source_unique_char_len += 1
                # 继续往右
                right += 1

            # 集齐了所有字母了。
            # right 指向的是如果不变left,第一个符合条件的字母的右边一个位置。
            if right - left < min_ans_len and source_unique_char_len == target_unique_char_len:
                min_ans_len = right - left
                ans = source[left:right]  # in python this will not include source[right]

            # get ready, the left pointer will be move towards to the right.
            curr_char = source[left]
            if curr_char in target_dic:  # if we care about this charcter
                # 如果因为有这个字母让我们集齐了这个字母需要的次数。
                if target_dic[curr_char] == source_dic[curr_char]:
                    source_unique_char_len -= 1
                source_dic[curr_char] -= 1

        return ans

    def calc_target_dic(self, target):
        dic = {}
        for char in target:
            dic[char] = dic.get(char, 0) + 1

        return dic


sol = Solution()
assert sol.minWindow(source='adobecodebanc', target='abc') == 'banc'
