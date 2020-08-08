# 120. Word Ladder
# 中文English
# Given two words (start and end), and a dictionary, find the shortest transformation sequence from
#  start to end, output the length of the sequence.
# Transformation rule such that:
#
# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary. (Start and end words do not need to appear in the dictionary )
# Example
# Example 1:
#
# Input：start = "a"，end = "c"，dict =["a","b","c"]
# Output：2
# Explanation：
# "a"->"c"
# Example 2:
#
# Input：start ="hit"，end = "cog"，dict =["hot","dot","dog","lot","log"]
# Output：5
# Explanation：
# "hit"->"hot"->"dot"->"dog"->"cog"
# Notice
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

#
# 120. 单词接龙
# 中文English
# 给出两个单词（start和end）和一个字典，找出从start到end的最短转换序列，输出最短序列的长度。
#
# 变换规则如下：
#
# 每次只能改变一个字母。
# 变换过程中的中间单词必须在字典中出现。(起始单词和结束单词不需要出现在字典中)
# Example
# 样例 1:
#
# 输入：start = "a"，end = "c"，dict =["a","b","c"]
# 输出：2
# 解释：
# "a"->"c"
# 样例 2:
#
# 输入：start ="hit"，end = "cog"，dict =["hot","dot","dog","lot","log"]
# 输出：5
# 解释：
# "hit"->"hot"->"dot"->"dog"->"cog"
# Notice
# 如果不存在这样的转换序列，返回 0。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。


from collections import deque


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """

    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end)
        queue = deque([start])
        visited = set()
        visited.add(start)
        distance = 0

        while queue:
            distance += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == end:
                    return distance

                for next_word in self.get_one_char_change_words(word=word):
                    if next_word not in dict or next_word in visited:
                        continue
                    queue.append(next_word)
                    visited.add(next_word)

    def get_one_char_change_words(self, word):
        # the index that point to the character that need to change.
        words = []
        for idx in range(len(word)):
            left = word[0:idx]
            right = word[idx + 1:]

            for char in "abcdefghijklmnopqrstuvwxyz":
                if char == word[idx]:
                    continue
                words.append(left + char + right)

        return words


sol = Solution()
sol.get_one_char_change_words(word="abc")

assert sol.ladderLength(start="hit", end="cog", dict=set(["hot", "dot", "dog", "lot", "log"])) == 5
