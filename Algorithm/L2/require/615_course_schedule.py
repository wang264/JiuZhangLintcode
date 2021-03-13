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
    """
    @param numCourses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """

    def canFinish(self, numCourses, prerequisites):
        # write your code here
        node_to_indegree = {i: 0 for i in range(numCourses)}
        node_to_neighbors = {i: set() for i in range(numCourses)}

        visited = set()
        for curr_course, prereq_course in prerequisites:
            # contains duplicate edge, need to filter them out.
            if (curr_course, prereq_course) in visited:
                continue
            visited.add((curr_course, prereq_course))
            node_to_indegree[curr_course] += 1
            node_to_neighbors[prereq_course].add(curr_course)

        q = deque([])
        # start with the node with in degree of 0.
        for course, indegree in node_to_indegree.items():
            if indegree == 0:
                q.append(course)

        rslt = []
        while (q):
            for _ in range(len(q)):
                course = q.popleft()
                rslt.append(course)
                for neighbor in node_to_neighbors[course]:
                    node_to_indegree[neighbor] -= 1
                    if node_to_indegree[neighbor] == 0:
                        q.append(neighbor)

        return len(rslt) == numCourses


sol = Solution()
assert sol.canFinish(numCourses=10,
                     prerequisites=[[5, 8], [3, 5], [1, 9], [4, 5], [0, 2], [1, 9], [7, 8], [4, 9]]) == True

assert sol.canFinish(numCourses=2, prerequisites=[[1, 0]]) == True
