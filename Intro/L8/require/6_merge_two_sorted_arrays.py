# 6 Merge Two Sorted Arrays
#
# Merge two given sorted ascending integer array A and B into a new sorted integer array.
#
# Example 1:
# Input:
# A = [1]
# B = [1]
# Output:
#
# [1,1]
# Explanation:
# return array merged.
#
# Example 2:
# Input:
#
# A = [1,2,3,4]
# B = [2,4,5,6]
# Output:
#
# [1,2,2,3,4,4,5,6]
#
# 挑战
# How can you optimize your algorithm if one array is very large and the other is very small?

class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """

    def mergeSortedArray(self, A, B):
        # write your code here
        len_a = len(A)
        len_b = len(B)

        if len_a == 0:
            return B
        if len_b == 0:
            return A

        idx_a = 0
        idx_b = 0
        rslt = []
        # have not finish either array
        while idx_a < len_a and idx_b < len_b:
            if A[idx_a] < B[idx_b]:
                rslt.append(A[idx_a])
                idx_a += 1
            else:
                rslt.append(B[idx_b])
                idx_b += 1

        # if only b left
        if idx_a == len_a:
            arr = B
            idx = idx_b
        else:
            arr = A
            idx = idx_a

        while idx < len(arr):
            rslt.append(arr[idx])
            idx += 1

        return rslt


A = [1,2,3,4]
B = [2,4,5,6]
sol=Solution()
sol.mergeSortedArray(A,B)