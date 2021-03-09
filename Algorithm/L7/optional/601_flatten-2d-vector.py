# 601. Flatten 2D Vector
# 中文English
# Implement an iterator to flatten a 2d vector.
#
# 样例
# Example 1:
#
# Input:[[1,2],[3],[4,5,6]]
# Output:[1,2,3,4,5,6]
# Example 2:
#
# Input:[[7,9],[5]]
# Output:[7,9,5]

from collections import deque


class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        self.deque = deque(vec2d)
        self.next_element = None

    # Initialize your data structure here

    # @return {int} a next element
    def next(self):
        return self.next_element

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        if not self.deque:
            return False

        curr_element = self.deque.popleft()

        while isinstance(curr_element, list):
            for i in reversed(curr_element):
                self.deque.appendleft(i)
            if len(self.deque) != 0:
                curr_element = self.deque.popleft()
            else:
                curr_element = None

        if curr_element is None:
            return False
        else:
            self.next_element = curr_element
            return True


# Your Vector2D object will be instantiated and called as such:

vec2d = [[1, 2], [3], [4, 5, 6]]
i, v = Vector2D(vec2d), []
while i.hasNext(): v.append(i.next())
v

vec2d = [[], []]
i, v = Vector2D(vec2d), []
while i.hasNext(): v.append(i.next())