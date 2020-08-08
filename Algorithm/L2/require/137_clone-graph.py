# 137. Clone Graph
# 中文English
# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
# Nodes are labeled uniquely.
#
# You need to return a deep copied graph, which has the same structure as the original graph, and any
# changes to the new graph will not have any effect on the original graph.
#
# Example
# Example1
#
# Input:
# {1,2,4#2,1,4#4,1,2}
# Output:
# {1,2,4#2,1,4#4,1,2}
# Explanation:
# 1------2
#  \     |
#   \    |
#    \   |
#     \  |
#       4
# Clarification
# How we serialize an undirected graph: http://www.lintcode.com/help/graph/


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


from collections import deque


class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """

    def cloneGraph(self, node):
        # write your code here
        if node is None:
            return None
        begin_node = node
        # build a mapping from old node to new node
        old_node_to_new_node = dict()

        # use bfs to search for all nodes in the old graph and create them
        visited = set()
        visited.add(node)
        q = deque([node])
        while q:
            node = q.popleft()
            old_node_to_new_node[node] = UndirectedGraphNode(node.label)
            for neighbor_node in node.neighbors:
                if neighbor_node in visited:
                    continue
                visited.add(neighbor_node)
                q.append(neighbor_node)

        # fix the neighbors
        for old_node, new_node in old_node_to_new_node.items():
            for neighbor_node in old_node.neighbors:
                new_node.neighbors.append(old_node_to_new_node[neighbor_node])

        return old_node_to_new_node[begin_node]


