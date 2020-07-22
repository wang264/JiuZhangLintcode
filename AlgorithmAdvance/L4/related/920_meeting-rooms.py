# 920. Meeting Rooms
# 中文English
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
# determine if a person could attend all meetings.
#
# Example
# Example1
#
# Input: intervals = [(0,30),(5,10),(15,20)]
# Output: false
# Explanation:
# (0,30), (5,10) and (0,30),(15,20) will conflict
# Example2
#
# Input: intervals = [(5,8),(9,15)]
# Output: true
# Explanation:
# Two times will not conflict
# Notice
# (0,8),(8,10) is not conflict at 8

# Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def canAttendMeetings(self, intervals):
        # Write your code here
        if len(intervals) <= 1:
            return True
        events = []
        for interval in intervals:
            events.append((interval.start, +1))
            events.append((interval.end, -1))

        events.sort()
        meeting_room = 0
        for event in events:
            time, delta = event
            meeting_room = meeting_room + delta
            if meeting_room > 1:
                return False

        return True


def build_intervals(list):
    rslt = []
    for fst, snd in list:
        rslt.append(Interval(start=fst, end=snd))
    return rslt


sol = Solution()
intervals = build_intervals([(0, 30), (5, 10), (15, 20)])
sol.canAttendMeetings(intervals=intervals)
