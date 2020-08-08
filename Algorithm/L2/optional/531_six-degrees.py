# 531. Six Degrees
# 中文English
# Six degrees of separation is the theory that everyone and everything is six or fewer steps away,
# by way of introduction, from any other person in the world, so that a chain of "a friend of a friend"
# statements can be made to connect any two people in a maximum of six steps.
#
# Given a friendship relations, find the degrees of two people, return -1 if they can not been
# connected by friends of friends.
#
# Example
# Example1
#
# Input: {1,2,3#2,1,4#3,1,4#4,2,3} and s = 1, t = 4
# Output: 2
# Explanation:
#     1------2-----4
#      \          /
#       \        /
#        \--3--/
# Example2
#
# Input: {1#2,4#3,4#4,2,3} and s = 1, t = 4
# Output: -1
# Explanation:
#     1      2-----4
#                  /
#                /
#               3

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
        queue = deque([s])
        visited = set()
        visited.add(s)
        distance = -1
        while queue:
            distance +=1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == t:
                    return distance
                for neighbor in node.neighbors:
                    if neighbor in visited:
                        continue
                    visited.add(neighbor)
                    queue.append(neighbor)

        return -1


