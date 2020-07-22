# 81. Find Median from Data Stream
# 中文English
# Numbers keep coming, return the median of numbers at every time a new number added.
#
# 81. 数据流中位数
# 中文English
# 数字是不断进入数组的，在每次添加一个新的数进入数组的同时返回当前新数组的中位数。

# Example
# Example 1
#
# Input: [1,2,3,4,5]
# Output: [1,1,2,2,3]
# Explanation:
# The medium of [1] and [1,2] is 1.
# The medium of [1,2,3] and [1,2,3,4] is 2.
# The medium of [1,2,3,4,5] is 3.
# Example 2
#
# Input: [4,5,1,3,2,6,0]
# Output: [4,4,4,3,3,3,3]
# Explanation:
# The medium of [4], [4,5], [4,5,1] is 4.
# The medium of [4,5,1,3], [4,5,1,3,2], [4,5,1,3,2,6] and [4,5,1,3,2,6,0] is 3.
# Challenge
# Total run time in O(nlogn).
#
# Clarification
# What's the definition of Median?
#
# The median is not equal to median in math.
# Median is the number that in the middle of a sorted array.
# If there are n numbers in a sorted array A, the median is A[(n - 1) / 2]
# For example, if A=[1,2,3], median is 2. If A=[1,19], median is 1.

import heapq


class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """

    def __init__(self):
        self.median = None
        self.max_heap = []
        self.min_heap = []
        self.count = 0

    # the size of the max_heap can be at most 1 element larger than min_heap
    # the size of min_heap can not be larger than max_heap.
    # the median is the max_element in the max_heap
    def medianII(self, nums):
        if nums is None or len(nums) == 0:
            return None
        self.median = None  # the max element in the first half/maxheap would be the median
        self.max_heap = []  # store the first half
        self.min_heap = []  # store the second half
        self.count = 0

        rslt = []
        heapq.heappush(self.max_heap, -1 * nums[0])  # heapq is a min heap, we use it as maxheap here
        self.median = -1 * self.max_heap[0]  # the maximum element
        rslt.append(self.median)
        self.count += 1
        for num in nums[1:]:
            self.count += 1
            if num > -1 * self.max_heap[0]:  # if this number is larger than the largest in max_heap
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -1 * num)

            # balance
            if len(self.max_heap) - len(self.min_heap) > 1:
                temp = -1 * heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, temp)
            if len(self.min_heap) > len(self.max_heap):
                temp = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -1 * temp)
            self.median = -1 * self.max_heap[0]
            rslt.append(self.median)

        return rslt


sol = Solution()
assert sol.medianII(nums=[1, 2, 3, 4, 5]) == [1, 1, 2, 2, 3]
assert sol.medianII(nums=[4, 5, 1, 3, 2, 6, 0]) == [4, 4, 4, 3, 3, 3, 3]
assert sol.medianII(nums=[4, 5, 1, 3, 2]) == [4, 4, 4, 3, 2]
