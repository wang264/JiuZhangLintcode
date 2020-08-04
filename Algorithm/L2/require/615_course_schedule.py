# 615. 课程表
# 中文English
# 现在你总共有 n 门课需要选，记为 0 到 n - 1.
# 一些课程在修之前需要先修另外的一些课程，比如要学习课程 0 你需要先学习课程 1 ，表示为[0,1]
# 给定n门课以及他们的先决条件，判断是否可能完成所有课程？
#
# 样例
# 例1:
#
# 输入: n = 2, prerequisites = [[1,0]]
# 输出: true
# 例2:
#
# 输入: n = 2, prerequisites = [[1,0],[0,1]]
# 输出: false

from collections import deque


class Solution:
    # @param {int} numCourses a total of n courses
    # @param {int[][]} prerequisites a list of prerequisite pairs
    # @return {boolean} true if can finish all courses or false
    def canFinish(self, numCourses, prerequisites):
        directed_edges = {node: [] for node in range(numCourses)}
        node_to_indegree = {node: 0 for node in range(numCourses)}

        for this_course, pre_req_course in prerequisites:
            directed_edges[pre_req_course].append(this_course)
            node_to_indegree[this_course] += 1

        # start with the node with in degree of 0.
        start_nodes = [node for node in node_to_indegree.keys() if node_to_indegree[node] == 0]
        q = deque(start_nodes)
        count = 0

        while q:
            node = q.popleft()
            count += 1
            for neighbor in directed_edges[node]:
                node_to_indegree[neighbor] -= 1
                if node_to_indegree[neighbor] == 0:
                    q.append(neighbor)

        return count == numCourses


sol = Solution()
assert sol.canFinish(numCourses=2, prerequisites=[[1, 0]]) == True
assert sol.canFinish(numCourses=10,
                     prerequisites=[[5, 8], [3, 5], [1, 9], [4, 5], [0, 2], [1, 9], [7, 8], [4, 9]]) == True
