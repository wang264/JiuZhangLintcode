# 75. Find Peak Element
# There is an integer array which has the following features:
#
# The numbers in adjacent positions are different. A[0] < A[1] & & A[A.length - 2] > A[A.length - 1].
# We define a position P is a peak if: A[P] > A[P - 1] & & A[P] > A[P + 1]
# Find a peak element in this array.Return the index of the peak.
#
# Example 1:
# Input: [1, 2, 1, 3, 4, 5, 7, 6]
# Output: 1 or 6
#
# Explanation: return the index of peek.
#
# Example 2:
# Input: [1, 2, 3, 4, 1]
# Output: 3
#
# Challenge
# Time complexity O(logN)
#
# Notice It 's guaranteed the array has at least one peak. The array may contain multiple peeks, find
# any of them. The array has at least 3 numbers in it.

class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """

    def findPeak(self, A):
        # write your code here
        left = 0
        right = len(A) - 1

        # exit when there are two elements
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] < A[mid + 1]:  # answer must be to the right of mid
                left = mid
            elif A[mid] < A[mid - 1]:  # answer must be to the left of mid
                right = mid
            else:
                return mid

        # you can add the block below or not ~~
        # if A[left] < A[right]:
        #     return right
        # else:
        #     return left


sol = Solution()
sol.findPeak(A=[1, 2, 3, 4, 1])
sol.findPeak(A=[1, 2, 1, 3, 4, 5, 7, 6])
