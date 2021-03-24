# 494. Implement Stack by Two Queues
# 中文English
# Implement a stack by two queues. The queue is first in first out (FIFO). That means you can not directly pop the last element in a queue.
#
# Example
# Example 1:
#
# Input:
# push(1)
# pop()
# push(2)
# isEmpty() // return false
# top() // return 2
# pop()
# isEmpty() // return true
# Example 2:
#
# Input:
# isEmpty()


from collections import deque


class Stack:
    """
    @param: x: An integer
    @return: nothing
    """

    def __init__(self):
        self.q1 = deque(list())
        self.q2 = deque(list())

    def push(self, x):
        # write your code here
        self.q1.append(x)

    """
    @return: nothing
    """

    def pop(self):
        # write your code here
        if len(self.q1) == 0:
            return None
        if len(self.q1) == 1:
            return self.q1.popleft()
        else:
            while len(self.q1) > 1:
                self.q2.append(self.q1.popleft())

            val = self.q1.pop()
            self.q1, self.q2 = self.q2, self.q1
            return val

    """
    @return: An integer
    """

    def top(self):
        # write your code here
        while len(self.q1) != 0:
            val = self.q1.popleft()
            self.q2.append(val)
        self.q1, self.q2 = self.q2, self.q1
        return val

    """
    @return: True if the stack is empty
    """

    def isEmpty(self):
        # write your code here
        return len(self.q1) == 0


