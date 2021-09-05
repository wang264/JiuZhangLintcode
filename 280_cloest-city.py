# 280 Closest City
#
# There are many cities on a two-dimensional plane, all cities have their own names c[i]c[i], and location
# coordinates (x[i],y[i])(x[i],y[i]) (both are integers). There are qq group queries, and each group query gives a
# city name. You need to answer the city name that is the closest to the city and has the same x or y
#
#
# If there are multiple answers that satisfy the conditions, the one with the smallest lexicographic name is output.
# The distance here is the Euler distance: the absolute value of the coordinate difference of x plus the absolute value
# of the coordinate difference of y.
#
#
# 0 <= Number of cities <= 10^5
# 0<= Ask for the number of groups <=10
# 1<= Coordinate <= 10^9
#

# 样例
# Example 1：
#
# Input: x = [3, 2, 1] y = [3, 2, 3] c = ["c1", "c2", "c3"] q = ["c1", "c2", "c3"]
# Output: ["c3", "NONE", "c1"]
# Explanation: For c1, c3 is the same as its y, the closest distance is (3-1)+(3-3)=2
# For c2, no city is the same as its x or y
# For c3, c1 is the same as his y, the closest distance is (3-1)+(3-3)=2

import collections
import sys

class Solution:
    """
    @param x: an array of integers, the x coordinates of each city[i]
    @param y: an array of integers, the y coordinates of each city[i]
    @param c: an array of strings that represent the names of each city[i]
    @param q: an array of strings that represent the names of query locations
    @return: the closest city for each query
    """
    # 给定二维平面上的城市的坐标数组（分为x坐标数组和y坐标数组），以及名字数组c，给出若干询问q，对每个城市名，问与其x坐标相同或者y
    # 坐标相同的城市中离其最近的城市的名字。如果不存在则标记为“NONE”。
    #
    # 思路是，先开两个哈希表，第一个哈希表的key存x坐标，value存一个pair，pair里存横坐标是x的城市的y坐标和其在c
    # 中的下标，第二个哈希表相反，key存y坐标，value存一个pair，pair里存纵坐标是y的城市的x坐标和其在c中的下标。
    # 同时还需要存一下每个城市名到其在c中的下标的映射。接着开始遍历q，先找到其对应的城市下标，然后通过这个下标，找到其x和y坐标，
    # 接着到哈希表里找到横坐标是x的城市和纵坐标是y的城市，然后遍历那些城市，求出距离最近的一个。代码如下：

    def NearestNeighbor(self, x, y, c, q):
        # write your code here
        x_to_y_and_cidx = collections.defaultdict(list)
        y_to_x_and_cidx = collections.defaultdict(list)
        c_to_x_and_y = dict()

        n = len(x)
        for i in range(n):
            x_cord = x[i]
            y_cord = y[i]
            c_name = c[i]

            x_to_y_and_cidx[x_cord].append((y_cord, i))
            y_to_x_and_cidx[y_cord].append((x_cord, i))
            c_to_x_and_y[c_name] = (x_cord, y_cord)

        rslt = []

        for q_name in q:
            min_dist = sys.maxsize
            min_dist_city = "NONE"
            x_cord, y_cord = c_to_x_and_y[q_name]

            # iterate through candidates with same X
            for y_cand, cidx_cand in x_to_y_and_cidx[x_cord]:
                name_cand = c[cidx_cand]
                if name_cand == q_name:
                    continue
                else:
                    d = abs(y_cand - y_cord)
                    if d < min_dist or (d == min_dist and name_cand < min_dist_city):
                        min_dist = d
                        min_dist_city = name_cand

            # iterate through candidate with same Y
            for x_cand, cidx_cand in y_to_x_and_cidx[y_cord]:
                name_cand = c[cidx_cand]
                if name_cand == q_name:
                    continue
                else:
                    d = abs(x_cand - x_cord)
                    if d < min_dist or (d == min_dist and name_cand < min_dist_city):
                        min_dist = d
                        min_dist_city = name_cand

            rslt.append(min_dist_city)
        return rslt


x = [3, 2, 1]
y = [3, 2, 3]
c = ["c1", "c2", "c3"]
q = ["c1", "c2", "c3"]

sol = Solution()
sol.NearestNeighbor(x, y, c, q)
