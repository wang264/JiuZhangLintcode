# 65. Median of two Sorted Arrays
# 中文English
# There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.
#
# Example
# Example 1
#
# Input:
# A = [1,2,3,4,5,6]
# B = [2,3,4,5]
# Output: 3.5
# Example 2
#
# Input:
# A = [1,2,3]
# B = [4,5]
# Output: 3
# Challenge
# The overall run time complexity should be O(log (m+n)).
#
# Clarification
# The definition of the median:
#
# The median here is equivalent to the median in the mathematical definition.

class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """

    def findMedianSortedArrays(self, A, B):
        # write your code here
        size_a = len(A)
        size_b = len(B)
        n = size_a + size_b
        # if n is odd, this is the index for median.
        # if n is even, this index is bias towards the right. need to average with the number to its left.
        if n % 2 == 0:
            return (self.find_kth(A, B, n // 2) + self.find_kth(A, B, n // 2 + 1)) / 2.0
        return self.find_kth(A, B, n // 2 + 1)

    def find_kth(self, A, B, k):
        if len(A) == 0:
            return B[k - 1]
        if len(B) == 0:
            return A[k - 1]

        # possible median
        start = min(A[0], B[0])
        end = max(A[-1], B[-1])

        while start + 1 < end:
            mid = (start + end) // 2
            # if together there are less than k element smaller than the perpose median, then the true median
            # must larger or equal to the perpose median
            if self.count_smaller_or_equal(A, mid) + self.count_smaller_or_equal(B, mid) < k:
                start = mid
            else:
                end = mid

        if self.count_smaller_or_equal(A, start) + self.count_smaller_or_equal(B, start) >= k:
            return start

        return end

    # count the number of elements in array A that are smaller or equal to target
    def count_smaller_or_equal(self, A, target):
        n = len(A)
        left = 0
        right = n - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] <= target:
                left = mid
            else:
                right = mid

        # if left=4, then if A[4](the fifth) element is smaller that target
        # which means there are 4 elements smaller or equal to target
        if A[left] > target:
            return left
        if A[right] > target:
            return right

        return len(A)


sol = Solution()
assert sol.findMedianSortedArrays(A=[1, 2, 3, 4, 5, 6], B=[2, 3, 4, 5]) == 3.5
assert sol.findMedianSortedArrays(A=[], B=[1]) == 1
assert sol.findMedianSortedArrays(A=[5, 6, 9, 10], B=[0, 2, 3, 4])==4.5
