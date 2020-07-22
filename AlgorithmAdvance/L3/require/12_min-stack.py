# 12. Min Stack
# 中文English
# Implement a stack with following functions:
#
# push(val) push val into the stack
# pop() pop the top element and return it
# min() return the smallest number in the stack
# All above should be in O(1) cost.
#
# 12. 带最小值操作的栈
# 中文English
# 实现一个栈, 支持以下操作:
#
# push(val) 将 val 压入栈
# pop() 将栈顶元素弹出, 并返回这个弹出的元素
# min() 返回栈中元素的最小值
# 要求 O(1) 开销.


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
#
#
#
class MinStack:

    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.min_stack = []

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):
        self.stack.append(number)
        if len(self.min_stack) == 0:
            self.min_stack.append(number)
        else:
            min_number = self.min()
            self.min_stack.append(min(min_number, number))

    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()

    def min(self):
        return self.min_stack[-1]


sol = MinStack()
sol.push(1)
sol.min()
sol.push(2)
sol.min()
sol.push(3)
sol.min()
sol.push(-1)
sol.min()
sol.pop()
sol.min()
