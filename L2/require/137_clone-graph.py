"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from collections import deque


class Solution:
    def cloneGraph(self, node):
        if node is None:
            return node

        root = node
        # get the nodes from the old graph
        old_nodes = self.get_nodes_bfs(start_node=node)

        # build a mapping from old node to new node
        old_to_new = {}
        for node in old_nodes:
            old_to_new[node] = UndirectedGraphNode(x=node.label)

        # then we fix the neighbors
        for old_node in old_nodes:
            new_node = old_to_new[old_node]
            for old_neighbor in old_node.neighbors:
                new_neighbor = old_to_new[old_neighbor]
                new_node.neighbors.append(new_neighbor)

        return old_to_new[root]

    def get_nodes_bfs(self, start_node) -> set:
        q = deque([start_node])
        nodes = set()
        while q:
            node = q.popleft()
            # add to list if never visit
            if node not in nodes:
                nodes.add(node)
            # append each neighbor to the list if we never visit them before.
            for neighbor in node.neighbors:
                if neighbor not in nodes:
                    q.append(neighbor)

        return nodes
