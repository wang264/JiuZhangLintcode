# 642. 数据流滑动窗口平均值
# 中文English
# 给出一串整数流和窗口大小，计算滑动窗口中所有整数的平均值。
#
# 样例1 :
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1 // 返回 1.00000
# m.next(10) = (1 + 10) / 2 // 返回 5.50000
# m.next(3) = (1 + 10 + 3) / 3 // 返回 4.66667
# m.next(5) = (10 + 3 + 5) / 3 // 返回 6.00000
from collections import deque


class MovingAverage:
    """
    @param: size: An integer
    """

    def __init__(self, size):
        # do intialization if necessary
        self.queue = deque()
        self.sum = 0
        self.size = size

    """
    @param: val: An integer
    @return:
    """

    def next(self, val):
        # write your code here
        self.sum += val
        self.queue.append(val)
        if len(self.queue) > self.size:
            self.sum -= self.queue.popleft()

        return self.sum / len(self.queue)
#
# m = MovingAverage(3)
# m.next(1) #= 1 # 返回 1.00000
# m.next(10)# = (1 + 10) / 2 // 返回 5.50000
# m.next(3) #= (1 + 10 + 3) / 3 // 返回 4.66667
# m.next(5) #= (10 + 3 + 5) / 3 // 返回 6.00000

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)