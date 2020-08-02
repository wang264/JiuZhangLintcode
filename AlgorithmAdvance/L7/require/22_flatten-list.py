# 22. Flatten List
# 中文English
# Given a list, each element in the list can be a list or integer.flatten it into a simply list with integers.
#
# Example1:
# Input: [[1, 1], 2, [1, 1]]
# Output: [1, 1, 2, 1, 1]
#
# Explanation: \
# flatten it into a simply list with integers.
#
# Example 2:
# Input: [1, 2, [1, 2]]
# Output: [1, 2, 1, 2]
#
# Explanation:
# flatten it into a simply list with integers.
#
# Example
# 3:
# Input: [4, [3, [2, [1]]]]
# Output: [4, 3, 2, 1]
#
# Explanation: flatten it into a simply list with integers.
#
# Challenge
# Do it in non - recursive.
#
# Notice If the element in the given list is a list, it can contain list too.

from collections import deque


class Solution(object):

    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        flatten_list = []
        self.helper(nestedList, flatten_list)

        return flatten_list

    def helper(self, nestedList, flatten_list):
        if isinstance(nestedList, int):
            flatten_list.append(nestedList)
            return
        for element in nestedList:
            self.helper(element, flatten_list)

    def flatten_non_recursive(self, nestedList):
        nestedList = [nestedList]
        queue = deque(nestedList)
        flatten_list = []

        while queue:
            head = queue.popleft()
            if isinstance(head, list):
                for elem in reversed(head):
                    queue.appendleft(elem)
            else:
                flatten_list.append(head)

        return flatten_list


sol = Solution()
sol.flatten(nestedList=[[1, 1], 2, [1, 1]])
sol.flatten(nestedList=[4, [3, [2, [1]]]])

sol.flatten_non_recursive(nestedList=[[1, 1], 2, [1, 1]])
sol.flatten_non_recursive(nestedList=[4, [3, [2, [1]]]])
