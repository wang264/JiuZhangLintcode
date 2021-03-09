# Description
# Implement a web logger, which provide two methods:
#
# hit(timestamp), record a hit at given timestamp.
# get_hit_count_in_last_5_minutes(timestamp), get hit count in last 5 minutes.
# the two methods will be called with non-descending timestamp (in sec).
#
# The unit of timestamp is seconds.
#
# The call to the function is in chronological order, that is to say, timestamp is in ascending order.
#
# Have you met this question in a real interview?
# Example
# Example 1:
#
# Input:
#   hit(1);
#   hit(2);
#   get_hit_count_in_last_5_minutes(3);
#   hit(300);
#   get_hit_count_in_last_5_minutes(300);
#   get_hit_count_in_last_5_minutes(301);
# Output:
#   2
#   3
#   2
# Example 2:
#
# Input:
#   hit(1)
#   hit(1)
#   hit(1)
#   hit(2)
#   get_hit_count_in_last_5_minutes(3)
#   hit(300)
#   get_hit_count_in_last_5_minutes(300)
#   get_hit_count_in_last_5_minutes(301)
#   get_hit_count_in_last_5_minutes(302)
#   get_hit_count_in_last_5_minutes(900)
#   get_hit_count_in_last_5_minutes(900)
# Output:
#   4
#   5
#   2
#   1
#   0
#   0
#
# 因为 timestamp 是递增的, 所以我们可以用一个队列储存所有的记录.
#
# hit(timestamp) 直接将 timestamp 放到队尾
# get_hit_count_in_last_5_minutes(timestamp) 弹出队首, 直到队首元素与 timestamp 差距在300内为止, 返回队列大小即可
# 其中, 弹出元素的过程可以优化, 使用二分查找确定最大的小于 timestamp - 300 的元素.

class WebLogger:

    def __init__(self):
        self.Q = []

    """
    @param: timestamp: An integer
    @return: nothing
    """

    def hit(self, timestamp):
        self.Q.append(timestamp)

    """
    @param: timestamp: An integer
    @return: An integer
    """

    def get_hit_count_in_last_5_minutes(self, timestamp):
        if self.Q == []:
            return 0
        i = 0
        n = len(self.Q)
        while i < n and self.Q[i] + 300 <= timestamp:
            i += 1
        self.Q = self.Q[i:]
        return len(self.Q)