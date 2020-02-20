"""
605. 序列重构
中文English
判断是否序列 org 能唯一地由 seqs重构得出. org是一个由从1到n的正整数排列而成的序列，1 ≤ n ≤ 10^4。 重构表示组合成seqs的一个最短的父序列 (意思是，一个最短的序列使得所有 seqs里的序列都是它的子序列).
判断是否有且仅有一个能从 seqs重构出来的序列，并且这个序列是org。

样例
例1:

输入:org = [1,2,3], seqs = [[1,2],[1,3]]
输出: false
解释:
[1,2,3] 并不是唯一可以被重构出的序列，还可以重构出 [1,3,2]
例2:

输入: org = [1,2,3], seqs = [[1,2]]
输出: false
解释:
能重构出的序列只有 [1,2].
例3:

输入: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
输出: true
解释:
序列 [1,2], [1,3], 和 [2,3] 可以唯一重构出 [1,2,3].
例4:

输入:org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
输出:true
"""

from collections import deque


class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """

    def sequenceReconstruction(self, org, seqs):
        # similar to topological sort, but instead at any given time, if the length of q is longer than one,
        # then there exist another topological order.
        order = self.get_order(seqs)

        return order == org

    def get_order(self, seqs) -> list:
        # init graph
        node_to_neighbors = self.build_graph(seqs)
        node_to_indegree = self.get_node_to_indegree_mapping(graph=node_to_neighbors)
        starting_nodes = [node for node in node_to_neighbors.keys() if node_to_indegree[node] == 0]
        order = []
        q = deque(starting_nodes)

        while q:
            if len(q) != 1:
                return []
            node = q.popleft()
            order.append(node)

            for neighbor in node_to_neighbors[node]:
                node_to_indegree[neighbor] -= 1
                if node_to_indegree[neighbor] == 0:
                    q.append(neighbor)

        return order

    def build_graph(self, seqs) -> dict:
        # return a dictionary to represent a graph, with key as the node, and value as it's neighbor that you can visit
        # through the node.
        graph = {}

        # init all the nodes
        for seq in seqs:
            for node in seq:
                if node not in graph:
                    graph[node] = set()

        # init all the neighbors
        for seq in seqs:
            for i in range(0, len(seq)-1):
                node, neighbor_node = seq[i], seq[i+1]
                graph[node].add(neighbor_node)

        return graph


    def get_node_to_indegree_mapping(self, graph):
        # return a dictionary, where key is the node and value is the indegree of each node
        node_to_indegree = {node: 0 for node in graph.keys()}

        for node, neighbors in graph.items():
            for neighbor in neighbors:
                node_to_indegree[neighbor] += 1

        return node_to_indegree


sol = Solution()
sol.sequenceReconstruction(org=[1], seqs=[])