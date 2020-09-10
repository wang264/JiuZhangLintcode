# 494. 双队列实现栈
# 中文English
# 利用两个队列来实现一个栈的功能
#
# 例1:
# 输入：
# push(1)
# pop()
# push(2)
# isEmpty() // return false
# top() // return 2
# pop()
# isEmpty() // return true
# 例2:
#
# 输入：
# isEmpty()
from collections import deque


class Stack:
    """
    @param: x: An integer
    @return: nothing
    """

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        # write your code here
        self.q1.append(x)

    """
    @return: nothing
    """

    def pop(self):
        # write your code here
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        item = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return None

    """
    @return: An integer
    """

    def top(self):
        # write your code here
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        item = self.q1.popleft()
        self.q2.append(item)
        self.q1, self.q2 = self.q2, self.q1
        return item

    """
    @return: True if the stack is empty
    """

    def isEmpty(self):
        return len(self.q1) == 0


s = Stack()
s.push(1)
s.push(2)
s.pop()
s.push(3)
s.isEmpty() #// return false
s.top() #// #return 2
s.pop()
s.isEmpty() #// return true

s = Stack()
s.push(1)
s.pop()
s.push(2)
s.isEmpty()
s.top()
s.pop()
s.isEmpty()