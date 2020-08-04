# 616. Course Schedule II
# 中文English
# There are a total of n courses you have to take, labeled from 0 to n - 1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
#
# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
#
# Example
# Example 1:
#
# Input: n = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Example 2:
#
# Input: n = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]


from collections import deque


class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """

    def findOrder(self, numCourses, prerequisites):
        # write your code here
        node_to_neighbors = {node: [] for node in range(numCourses)}
        node_to_indegree = {node: 0 for node in range(numCourses)}

        for course, prerequisite in prerequisites:
            node_to_neighbors[prerequisite].append(course)
            node_to_indegree[course] += 1

        start_nodes = [node for node in range(numCourses) if node_to_indegree[node] == 0]
        rslt_seqence = []
        q = deque(start_nodes)
        while q:
            node = q.popleft()
            rslt_seqence.append(node)
            for neighbor in node_to_neighbors[node]:
                node_to_indegree[neighbor] -= 1
                if node_to_indegree[neighbor] == 0:
                    q.append(neighbor)

        if len(rslt_seqence) == numCourses:
            return rslt_seqence
        else:
            return []
