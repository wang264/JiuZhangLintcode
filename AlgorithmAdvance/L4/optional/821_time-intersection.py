# 时间交集 · Time Intersection
# Sweep line
# 脸书
# 区间
# 描述
# Give two users' ordered online time series, and each section records the user's login time point x and offline
# time point y. Find out the time periods when both users are online at the same time,
# and output in ascending order.you need return a list of intervals.

# * We guarantee that the length of online time series meet `1 <= len <= 1e6`.
# * For a user's online time series, any two of its sections do not intersect.
#
# 描述
# 目前有两个用户的有序在线时间序列，每一个区间记录了该用户的登录时间点x和离线时间点y，请找出这两个用户同时在线的时间段，
# 输出的时间段请从小到大排序。你需要返回一个intervals的列表
# * 我们保证在线时间序列的长度 `1 <= len <= 1e6`。 * 我们保证在线时间序列是合法的，
# 即对于某一个用户的在线时间序列，它的任意两个区间不相交。


# Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param seqA: the list of intervals
    @param seqB: the list of intervals
    @return: the time periods
    """

    # similar to the #391, number of airplanes in the sky.
    # use sweep line to solve this problem. we maintain a variable 'count' which represent the number of
    # users that are online at that time. if count equals to 2, then it means that both of them are online.
    def timeIntersection(self, seqA, seqB):
        points = []
        for interval in seqA + seqB:
            points.append((interval[0], +1))
            points.append((interval[1], -1))
        points.sort()

        rslt = []
        curr_count = 0
        previous_count = 0
        previous_timestamp = None
        for curr_timestamp, delta in points:
            curr_count += delta
            self.merge_to_rslt(rslt, previous_count, previous_timestamp, curr_count, curr_timestamp)
            previous_timestamp = curr_timestamp
            previous_count = curr_count

        return rslt

    def merge_to_rslt(self, rslt, previous_count, previous_timestamp, curr_count, curr_timestamp):
        if curr_count == 2 and previous_count != 2:
            rslt.append([curr_timestamp, None])
        if previous_count == 2 and curr_count != 2:
            rslt[-1][1] = curr_timestamp


sol = Solution()
assert sol.timeIntersection(seqA=[(0, 2), (3, 6), (13, 14), (16, 18)],
                     seqB=[(1, 4), (5, 9), (12, 14)]) == [[1, 2], [3, 4], [5, 6], [13, 14]]
