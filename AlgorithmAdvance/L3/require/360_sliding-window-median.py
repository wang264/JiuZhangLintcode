# 360. Sliding Window Median
# 中文English
# Given an array of n integer, and a moving window(size k), move the window at each iteration from the start
# of the array, find the median of the element inside the window at each moving.
# (If there are even numbers in the array, return the N/2-th number after sorting the element in the window. )
#
# Example
# Example 1:
#
# Input:
# [1,2,7,8,5]
# 3
# Output:
# [2,7,7]
#
# Explanation:
# At first the window is at the start of the array like this `[ | 1,2,7 | ,8,5]` , return the median `2`;
# then the window move one step forward.`[1, | 2,7,8 | ,5]`, return the median `7`;
# then the window move one step forward again.`[1,2, | 7,8,5 | ]`, return the median `7`;
# Example 2:
#
# Input:
# [1,2,3,4,5,6,7]
# 4
# Output:
# [2,3,4,5]
#
# Explanation:
# At first the window is at the start of the array like this `[ | 1,2,3,4, | 5,6,7]` , return the median `2`;
# then the window move one step forward.`[1,| 2,3,4,5 | 6,7]`, return the median `3`;
# then the window move one step forward again.`[1,2, | 3,4,5,6 | 7 ]`, return the median `4`;
# then the window move one step forward again.`[1,2,3,| 4,5,6,7 ]`, return the median `5`;
# Challenge
# O(nlog(n)) time
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
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """

    def medianSlidingWindow(self, nums, k):
        # write your code here
        max_heap = Heap()
        min_heap = Heap()
        rslt = []
        for i, num in enumerate(nums):

            #ADD TO WINDOW
            # the first element, we push into the max_heap
            if i == 0:
                max_heap.push(-1 * num)
            else:
                if num > -1 * max_heap.top():
                    min_heap.push(num)
                else:
                    max_heap.push(-1 * num)

            #DELETE FROM WINDOW
            # need to consider which element to remove
            if i >= k:
                num_need_del = nums[i - k]
                if num_need_del > -1 * max_heap.top():
                    min_heap.remove(num_need_del)
                else:
                    max_heap.remove(-1 * num_need_del)

            # balance the two heap
            if max_heap.size() - min_heap.size() > 1:
                temp = -1 * max_heap.top()
                max_heap.pop()
                min_heap.push(temp)
            elif min_heap.size() > max_heap.size():
                temp = min_heap.top()
                min_heap.pop()
                max_heap.push(-1 * temp)

            # need to start recording median
            if i >= k - 1:
                rslt.append(-1 * max_heap.top())



        return rslt


sol = Solution()
sol.medianSlidingWindow(nums=[1, 2, 7, 8, 5], k=3)
sol.medianSlidingWindow(nums=[1, 2, 3, 4, 5, 6, 7], k=4)
