# 127. Topological Sorting
# 中文English
# Given an directed graph, a topological order of the graph nodes is defined as follow:
#
# For each directed edge A -> B in graph, A must before B in the order list.
# The first node in the order can be any node in the graph with no nodes direct to it.
# Find any topological order for the given graph.
#
# Example
# For graph as follow:
#
# [0 -->1], [0 -->2], [0 -->3], [1 -->4], [2 -->4], [2 -->5], [3 -->4], [3 -->5]
#
# The topological order can be:
#
# [0, 1, 2, 3, 4, 5]
# [0, 2, 3, 1, 5, 4]


# Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


from collections import deque


class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        node_to_indegree = self.get_in_degree(graph)
        start_node = [node for node in graph if node_to_indegree[node] == 0]
        q = deque(start_node)

        top_order = []
        while q:
            node = q.popleft()
            top_order.append(node)
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] -= 1
                if node_to_indegree[neighbor] == 0:
                    q.append(neighbor)
        return top_order

    def get_in_degree(self, graph):
        """
        :param graph: A list of Directed graph node
        :return: A dictionary of key: Directed GraphNode  key: that node's indegree
        """
        node_to_indegree = {key: 0 for key in graph}
        for node in graph:
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] += 1
        return node_to_indegree
