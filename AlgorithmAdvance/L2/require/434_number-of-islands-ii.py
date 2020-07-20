# 434. Number of Islands II
# 中文English
# Given a n,m which means the row and column of the 2D matrix and an array of pair A( size k). Originally, the 2D
# matrix is all 0 which means there is only sea in the matrix. The list pair has k operator and each operator has
# two integer A[i].x, A[i].y means that you can change the grid matrix[A[i].x][A[i].y] from sea to island.
# Return how many island are there in the matrix after each operator.
#
# 434. 岛屿的个数II
# 中文English
# 给定 n, m, 分别代表一个二维矩阵的行数和列数, 并给定一个大小为 k 的二元数组A. 初始二维矩阵全0. 二元数组A内的k个元素
# 代表k次操作, 设第i个元素为 (A[i].x, A[i].y), 表示把二维矩阵中下标为A[i].x行A[i].y列的元素由海洋变为岛屿.
# 问在每次操作之后, 二维矩阵中岛屿的数量. 你需要返回一个大小为k的数组.

# Example
# Example 1:
#
# Input: n = 4, m = 5, A = [[1,1],[0,1],[3,3],[3,4]]
# Output: [1,1,2,2]
# Explanation:
# 0.  00000
#     00000
#     00000
#     00000
# 1.  00000
#     01000
#     00000
#     00000
# 2.  01000
#     01000
#     00000
#     00000
# 3.  01000
#     01000
#     00000
#     00010
# 4.  01000
#     01000
#     00000
#     00011
# Example 2:
#
# Input: n = 3, m = 3, A = [[0,0],[0,1],[2,2],[2,1]]
# Output: [1,1,2,2]
# Notice
# 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.


# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


# application of union find algorithm in 2 dimension
# we use one cell for each island to represent the whole island
class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """

    def __init__(self):
        self.size = 0
        self.father = {}

    def numIslands2(self, n, m, operators):
        # reset instance variable
        self.size = 0
        self.father = {}
        result = []
        lands_visited = set()

        # iterate each operation
        for operator in operators:
            x, y = operator.x, operator.y
            if not self.is_valid(x, y, n, m):
                continue
            # if the operation is duplicate of the previous, ie. we see this piece of land before
            if (x, y) in lands_visited:
                result.append(self.size)
                continue

            # we first assume we have a new island
            lands_visited.add((x, y))
            self.father[(x, y)] = (x, y)
            self.size += 1
            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                # if we are not out of bound and the adjacent is a land
                if self.is_valid(new_x, new_y, n, m) and (new_x, new_y) in lands_visited:
                    self.union((x, y), (new_x, new_y))

            result.append(self.size)
        return result

    def is_valid(self, x, y, n, m):
        return 0 <= x < n and 0 <= y < m

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        # if we combine 2 island, the total island size need to -1
        if self.father[root_x] != self.father[root_y]:
            self.father[root_x] = root_y
            self.size -= 1

    def find(self, x):
        # if x is the root, directly return it
        if self.father[x] == x:
            return x

        # try to find the root
        root = x
        while self.father[root] != root:
            root = self.father[root]

        # path compression
        while self.father[x] != root:
            temp = self.father[x]
            self.father[x] = root
            x = temp

        return root


sol = Solution()
operators = [[0, 0], [0, 1], [2, 2], [2, 1]]
points = [Point(a, b) for a, b in operators]
assert sol.numIslands2(n=3, m=3, operators=points) == [1, 1, 2, 2]

operators = [[0, 0], [0, 1], [2, 2], [2, 2]]
points = [Point(a, b) for a, b in operators]
assert sol.numIslands2(n=3, m=3, operators=points) == [1, 1, 2, 2]
