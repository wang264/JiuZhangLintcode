# Description
# 中文
# English
# Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.
#
# You need to support the following method:
#
# connect(a, b), an edge to connect node a and node b
# query(), Returns the number of connected component in the graph
# Have you met this question in a real interview?
# Example
# Example 1:
#
# Input:
# ConnectingGraph3(5)
# query()
# connect(1, 2)
# query()
# connect(2, 4)
# query()
# connect(1, 4)
# query()
#
# Output:[5,4,3,3]


class ConnectingGraph3:
    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """

    def __init__(self, n):
        self.father = {}
        # 连通区域个数
        self.count = n
        for i in range(n + 1):
            self.father[i] = i

    # initialize your data structure here.

    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.count -= 1

    """
    @return: An integer
    """

    def query(self):
        return self.count

    def find(self, x):
        if self.father[x] == x:
            return x

        root = x
        while self.father[root] != root:
            root = self.father[root]

        # path compression
        while x != root:
            temp = self.father[x]
            self.father[x] = root
            x = temp

        return x
