# Implement a Trie with insert, search, and startsWith methods.
#
# Example
# Example 1:
#
# Input:
#   insert("lintcode")
#   search("lint")
#   startsWith("lint")
# Output:
#   false
#   true
# Example 2:
#
# Input:
#   insert("lintcode")
#   search("code")
#   startsWith("lint")
#   startsWith("linterror")
#   insert("linterror")
#   search("lintcode“)
#   startsWith("linterror")
# Output:
#   false
#   true
#   false
#   true
#   true
# Notice
# You may assume that all inputs are consist of lowercase letters a-z.


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    # return the node that has the last character of this word if exist.
    def find(self, word):
        node = self.root
        for char in word:
            node = node.children.get(char)
            if node is None:
                return None
        return node

    """
    @param: word: A string
    @return: if the word is in the trie.
    """

    def search(self, word):
        node = self.find(word)
        if node is None:
            return False

        return node.is_word

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """

    def startsWith(self, prefix):
        return self.find(prefix) is not None

trie = Trie()
trie.search('lintcode')
trie.startsWith("lint")
trie.insert("lint")
trie.startsWith("lint")