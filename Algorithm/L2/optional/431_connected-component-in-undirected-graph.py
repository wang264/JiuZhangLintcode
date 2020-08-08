# 431. Connected Component in Undirected Graph
# 中文English
# Find connected component in undirected graph.
#
# Each node in the graph contains a label and a list of its neighbors.
#
# (A connected component of an undirected graph is a subgraph in which any two vertices are connected to each other
# by paths, and which is connected to no additional vertices in the supergraph.)
#
# You need return a list of label set.

# 431. 找无向图的连通块
# 中文English
# 找出无向图中所有的连通块。
#
# 图中的每个节点包含一个label属性和一个邻接点的列表。
#
# （一个无向图的连通块是一个子图，其中任意两个顶点通过路径相连，且不与整个图中的其它顶点相连。）
#
# 你需要返回 label 集合的列表.

#
# Example
# Example 1:
#
# Input: {1,2,4#2,1,4#3,5#4,1,2#5,3}
# Output: [[1,2,4],[3,5]]
# Explanation:
#
#   1------2  3
#    \     |  |
#     \    |  |
#      \   |  |
#       \  |  |
#         4   5
# Example 2:
#
# Input: {1,2#2,1}
# Output: [[1,2]]
# Explanation:

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class Solution:
    """
    @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """

    def __init__(self):
        self.father = {}
        self.node_labels = set()

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_b] = root_a

    def find(self, x):
        # if x is root, return directly
        if self.father[x] == x:
            return x

        # try to find the root
        root = x
        while self.father[root] != root:
            root = self.father[root]

        # path compression
        while self.father[x] != root:
            temp = self.father[x]
            self.father[x] = root
            x = temp

        return root

    def connectedSet(self, nodes: list):
        # write your code here
        for node in nodes:
            self.node_labels.add(node.label)
            self.father[node.label] = node.label
        for node in nodes:
            self.node_labels.add(node.label)
            for nb in node.neighbors:
                self.union(node.label, nb.label)

        root_label_to_its_sons = {}
        for label in self.node_labels:
            root_label = self.find(label)
            if root_label not in root_label_to_its_sons:
                root_label_to_its_sons[root_label] = list()
            root_label_to_its_sons[root_label].append(label)

        rslt = []
        for key, val in root_label_to_its_sons.items():
            rslt.append(sorted(val))

        return rslt


# sol = Solution()
# nodes = [UndirectedGraphNode(x) for x in range(1, 6)]
# nodes[0].neighbors = [nodes[1], nodes[3]]
# nodes[1].neighbors = [nodes[0], nodes[3]]
# nodes[3].neighbors = [nodes[0], nodes[1]]

# nodes[2].neighbors = [nodes[4]]
# nodes[4].neighbors = [nodes[2]]

# assert sol.connectedSet(nodes=nodes) == [[1, 2, 4], [3, 5]]