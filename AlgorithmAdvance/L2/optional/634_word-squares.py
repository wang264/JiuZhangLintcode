# 634. Word Squares
# 中文English
# Given a set of words without duplicates, find all word squares you can build from them.
#
# A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).
#
# For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.
#
# b a l l
# a r e a
# l e a d
# l a d y
# Example
# Example 1:
#
# Input:
# ["area","lead","wall","lady","ball"]
# Output:
# [["wall","area","lead","lady"],["ball","area","lead","lady"]]
#
# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
# Example 2:
#
# Input:
# ["abat","baba","atan","atal"]
# Output:
#  [["baba","abat","baba","atan"],["baba","abat","baba","atal"]]
# Notice
# There are at least 1 and at most 1000 words.
# All words will have the exact same length.
# Word length is at least 1 and at most 5.
# Each word contains only lowercase English alphabet a-z.

#
# 634. 单词矩阵
# 中文English
# 给出一系列 不重复的单词，找出所有用这些单词能构成的 单词矩阵。
# 一个有效的单词矩阵是指, 如果从第 k 行读出来的单词和第 k 列读出来的单词相同(0 <= k < max(numRows, numColumns))，那么就是一个单词矩阵.
# 例如，单词序列为 ["ball","area","lead","lady"] ,构成一个单词矩阵。因为对于每一行和每一列，读出来的单词都是相同的。
#
# b a l l
# a r e a
# l e a d
# l a d y
# Example
# 样例 1:
#
# 输入:
# ["area","lead","wall","lady","ball"]
# 输出:
# [["wall","area","lead","lady"],["ball","area","lead","lady"]]
#
# 解释:
# 输出包含 两个单词矩阵，这两个矩阵的输出的顺序没有影响(只要求矩阵内部有序)。
# 样例 2:
#
# 输入:
# ["abat","baba","atan","atal"]
# 输出:
#  [["baba","abat","baba","atan"],["baba","abat","baba","atal"]]
# Notice
# 现在至少有一个单词并且不多于1000个单词
# 所有的单词都有相同的长度
# 单词的长度最短为 1 最长为 5
# 每一个单词均由小写字母组成

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word_list_this_prefix = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addword(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.word_list_this_prefix.append(word)

        node.is_word = True

    # return the node
    def find(self, word):
        node = self.root
        for char in word:
            node = node.children.get(char)
            if node is None:
                return None

        return node

    def get_words_with_prefix(self, prefix):
        node = self.find(prefix)
        return [] if node is None else node.word_list_this_prefix

    def contains_this_word(self, word):
        node = self.find(word)
        if node is None:
            return False
        else:
            return node.is_word


class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """

    def wordSquares(self, words):
        # write your code here
        trie = Trie()
        for word in words:
            trie.addword(word)

        rslt_squares = []
        for word in words:
            self.search(trie, [word], rslt_squares)
        return rslt_squares

    def search(self, trie, square, rslt_squares):
        n = len(square[0])
        curt_idx = len(square)  # indicate we need to work on the cirt_idx+1 th word next.
        if curt_idx == n:
            rslt_squares.append(list(square))
            return

        # pruning, after the 1st/2nd word.. the 1st/first two character of all other words are defined.
        # we for one of them, there is no word start with that prefix. it is a dead end.
        for row_idx in range(curt_idx, n):
            prefix = ''.join([square[i][row_idx] for i in range(curt_idx)])
            if trie.find(prefix) is None:
                return

        # DFS and backtracking
        prefix = ''.join([square[i][curt_idx] for i in range(curt_idx)])
        for word in trie.get_words_with_prefix(prefix):
            square.append(word)
            self.search(trie, square, rslt_squares)
            square.pop()  # remove the last word


sol = Solution()
assert sol.wordSquares(words=["area", "lead", "wall", "lady", "ball"]) == [["wall","area","lead","lady"],["ball","area","lead","lady"]]

assert sol.wordSquares(words=["abat","baba","atan","atal"]) == [["baba","abat","baba","atan"],["baba","abat","baba","atal"]]
