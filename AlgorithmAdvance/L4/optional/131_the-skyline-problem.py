# 131. The Skyline Problem
# 中文English
# Given N buildings in a x-axis，each building is a rectangle and can be represented by a triple
# (start, end, height)，where start is the start position on x-axis, end is the end position on x-axis and height
#  is the height of the building. Buildings may overlap if you see them from far away，find the outline of them。
# An outline can be represented by a triple, (start, end, height), where start is the start position on x-axis
# of the outline, end is the end position on x-axis and height is the height of the outline.

#
# Building Outline
#
# Example
# Example 1
#
# Input:
# [
#     [1, 3, 3],
#     [2, 4, 4],
#     [5, 6, 1]
# ]
# Output:
# [
#     [1, 2, 3],
#     [2, 4, 4],
#     [5, 6, 1]
# ]
# Explanation:
# The buildings are look like this in the picture. The yellow part is buildings.
#
# Example 2
#
# Input:
# [
#     [1, 4, 3],
#     [6, 9, 5]
# ]
# Output:
# [
#     [1, 4, 3],
#     [6, 9, 5]
# ]
# Explanation:
# The buildings are look like this in the picture. The yellow part is buildings.
#
# Notice
# Please merge the adjacent outlines if they have the same height and make sure different outlines cant overlap on x-axis.

# 将每个矩形的左边和右边建立两个事件， 记下对应高度。
# 　对所有事件按X坐标排序。
# 建立高度的最大堆
# 扫描线
#   - 遇到左边事件，堆中加入高度
#   - 遇到右边事件，堆中删除高度
# 堆中最大值即为组合图形现在的高度
# 将同一个X坐标的事件全部处理完成后，如果新的高度!=原来的高度，说明出现拐点，记录下来。
#


import heapq


# 我们可以用两个优先队列维护一个可以删除的堆
class Heap:
    # q1存储了当前所有元素（包括未删除元素）
    # q2存储了q1中已删除的元素
    def __init__(self):
        self.__q1 = []
        self.__q2 = []

    # push 操作向 q1 中 push 一个新的元素
    def push(self, x):
        heapq.heappush(self.__q1, x)

    # q2 中 push 一个元素表示在 q1 中它已经被删除了
    def remove(self, x):
        heapq.heappush(self.__q2, x)

    # 这里就要用到 q2 里面的元素了，如果堆顶的元素已经被 remove 过，那么它此时应该在 q2 中的堆顶
    # 此时我们把两个堆一起 pop 就好了，直到堆顶元素不同或者 q2 没元素了
    def pop(self):
        while len(self.__q2) != 0 and self.__q1[0] == self.__q2[0]:
            heapq.heappop(self.__q1)
            heapq.heappop(self.__q2)
        if len(self.__q1) != 0:
            heapq.heappop(self.__q1)

    # 这里就是先进行和 pop 中类似的操作，删除已经 remove 的元素，然后取出堆顶
    def top(self):
        while len(self.__q2) != 0 and self.__q1[0] == self.__q2[0]:
            heapq.heappop(self.__q1)
            heapq.heappop(self.__q2)
        if len(self.__q1) != 0:
            return self.__q1[0]

    # 这个就是返回堆大小的，可以知道堆当前真实大小就是 q1 大小减去 q2 大小
    def size(self):
        return len(self.__q1) - len(self.__q2)

    def sol(self):
        print(self.__q1)
        # print(self.q2)


class Solution:
    """
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """

    def buildingOutline(self, buildings):
        # write your code here
        events = []
        for start, end, height in buildings:
            # (time, is_end_flag, height)
            events.append((start, False, height))
            events.append((end, True, height))

        rslt = []
        events = sorted(events)
        max_heap = Heap()
        last_position = None
        for i, event in enumerate(events):
            position, is_end, height = event
            if max_heap.size() == 0:
                max_height = 0
            else:
                max_height = -1 * max_heap.top()

            self.merge_to(rslt, last_position, position, max_height)

            if not is_end:
                max_heap.push(-1 * height)
            else:
                max_heap.remove(-1 * height)

            last_position = position

        return rslt

    def merge_to(self, rslt, start, end, height):
        if start is None or height == 0 or start == end:
            return

        if not rslt:
            rslt.append([start, end, height])
            return

        _, prev_end, prev_height = rslt[-1]
        if prev_height == height and prev_end == start:
            rslt[-1][1] = end
            return

        rslt.append([start, end, height])

sol = Solution()
sol.buildingOutline(buildings=[[1, 3, 3], [2, 4, 4], [5, 6, 1]])
