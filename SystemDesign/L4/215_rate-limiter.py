# Description
# Implement a rate limiter, provide one method: is_ratelimited(timestamp, event, rate, increment).
#
# timestamp: The current timestamp, which is an integer and in second unit.
# event: The string to distinct different event. for example, "login" or "signup".
# rate: The rate of the limit. 1/s (1 time per second), 2/m (2 times per minute), 10/h (10 times per hour), 100/d (100 times per day). The format is [integer]/[s/m/h/d].
# increment: Whether we should increase the counter. (or take this call as a hit of the given event)、
# The method should return true or false to indicate the event is limited or not.
# Note: Login failure is not recorded in login times.
#
# Have you met this question in a real interview?
# Example
# Example 1
#
# Input:
# is_ratelimited(1, "login", "3/m", true)
# is_ratelimited(11, "login", "3/m", true)
# is_ratelimited(21, "login", "3/m", true)
# is_ratelimited(30, "login", "3/m", true)
# is_ratelimited(65, "login", "3/m", true)
# is_ratelimited(300, "login", "3/m", true)
#
# Output:
# false
# false
# false
# true
# false
# false
#
# Challenge
# How many different algorithms you can come up with?

from collections import defaultdict
from bisect import bisect_left


class Solution:
    """
    @param: timestamp: the current timestamp
    @param: event: the string to distinct different event
    @param: rate: the format is [integer]/[s/m/h/d]
    @param: increment: whether we should increase the counter
    @return: true or false to indicate the event is limited or not
    """

    def __init__(self, ):
        self.event_to_timestamps = defaultdict(list)
        self.windows = {
            's': 1,
            'm': 60,
            'h': 3600,
            'd': 86400
        }

    def isRatelimited(self, timestamp, event, rate, increment):
        max_count = int(rate[:-2])
        window = self.windows[rate[-1]]

        is_limited = self.is_valid(timestamp, event, max_count, window)

        if not is_limited and increment:
            self.event_to_timestamps[event].append(timestamp)

        return is_limited

    def is_valid(self, timestamp, event, max_count, window):
        start_time = timestamp - window + 1
        idx = bisect_left(self.event_to_timestamps[event], start_time)
        cnt = len(self.event_to_timestamps[event]) - idx

        return cnt >= max_count