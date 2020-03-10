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

class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.vec2d = vec2d
        self.row = 0
        self.col = -1
        self.next_element = None

    # @return {int} a next element
    def next(self):
        # Write your code here
        # return the value currently in self.next_element and set it to none
        if self.next_element is None:
            self.hasNext()
        curr, self.next_element = self.next_element, None
        return curr

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        if self.next_element:
            return True

        self.col += 1

        # try to find the next valid row starting point
        # while instead of if in the below line is to handel the case of [[], [], []]
        # where multiple consecutive row have no entry.
        while self.row < len(self.vec2d) and self.col >= len(self.vec2d[self.row]):
            self.row += 1
            self.col = 0

        # update the self.next_element
        if self.row < len(self.vec2d) and self.col < len(self.vec2d[self.row]):
            self.next_element = self.vec2d[self.row][self.col]
            return True

        return False
# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())

# vec2d = [[],[],[1,2,3],[],[4]]
# i, v = Vector2D(vec2d), []
# while i.hasNext():
#     v.append(i.next())
