# 229. Stack Sorting
# 中文English
# Sort a stack in ascending order (with biggest terms on top).
#
# You may use at most one additional stack to hold items, but you may not copy the
# elements into any other data structure (e.g. array).
#
# You don't need to return a new stack, just sort elements in the given parameter stack.
#
# Example
# Given stack =
#
# | |
# |3|
# |1|
# |2|
# |4|
#  -
# After sort, the stack should become:
#
# | |
# |4|
# |3|
# |2|
# |1|
#  -
# The data will be serialized to [4,2,1,3]. The last element is the element on the top of the stack.
#
# Notice
# O(n^2) time is acceptable.

class Solution:
    """
    @param: stk: an integer stack
    @return: void
    """

    def stackSorting(self, stack):
        stack_2 = []
        while stack:
            element = stack.pop()
            while stack_2 and stack_2[-1]<element:
                stack.append(stack_2.pop())

            stack_2.append(element)

        while stack_2:
            stack.append(stack_2.pop())

stack = [4, 2, 1, 3]

sol = Solution()
sol.stackSorting(stack=stack)
print(stack)
