class Stack:
    """
    @param: x: An integer
    @return: nothing
    """
    def __init__(self):
        self.arr = list()
    def push(self, x):
        # write your code here
        self.arr.append(x)
    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        self.arr.pop()
    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.arr[-1]
    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return len(self.arr)==0