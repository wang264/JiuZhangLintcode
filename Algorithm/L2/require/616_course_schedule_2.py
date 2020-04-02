from collections import deque

class Solution:
    # @param {int} numCourses a total of n courses
    # @param {int[][]} prerequisites a list of prerequisite pairs
    # @return {int[]} the course order
    def findOrder(self, numCourses, prerequisites):
        # Write your code here
        directed_edges = {node:[] for node in range(numCourses)}
        node_to_indegree = {node: 0 for node in range(numCourses)}

        for this_course, pre_req_course in prerequisites:
            directed_edges[pre_req_course].append(this_course)
            node_to_indegree[this_course] += 1

        start_node = [node for node in node_to_indegree.keys() if node_to_indegree[node] == 0]
        q = deque(start_node)
        order = []
        
        while q:
            node = q.popleft()
            order.append(node)
            for neighbor in directed_edges[node]:
                node_to_indegree[neighbor] -= 1
                if node_to_indegree[neighbor] == 0:
                    q.append(neighbor)
        
        if len(order) == numCourses:
            return order
        else:
            return []
        