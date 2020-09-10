# 612. K Closest Points
# 中文English
# Given some points and an origin point in two-dimensional space, find k points which are nearest to the origin.
# Return these points sorted by distance, if they are same in distance, sorted by the x-axis, and if
# they are same in the x-axis, sorted by y-axis.
#
# Example
# Example 1:
#
# Input: points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
# Output: [[1,1],[2,5],[4,4]]
# Example 2:
#
# Input: points = [[0,0],[0,9]], origin = [3, 1], k = 1
# Output: [[0,0]]

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


