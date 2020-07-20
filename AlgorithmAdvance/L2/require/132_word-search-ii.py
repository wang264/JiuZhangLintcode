# 132. Word Search II
# 中文English
# Given a matrix of lower alphabets and a dictionary. Find all words in the dictionary that can be found in the
# matrix. A word can start from any position in the matrix and go left/right/up/down to the adjacent position.
# One character only be used once in one word. No same word in dictionary
#

# 132. 单词搜索 II
# 中文English
# 给出一个由小写字母组成的矩阵和一个字典。找出所有同时在字典和矩阵中出现的单词。一个单词可以从矩阵中的任意位置开始，
# 可以向左/右/上/下四个相邻方向移动。一个字母在一个单词中只能被使用一次。且字典中不存在重复单词

# Example
# Example 1:
#
# Input：["doaf","agai","dcan"]，["dog","dad","dgdg","can","again"]
# Output：["again","can","dad","dog"]
# Explanation：
#   d o a f
#   a g a i
#   d c a n
# search in Matrix，so return ["again","can","dad","dog"].
# Example 2:
#
# Input：["a"]，["b"]
# Output：[]
# Explanation：
#  a
# search in Matrix，return [].
# Challenge
# Using trie to implement your algorithm.

DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # 在此节点申请节点
            node = node.children[char]  # 继续遍历
        node.is_word = True
        node.word = word  # 存入单词

    # return the node that contain this word
    def find(self, word):
        node = self.root
        for char in word:
            node = node.children.get(char)
            if node is None:
                return None

        return node

    def search_word(self, word):
        node = self.find(word)
        if node is None:
            return False
        return node.is_word


class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """

    def wordSearchII(self, board, words):
        # write your code here
        if board is None or len(board) == 0:
            return []

        trie = Trie()
        for word in words:
            trie.add_word(word)

        rslt_word = set()
        num_rows = len(board)
        num_cols = len(board[0])

        visited_location = set()

        for i in range(num_rows):
            for j in range(num_cols):
                char = board[i][j]
                visited_location.add((i, j))
                self.dfs_search(trie, board, i, j, trie.root.children.get(char), visited_location, rslt_word)
                visited_location.remove((i, j))
        return list(rslt_word)

    def valid_location(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])

    def dfs_search(self, trie, board, x, y, node, visited, rslt):
        # this child does not exist, means does not have a word with that char.
        if node is None:
            return

        # we find a word
        if node.is_word:
            rslt.add(node.word)

        for dx, dy in DIRECTIONS:
            new_x, new_y = x + dx, y + dy

            # out of the board
            if not self.valid_location(board, new_x, new_y):
                continue
            # we take into account the same character twice
            if (new_x, new_y) in visited:
                continue

            # print(new_x, new_y)
            char = board[new_x][new_y]
            visited.add((new_x, new_y))
            self.dfs_search(trie, board, new_x, new_y, node.children.get(char), visited, rslt)
            visited.remove((new_x, new_y))


sol = Solution()
sol.wordSearchII(board=["abce","sfcs","adee"], words=["as","ab","cf","da","ee","e","adee","eeda"])

assert set(sol.wordSearchII(board=["doaf", "agai", "dcan"], words=["dog", "dad", "dgdg", "can", "again"])) == set(
    ['dad', 'can', 'again', 'dog'])