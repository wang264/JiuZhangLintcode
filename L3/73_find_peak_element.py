class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        left = 0
        right = len(A) - 1
        
        while left + 2 < right:
            mid = (left + right) // 2
            if A[mid - 1] < A[mid] > A[mid + 1]: # local max
                return mid
            elif A[mid - 1] < A[mid] < A[mid + 1]: # increasing
                left = mid
            elif A[mid - 1] > A[mid] > A[mid + 1]: # decresing
                right = mid
            elif A[mid]<A[mid -1] and A[mid]<A[mid+1]: # local min
                right = mid 
        return (left + right) // 2