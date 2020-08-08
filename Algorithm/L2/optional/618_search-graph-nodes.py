# Definition for a undirected graph node


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


def build_graph(input_str: str, values: list) -> list:
    nodes = [UndirectedGraphNode(val) for val in values]
    str_temp = input_str.split('{')[1].split('}')[0]
    strs_to_set_neighbors = str_temp.split('#')
    for the_str in strs_to_set_neighbors:
        node_idx_plus1, *neighbors_idx_plus1 = [int(x) for x in the_str.split(',')]
        for neighbor_idx_plus1 in neighbors_idx_plus1:
            nodes[node_idx_plus1 - 1].neighbors.append(nodes[neighbor_idx_plus1 - 1])

    return nodes

from collections import deque


class Solution:
    # @param {UndirectedGraphNode[]} graph a list of undirected graph node
    # @param {dict} values a dict, <UndirectedGraphNode, (int)value>
    # @param {UndirectedGraphNode} node an Undirected graph node
    # @param {int} target an integer
    # @return {UndirectedGraphNode} a node
    def searchNode(self, graph, values, node, target):
        # Write your code here
        q = deque([node])
        if values[node] == target:
            return node

        del values[node]

        while q:
            head = q.popleft()
            for n in head.neighbors:
                if n in values:
                    if values[n] == target:
                        return n
                    del values[n]
                    q.append(n)
        return None


all_nodes = build_graph(input_str='{1,2,3,4#2,1,3#3,1#4,1,5#5,4}', values=[3, 4, 5, 50, 50])

sol = Solution()

values = dict(zip(all_nodes, [3, 4, 5, 50, 50]))
sol.searchNode(graph=all_nodes[0], values=values, node=all_nodes[0], target=50)
