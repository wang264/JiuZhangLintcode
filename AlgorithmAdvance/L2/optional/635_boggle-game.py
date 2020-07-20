

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

    def boggleGame(self, board, words):
        # write your code here
        if board is None or len(board) == 0:
            return []

        trie = Trie()
        for word in words:
            trie.add_word(word)

        rslt_word = list()
        num_rows = len(board)
        num_cols = len(board[0])

        visited_location = set()

        for i in range(num_rows):
            for j in range(num_cols):
                char = board[i][j]
                visited_location.add((i, j))
                self.dfs_search(trie, board, i, j, trie.root.children.get(char), visited_location, rslt_word)
                visited_location.remove((i, j))
        return sorted(rslt_word)

    def valid_location(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])

    def dfs_search(self, trie, board, x, y, node, visited, rslt):
        # this child does not exist, means does not have a word with that char.
        if node is None:
            return

        # we find a word
        if node.is_word:
            rslt.append(node.word)

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
sol.boggleGame(board=["abc","def","ghi"], words=["abc","defi","gh"])
sol.boggleGame(board=["aaaa","aaaa","aaaa","aaaa"], words=["a"])
