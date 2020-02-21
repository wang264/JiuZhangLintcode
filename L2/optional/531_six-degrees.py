"""
Definition for Undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from collections import deque

class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """
    def sixDegrees(self, graph, s, t):
        # write your code here
        q = deque([s])
        visited = set()
        
        distance = 0
        while q:
            distance+=1
            new_q = deque()
            while q:
                node = q.popleft()
                visited.add(node)
                if node == t:
                    return distance -1
                for neighbor in node.neighbors:
                    if neighbor not in visited:
                        new_q.append(neighbor)
            
            q = new_q
        
        return -1