# Description
# Given two integer arrays sorted in ascending order and an integer k. Define sum = a + b, where a is an element from
# the first array and b is an element from the second one. Find the kth smallest sum out of all possible sums.
#
# Example 1
# Input:
# a = [1, 7, 11]
# b = [2, 4, 6]
# k = 3
# Output: 7
# Explanation: The sums are [3, 5, 7, 9, 11, 13, 13, 15, 17] and the 3th is 7.
#
# Example 2
# Input:
# a = [1, 7, 11]
# b = [2, 4, 6]
# k = 4
# Output: 9
# Explanation: The sums are [3, 5, 7, 9, 11, 13, 13, 15, 17] and the 4th is 9.
#
# Example 3
# Input:
# a = [1, 7, 11]
# b = [2, 4, 6]
# k = 8
# Output: 15
# Explanation: The sums are [3, 5, 7, 9, 11, 13, 13, 15, 17] and the 8th is 15.
# Challenge
# Do it in either of the following time complexity:
# O(k log min(n, m, k)). where n is the size of A, and m is the size of B.
# O( (m + n) log maxValue). where maxValue is the max number in A and B.

# 给定两个排好序的数组 A, B，定义集合 sum = a + b ，其中a来自A数组，b来自B数组，求 sum 中第k小的元素
# 样例1
# 输入:
# a = [1, 7, 11]
# b = [2, 4, 6]
# k = 3
# 输出: 7
# 说明: 满足条件的所有的和有[3, 5, 7, 9, 11, 13, 13, 15, 17]，其中第三个是7.
#
# 样例2
# 输入:
# a = [1, 7, 11]
# b = [2, 4, 6]
# k = 4
# 输出: 9
# 说明: 满足条件的所有的和有[3, 5, 7, 9, 11, 13, 13, 15, 17]，其中第四个是9.
#
# 样例3
# 输入:
# a = [1, 7, 11]
# b = [2, 4, 6]
# k = 8
# 输出: 15
# 说明: 满足条件的所有的和有[3, 5, 7, 9, 11, 13, 13, 15, 17]，其中第八个是15.
import heapq
class Solution:
    """
    @param A: an integer arrays sorted in ascending order
    @param B: an integer arrays sorted in ascending order
    @param k: An integer
    @return: An integer
    """
    def kthSmallestSum(self, A, B, k):
        # write your code here
        # 类似于 401 Kth smallest in sorted matrix 一题。
        # 使用heapq我们把行和列分别定为两个数组，就可以形成一个排好序的矩阵

        if not A or not B:
            return None

        n, m = len(A), len(B)
        minheap = [(A[0] + B[0], 0, 0)]
        visited = set([0])
        num = None
        for _ in range(k):
            num, x, y = heapq.heappop(minheap)
            if x + 1 < n and (x + 1) * m + y not in visited:
                heapq.heappush(minheap, (A[x + 1] + B[y], x + 1, y))
                visited.add((x + 1) * m + y)
            if y + 1 < m and x * m + y + 1 not in visited:
                heapq.heappush(minheap, (A[x] + B[y + 1], x, y + 1))
                visited.add(x * m + y + 1)

        return num