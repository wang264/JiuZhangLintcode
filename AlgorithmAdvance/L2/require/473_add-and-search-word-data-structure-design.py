# 473. Add and Search Word - Data structure design
# 中文English
# Design a data structure that supports the following two operations: addWord(word) and search(word)
#
# search(word) can search a literal word or a regular expression string containing only letters a-z or ..
#
# A . means it can represent any one letter.

# 473. 单词的添加与查找
# 中文English
# 设计一个包含下面两个操作的数据结构：addWord(word), search(word)
#
# addWord(word)会在数据结构中添加一个单词。而search(word)则支持普通的单词查询或是只包含.和a-z的简易正则表达式的查询。
#
# 一个 '.' 可以代表一个任何的字母。

#
# Example
# Example 1:
#
# Input:
#   addWord("a")
#   search(".")
# Output:
#   true
# Example 2:
#
# Input:
#   addWord("bad")
#   addWord("dad")
#   addWord("mad")
#   search("pad")
#   search("bad")
#   search(".ad")
#   search("b..")
# Output:
#   false
#   true
#   true
#   true
# Notice
# You may assume that all words are consist of lowercase letters a-z.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_word = True

    # recursive call
    def find(self, word, idx, curr_node):
        # exit condition
        if idx == len(word):
            return curr_node.is_word
        char = word[idx]
        # if we see the '.' then we need to try to find all possible characters
        if char == '.':
            for ascii_num in range(ord('a'), ord('z')+1):
                this_char = chr(ascii_num)
                if this_char in curr_node.children:
                    if self.find(word, idx+1, curr_node.children[this_char]):
                        return True
            return False
        # normal situation, if we do not have that character in children
        elif char not in curr_node.children:
            return False
        # normal situation, if we have that character in children
        elif char in curr_node.children:
            return self.find(word, idx+1, curr_node.children[char])

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        return self.find(word, idx=0, curr_node=self.root)
# write your code here

sol = WordDictionary()
sol.addWord("a")
sol.search(".")


sol_2 = WordDictionary()
sol_2.addWord("bad")
sol_2.addWord("dad")
sol_2.addWord("mad")
sol_2.search("pad")
sol_2.search("bad")
sol_2.search(".ad")
sol_2.search("b..")



sol_3 = WordDictionary()
sol_3.search(".")
