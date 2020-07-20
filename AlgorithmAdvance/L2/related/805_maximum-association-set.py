# 最大关联集合 · Maximum Association Set
# 亚马逊
# Union Find
# 描述
# Amazon sells books, every book has books which are strongly associated with it.Given ListA and ListB,
# indicates that ListA[i] is associated with ListB[i] which represents the book and associated books.
# Output the largest set associated with each other(output in any sort).
# You can assume that there is only one of the largest set.
#
# *The number of books does not exceed `5000`.
# 样例
# Example
# 1:
# Input: ListA = ["abc", "abc", "abc"], ListB = ["bcd", "acd", "def"]
# Output: ["abc", "acd", "bcd", "def"]

# Explanation:
# abc is associated
# with bcd, acd, dfe, so the largest set is the set of all books
#
# Example
# 2:
# Input: ListA = ["a", "b", "d", "e", "f"], ListB = ["b", "c", "e", "g", "g"]
# Output: ["d", "e", "f", "g"]
# Explanation:
# The
# current
# set
# are[a, b, c] and [d, e, g, f], then
# the
# largest
# set is [d, e, g, f]

class Solution:

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_b] = root_a
            self.root_node_to_size[root_a] += self.root_node_to_size[root_b]
            if self.root_node_to_size[root_a] > self.max_size:
                self.max_size = self.root_node_to_size[root_a]
                self.max_size_node = root_a

    def find(self, x):
        root = x
        # if x is root node, directly return it
        if self.father[x] == x:
            return x
        # find the root node
        while self.father[root] != root:
            root = self.father[root]

        # path compression
        while self.father[x] != root:
            temp = self.father[x]
            self.father[x] = root
            x = temp

        return root

    def __init__(self):
        self.father = {}  # each node --->its father.
        self.root_node_to_size = {}  # representation node ---> its set size
        self.max_size = 0  # the maximum size of the cluster
        self.max_size_node = None  # the representation node the cluster with max size

    def maximumAssociationSet(self, ListA, ListB):
        self.father = {}
        self.root_node_to_size = {}  # representation node ---> its set size
        self.max_size = 0  # the maximum size of the cluster
        self.max_size_node = None  # the representation node the cluster with max size

        if ListA is None or len(ListA) == 0:
            return []

        for book in ListA + ListB:
            self.father[book] = book
            self.root_node_to_size[book] = 1

        self.max_size = 1
        self.max_size_node = ListA[0]

        for book_a, book_b in zip(ListA, ListB):
            self.union(book_a, book_b)

        rslt = set()
        for book in ListA + ListB:
            if self.find(book) == self.max_size_node:
                rslt.add(book)

        return sorted(list(rslt))


sol = Solution()
sol.maximumAssociationSet(ListA=["abc", "abc", "abc"], ListB=["bcd", "acd", "def"])

sol.maximumAssociationSet(ListA=["a", "b", "d", "e", "f"], ListB=["b", "c", "e", "g", "g"])
