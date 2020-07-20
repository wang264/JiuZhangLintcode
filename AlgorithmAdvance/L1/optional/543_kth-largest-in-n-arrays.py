# 描述
# Find K-th largest element in N arrays.
#
# You can swap elements in the array
# 样例
# Example 1:
#
# Input:
# k=3, [[9,3,2,4,7],[1,2,3,4,8]]
# Output:
# 7
# Explanation:
# the 3rd largest element is 7
#
# Example 2:
#
# Input:
# k = 2, [[9,3,2,4,8],[1,2,3,4,2]]
# Output:
# 8
# Explanation:
# the 1st largest element is 9, 2nd largest element is 8, 3rd largest element is 4 and etc.

# 算法：优先队列 / k路归并
#
# 我们先对每个数组进行排序，让每个数组有序，先把每个数组的最后一位数添加到空的队列里，然后每次弹出队列顶元素，每次弹出完之后，如果该数字不在对应arrays[i]的第一位，那就把该数字前一位数字加入到堆中。弹出k-1次后的队首的结果就是第k大
#
# 优先队列的本质是大顶堆/小顶堆，python中有性质相同更便于使用的minheap，c++和java中我们直接使用优先队列并且手写比较器
# 注意判断数组是否有空集的存在
# 把每个数组的最后一位数添加到队列里
# 依次弹出队首
# 如果该数字不在对应arrays[i]的第一位，那就把该数字前一位数字加入到堆中
# 弹出k次后，第k大元素就在tmp中
# 复杂度分析
#
# 时间复杂度O(Σnilogni+klogm)
# 对每个数组排序的复杂度是Σnilogni, ni为arrayi的长度，每次进堆、出堆的操作都是logm，其中m是array的总长度，所有总时间复杂度是O(Σnilogni+klogm)`
# 空间复杂度O(n*m)
# 数组arrays的大小

import heapq


class Solution:
    def KthInArrays(self, arrays, k):
        if len(arrays) == 0:
            return None
        for i in range(len(arrays)):
            arrays[i].sort()

        min_heap = []
        # push the biggest element into the heap.
        # for each record in the heap, we store the (number, which_array, the_index_in that array)
        for i in range(len(arrays)):
            if len(arrays[i]) > 0:
                heapq.heappush(min_heap, (-arrays[i][-1], i, len(arrays[i]) - 1))

        for _ in range(k):
            max_val, arr_idx, element_idx = heapq.heappop(min_heap)
            if element_idx >= 1:
                heapq.heappush(min_heap, (-arrays[arr_idx][element_idx - 1], arr_idx, element_idx - 1))

        return max_val * -1


sol = Solution()
assert sol.KthInArrays(k=3, arrays=[[9, 3, 2, 4, 7], [1, 2, 3, 4, 8]]) == 7
assert sol.KthInArrays(k=2, arrays=[[9, 3, 2, 4, 8], [1, 2, 3, 4, 2]]) == 8
