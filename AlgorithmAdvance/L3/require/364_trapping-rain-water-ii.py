# 364. Trapping Rain Water II
# 中文English
# Given n x m non-negative integers representing an elevation map 2d where the area of each cell is 1 x 1,
# compute how much water it is able to trap after raining.
# 364. 接雨水 II
# 中文English
# 给出 n * m 个非负整数，代表一张X轴上每个区域为 1 * 1 的 2d 海拔图, 计算这个海拔图最多能接住多少（面积）雨水。
#
#
#
# Example
# Example 1:
#
# Given `5*4` matrix
# Input:
# [[12,13,0,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
# Output:
# 14
# Example 2:
#
# Input:
# [[2,2,2,2],[2,2,3,4],[3,3,3,1],[2,3,4,5]]
# Output:
# 0

# 一个格子高度h,它上面能盛多少水。
#   - 从这个格子检查所有到边界的路径，每条路径 I 都有最大高度值 M_i。
#   - Max(0,所有路径M_i的最小值 - h) 就是答案。（木桶原理）

# 用最小堆维护访问的点，先访问边界一圈的点。
# P 为，从这个点到边界的所有的路径中，每条路径的高度最大值M_i的最小值。
# 　P = Min(M_i)
# 每次从最小堆顶拿出点P， 向其周围4个方向上看未曾访问过的点，如 Q。
#   - 如果 Q 的高度 <= P， 那说明对于 Q 来说， M_i值就是P的高度！因为Q是第一次被访问到。将这个M_i这值加入到Heap中
#   - 如果 Q 的高度 > P ,则说明它不能装水，它的M_i值就是Q的高度，将其加入到Heap中。

import heapq


class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """

    def __init__(self):
        self.visited = set()
        self.P = []
        self.num_rows = None
        self.num_cols = None

    def is_valid(self, x, y):
        return 0 <= x < self.num_rows and 0 <= y < self.num_cols

    def get_not_visited_neighbors(self, x, y):
        adj = []
        for delta_x, delta_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x_ = x + delta_x
            y_ = y + delta_y
            if self.is_valid(x_, y_) and (x_, y_) not in self.visited:
                adj.append((x_, y_))
        return adj

    def initialize(self, heights):
        self.num_rows = len(heights)
        self.num_cols = len(heights[0])
        self.P = []

        # add all location in boards into self.P. for all boarder cells with height h.
        # The amount of rain water it can trap is 0, and it's P is h.
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                # print(i,j)
                if self.valid_and_on_edge(i, j):
                    self.add_to_heap(i, j, heights[i][j])

    def valid_and_on_edge(self, x, y):
        if self.is_valid(x, y):
            return x == 0 or y == 0 or x == self.num_rows - 1 or y == self.num_cols - 1
        else:
            return False

    def add_to_heap(self, x, y, height):
        heapq.heappush(self.P, (height, x, y))
        self.visited.add((x, y))

    def trapRainWater(self, heights):
        if not heights:
            return 0

        self.initialize(heights)

        water = 0
        while len(self.P) != 0:
            p_i_j, x, y = heapq.heappop(self.P)
            for x_, y_ in self.get_not_visited_neighbors(x, y):
                water += max(0, p_i_j - heights[x_][y_])
                self.add_to_heap(x_, y_, max(p_i_j, heights[x_][y_]))

        return water


sol = Solution()
assert sol.trapRainWater(
    heights=[[12, 13, 0, 12], [13, 4, 13, 12], [13, 8, 10, 12], [12, 13, 12, 12], [13, 13, 13, 13]]) == 14
assert sol.trapRainWater(heights=[[2, 2, 2, 2], [2, 2, 3, 4], [3, 3, 3, 1], [2, 3, 4, 5]]) == 0
