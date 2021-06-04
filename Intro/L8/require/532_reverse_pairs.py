# 532 Reverse Pairs
#
# 题目题解笔记讨论排名
# 描述
# Two numbers in the array, if the previous number is greater than the following number, then the two numbers form a reverse order pair. Give you an array, find out the total number of reverse order pairs in this array.
# Summary: if a [i] > a [j] and i < j, a [i] and a [j] form a reverse order pair.
#
# 样例
# Example1
#
# Input:  A = [2, 4, 1, 3, 5]
# Output: 3
# Explanation:
# (2, 1), (4, 1), (4, 3) are reverse pairs
# Example2
#
# Input:  A = [1, 2, 3, 4]
# Output: 0
# Explanation:
# No reverse pair

class Solution:
    # @param {int[]} A an array
    # @return {int} total of reverse pairs
    def reversePairs(self, A):
        # Write your code here
        self.tmp = [0] * len(A)
        return self.mergeSort(A, 0, len(A) - 1)

    def mergeSort(self, A, l, r):
        if l >= r:
            return 0

        m = (l + r) >> 1
        ans = self.mergeSort(A, l, m) + self.mergeSort(A, m + 1, r)
        i, j, k = l, m + 1, l
        while i <= m and j <= r:
            if A[i] > A[j]:
                self.tmp[k] = A[j]
                j += 1
                ans += m - i + 1
            else:
                self.tmp[k] = A[i]
                i += 1
            k += 1

        while i <= m:
            self.tmp[k] = A[i]
            k += 1
            i += 1
        while j <= r:
            self.tmp[k] = A[j]
            k += 1
            j += 1
        for i in range(l, r + 1):
            A[i] = self.tmp[i]

        return ans

A = [2, 4, 1, 3, 5]
sol = Solution()
sol.reversePairs(A)