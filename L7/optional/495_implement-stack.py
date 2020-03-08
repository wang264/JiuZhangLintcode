# 495. 实现栈
# 中文English
# 实现一个栈，可以使用除了栈之外的数据结构
#
# 样例
# 例1:
#
# 输入：
# push(1)
# pop()
# push(2)
# top()  // return 2
# pop()
# isEmpty() // return true
# push(3)
# isEmpty() // return false
# 例2:
#
# 输入：
# isEmpty()


class MyListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    """
    @param: x: An integer
    @return: nothing
    """

    def __init__(self):
        self.dummy = MyListNode(-1)

    def push(self, x):
        # write your code here
        node = MyListNode(x)
        node.next = self.dummy.next
        self.dummy.next = node

    """
    @return: nothing
    """

    def pop(self):
        # write your code here
        node = self.dummy.next
        rst_val = node.val
        self.dummy.next = node.next
        node.next = None
        del node
        return rst_val

    """
    @return: An integer
    """

    def top(self):
        # write your code here
        return self.dummy.next.val

    """
    @return: True if the stack is empty
    """

    def isEmpty(self):
        # write your code here
        return self.dummy.next is None