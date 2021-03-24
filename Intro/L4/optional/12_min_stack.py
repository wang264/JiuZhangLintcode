# 12. Min Stack
# 中文English
# Implement a stack with following functions:
#
# push(val) push val into the stack
# pop() pop the top element and return it
# min() return the smallest number in the stack
# All above should be in O(1) cost.
#
# Example
# Example 1:
#
# Input:
#   push(1)
#   pop()
#   push(2)
#   push(3)
#   min()
#   push(1)
#   min()
# Output:
#   1
#   2
#   1
# Example 2:
#
# Input:
#   push(1)
#   min()
#   push(2)
#   min()
#   push(3)
#   min()
# Output:
#   1
#   1
#   1
# Notice
# min() will never be called when there is no number in the stack.

# 算法：最小栈

# 思路：
# 1. 要求O(1)时间内完成所有操作，压入栈弹和出栈顶元素并返回本来就是O(1)没有问题，要返回栈中元素最小值也是O(1)就需要一个辅助栈。
# 2. 在压入新元素时，如果辅助栈为空或者辅助栈顶元素大于新元素，那么新元素就是目前最小值，压入新元素；如果辅助栈顶元素小于新元素，那么再次压入栈顶元素。
# 3. 在弹出元素时，辅助栈跟着一起弹出栈顶元素。
# 4. 这样就满足了辅助栈内存储的最小值与存储数据的栈同步，查询最小值的操作是O(1)的。

# 复杂度：
# 1. 空间复杂度取决于输入的数据
# 2. 时间复杂度O(1)

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):
        self.stack.append(number)
        if not self.min_stack:
            self.min_stack.append(number)
            return

        if number < self.min_stack[-1]:
            self.min_stack.append(number)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()

    def min(self):
        return self.min_stack[-1]

