# 130. Heapify
# 中文English
# Given an integer array, heapify it into a min-heap array.
#
# For a heap array A, A[0] is the root of heap, and for each A[i], A[i * 2 + 1] is the left child of A[i] and A[i * 2 + 2] is the right child of A[i].
# 样例
# Example 1
#
# Input : [3,2,1,4,5]
# Output : [1,2,3,4,5]
# Explanation : return any one of the legitimate heap arrays
# 挑战
# O(n) time complexity
#
# 说明
# What is heap? What is heapify? What if there is a lot of solutions?
#
# Heap is a data structure, which usually have three methods: push, pop and top. where "push" add a new element the heap, "pop" delete the minimum/maximum element in the heap, "top" return the minimum/maximum element.
# Convert an unordered integer array into a heap array. If it is min-heap, for each element A[i], we will get A[i * 2 + 1] >= A[i] and A[i * 2 + 2] >= A[i].
# Return any of them.

# Heapify 的具体实现方法。时间复杂度为 O(n)O(n)，使用的是 siftdown
# 之所以是 O(n) 是因为从第 N/2 个位置开始往下 siftdown，那么就有大约 N/4 个数在 siftdown 中最多交换 1 次，
# N/8 个数最多交换 2 次，N/16 个数最多交换 3 次。
# 所以 O(N/4 * 1 + N/8 * 2 + N/16 * 3 + ... + 1 * LogN) = O(N)O(N/4∗1+N/8∗2+N/16∗3+...+1∗LogN)=O(N)


class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """

    def heapify(self, A):
        # write your code here
        for i in list(range(len(A) // 2, -1, -1)):
            self.siftdown(A, i)

    def siftdown(self, A, index):
        n = len(A)
        while index < n:
            left = index * 2 + 1
            right = index * 2 + 2
            min_index = index
            if left < n and A[left] < A[min_index]:
                min_index = left
            if right < n and A[right] < A[min_index]:
                min_index = right

            # if val in parent is smallest, break
            if min_index == index:
                break

            # switch the value of parent and it's min son
            A[min_index], A[index] = A[index], A[min_index]
            # then point index to the swapped index
            index = min_index

#
# sol=Solution()
# A=[6,7,3,2,1,9,4,5,8,10,]
# sol.heapify(A)
