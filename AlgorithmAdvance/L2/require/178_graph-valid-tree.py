# 178. Graph Valid Tree
# 中文English
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
# write a function to check whether these edges make up a valid tree.
#
# Example
# Example 1:
#
# Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# Output: true.
# Example 2:
#
# Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
# Output: false.
# Notice
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected,
# [0, 1] is the same as [1, 0] and thus will not appear together in edges.

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    # 形成树的条件
    # n 个点的树要有n-1条边
    # 要形成1个联通块
    def __init__(self):
        self.father = {}
        self.size = 0

    def validTree(self, n, edges):
        # write your code here
        if len(edges) != n - 1:
            return False
        # reset instance variable
        self.father = {}
        self.size = 0

        # initialization
        for i in range(n):
            self.father[i] = i
        self.size = n

        for edge in edges:
            node_a, node_b = edge
            self.union(node_a, node_b)

        return self.query_size()

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.father[root_b] = root_a
            self.size -= 1

    def find(self, x):
        root = x
        # if x is root, return directly
        if self.father[root] == root:
            return root

        # try to find the root
        while self.father[root] != root:
            root = self.father[root]

        # path compression
        while self.father[x] != root:
            temp_x = self.father[x]
            self.father[x] = root
            x = temp_x

        return root

    def query_size(self):
        return self.size == 1


sol = Solution()

assert sol.validTree(n=5, edges=[[0, 1], [0, 2], [0, 3], [1, 4]]) == True
assert sol.validTree(n=5, edges=[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False
