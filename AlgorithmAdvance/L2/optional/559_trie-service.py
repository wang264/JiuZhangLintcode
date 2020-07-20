# 查找树服务 · Trie Service
# LintCode 版权所有
# 字典树
# 描述
# Build tries from a list of <word, freq> pairs. Save top 10 for each node.
# 通过<字符串，值>的集合来建立树结构，每个结点保存前10大的数值。
# 值-->表示该词出项的频率，权重。
#
# 样例
# Example1
#
# Input:
#  <"abc", 2>
#  <"ac", 4>
#  <"ab", 9>
# Output:<a[9,4,2]<b[9,2]<c[2]<>>c[4]<>>>
# Explanation:
# 			Root
#              /
#            a(9,4,2)
#           /    \
#         b(9,2) c(4)
#        /
#      c(2)
# Example2
#
# Input:
# <"a", 10>
# <"c", 41>
# <"b", 50>
# <"abc", 5>
# Output: <a[10,5]<b[5]<c[5]<>>>b[50]<>c[41]<>>

# Definition of TrieNode:
# 维护前10大的数值：
# 在依次插入每个字符的时候，我们依次插入数值到每个结点的top10列表，怎么插入呢？我们从后往前依次遍历，直到寻找到第一个不小于
# frequency的位置，这个位置之后的所有数值相对后移一位，最后插入frequency到这个位置即可。


class TrieNode:
    def __init__(self):
        # <key, value>: <Character, TrieNode>
        self.children = dict()
        self.top10 = []


class TrieService:
    def __init__(self):
        self.root = TrieNode()

    def get_root(self):
        return self.root

    def insert(self, word, frequency):
        node = self.get_root()
        for char in word:
            if char not in node.children:
                # if does not exist
                node.children[char] = TrieNode()

            node = node.children[char]
            # first append to the bottom, then work our way up to exchange any element that is larger than it
            node.top10.append(frequency)
            idx = len(node.top10) - 1
            while idx >= 1 and node.top10[idx - 1] < frequency:
                node.top10[idx] = node.top10[idx - 1]
                idx -= 1
            node.top10[idx] = frequency
            if len(node.top10) > 10:
                node.top10.pop()


ts = TrieService()
ts.insert('abc', 2)
ts.insert('ac', 4)
ts.insert('ab', 9)
print('done')