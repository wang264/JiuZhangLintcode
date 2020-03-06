# 544. 前K大数
# 中文English
# 在一个数组中找到前K大的数
#
# 样例
# 样例1
#
# 输入: [3, 10, 1000, -99, 4, 100] 并且 k = 3
# 输出: [1000, 100, 10]
# 样例2
#
# 输入: [8, 7, 6, 5, 4, 3, 2, 1] 并且 k = 5
# 输出: [8, 7, 6, 5, 4]

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

import heapq


class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """

    def kClosest(self, points, origin, k):
        # write your code here
        self.heap = []
        for point in points:
            distance = self.getDistance(point, origin)
            # the head will pop the smallest element, so we push -1*distance,
            # when it pop, it will pop the one with largest distance
            heapq.heappush(self.heap, (-distance, -point.x, -point.y))

            if len(self.heap) > k:
                heapq.heappop(self.heap)

        ret = []
        while len(self.heap) > 0:
            _, x, y = heapq.heappop(self.heap)
            ret.append(Point(-x, -y))
        ret.reverse()
        return ret

    def getDistance(self, a, b):
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2