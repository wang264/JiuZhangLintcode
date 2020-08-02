# 528. Flatten Nested List Iterator
# 中文English
# Given a nested list of integers, implement an iterator to flatten it.
#
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
#
# Example
# Example1
#
# Input: list = [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Example2
#
# Input: list = [1,[4,[6]]]
# Output: [1,4,6]
# Notice
# You don't need to implement the remove method.


"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""

from collections import deque


class NestedIterator(object):

    def __init__(self, nestedList):
        self.deque = deque(nestedList)

    # Initialize your data structure here.

    # @return {int} the next element in the iteration
    def next(self):
        if not self.hasNext():
            return
        int_or_list = self.deque.popleft()
        while isinstance(int_or_list, list):
            for item in reversed(int_or_list):
                self.deque.appendleft(item)

            int_or_list = self.deque.popleft()

        # in here the int_or_list must be an init
        return int_or_list

    # Write your code here

    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        return len(self.deque) != 0
# Write your code here


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

i, v = NestedIterator(nestedList=[[1,1],2,[1,1]]), []
while i.hasNext():
    v.append(i.next())


i, v = NestedIterator(nestedList=[]), []
while i.hasNext():
    v.append(i.next())
