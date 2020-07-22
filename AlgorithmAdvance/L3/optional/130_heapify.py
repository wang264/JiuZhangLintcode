# 130. Heapify
# 中文English
# Given an integer array, heapify it into a min-heap array.
#
# For a heap array A, A[0] is the root of heap, and for each A[i], A[i * 2 + 1] is the left child of A[i] and
# A[i * 2 + 2] is the right child of A[i].
# Example
# Example 1
#
# Input : [3,2,1,4,5]
# Output : [1,2,3,4,5]
# Explanation : return any one of the legitimate heap arrays
# Challenge
# O(n) time complexity
#
# Clarification
# What is heap? What is heapify? What if there is a lot of solutions?
#
# Heap is a data structure, which usually have three methods: push, pop and top.
# where "push" add a new element the heap, "pop" delete the minimum/maximum element in the heap,
# "top" return the minimum/maximum element.
# Convert an unordered integer array into a heap array.
# If it is min-heap, for each element A[i], we will get A[i * 2 + 1] >= A[i] and A[i * 2 + 2] >= A[i].
# Return any of them.


class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """

    def heapify(self, A):
        # write your code here
        # we start with the index of the last parent, which is len(A)//2
        for i in range((len(A)-2) // 2, -1, -1):
            self.sift_down(A, i)

        return A

    def sift_down(self, A, idx):
        n = len(A)
        while idx < n:
            node_val = A[idx]
            smallest_idx = idx
            smallest_val = node_val
            # if have left child, and left child is smaller than current val
            if idx*2+1<n and A[idx*2+1]<smallest_val:
                smallest_idx = idx*2+1
                smallest_val = A[idx*2+1]
            # if have right child, and right child is smaller than the minimum of current node and its left child.
            if idx*2+2<n and A[idx*2+2]<smallest_val:
                smallest_idx = idx*2+2
                smallest_val = A[idx*2+2]

            # if both it's child is larger than it. done
            if smallest_idx == idx:
                break
            # swap current node with the minimum of its left and right child
            A[smallest_idx], A[idx] = A[idx], A[smallest_idx]

            # update idx, continue to walk down
            idx = smallest_idx


sol = Solution()
sol.heapify(A=[3, 2, 1, 4, 5])
