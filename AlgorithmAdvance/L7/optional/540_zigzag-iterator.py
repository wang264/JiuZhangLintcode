# 540. Zigzag Iterator
# 中文English
# Given two 1d vectors, implement an iterator to return their elements alternately.
#
# Example
# Example1
#
# Input: v1 = [1, 2] and v2 = [3, 4, 5, 6]
# Output: [1, 3, 2, 4, 5, 6]
# Explanation:
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].
# Example2
#
# Input: v1 = [1, 1, 1, 1] and v2 = [3, 4, 5, 6]
# Output: [1, 3, 1, 4, 1, 5, 1, 6]

from collections import deque
class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    def __init__(self, v1, v2):
        # do intialization if necessary
        self.deque_1 = deque(v1)
        self.deque_2 = deque(v2)

        self.pop_v1_next = True

    """
    @return: An integer
    """
    def next(self):
        # write your code here
        if self.pop_v1_next:
            if self.deque_1:
                rslt = self.deque_1.popleft()
                self.pop_v1_next = False
                return rslt
            else:
                rslt = self.deque_2.popleft()
                self.pop_v1_next = False
                return rslt
        else:
            if self.deque_2:
                rslt = self.deque_2.popleft()
                self.pop_v1_next = True
                return rslt
            else:
                rslt = self.deque_1.popleft()
                self.pop_v1_next = True
                return rslt


    """
    @return: True if has next
    """
    def hasNext(self):
        # write your code here
        if self.deque_1 or self.deque_2:
            return True
        else:
            return False


# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result

