# 919. Meeting Rooms II
# 中文English
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
# find the minimum number of conference rooms required.
#
# Example
# Example1
#
# Input: intervals = [(0,30),(5,10),(15,20)]
# Output: 2
# Explanation:
# We need two meeting rooms
# room1: (0,30)
# room2: (5,10),(15,20)
# Example2
#
# Input: intervals = [(2,7)]
# Output: 1
# Explanation:
# Only need one meeting room

# Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    # use sweep line algorithm
    # if meeting A end at 30 and meeting B start at 30. meeting end first.
    # so [(0,30), (30,50)] only need 1 meeting room
    def minMeetingRooms(self, intervals):
        # delta = +1 --> meeting room +1, meeting start
        # delta = -1 --> meeting room -1, meeting over
        # because be default if the 'time' are the same, -1 appear before 1 after sort ascendingly.
        events = []  # (time, delta)
        for interval in intervals:
            start_time, end_time = interval
            events.append((start_time, +1))
            events.append((end_time, -1))

        events.sort()

        curr_meeting_rooms = 0
        max_meeting_rooms = 0
        for event in events:
            event_time, delta = event
            curr_meeting_rooms += delta
            max_meeting_rooms = max(max_meeting_rooms, curr_meeting_rooms)

        return max_meeting_rooms


sol = Solution()
assert sol.minMeetingRooms(intervals=[(0, 30), (30, 50)]) == 1
assert sol.minMeetingRooms(intervals=[(0, 30), (5, 10), (15, 20)]) == 2
assert sol.minMeetingRooms(intervals=[(2, 7)]) == 1
