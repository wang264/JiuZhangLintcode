class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    def sortIntegers2(self, A):
        # write your code here
        self.quickSort(A, 0, len(A) - 1)

    def quickSort(self, A, start, end):
        if start >= end:
            return

        pivot = A[(start + end) // 2]
        left, right = start, end
        # key point 2: every time you compare left & right, it should be
        # left <= right not left < right
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1

            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        self.quickSort(A, start, right)
        self.quickSort(A, left, end)


class Solution2:
    """
    @param A: an integer array
    @return: nothing
    """

    def sortIntegers2(self, A):
        # write your code here
        self.quickSort(A, 0, len(A) - 1)

    def partition(self, A, start, end):
        # use the last element as the pivot
        pivot = A[end]

        prev = start - 1
        for curr in range(start, end):
            if A[curr] > pivot:
                continue
            else:
                prev += 1
                A[prev], A[curr] = A[curr], A[prev]

        prev = prev + 1
        A[end], A[prev] = A[prev], A[end]
        return prev

    def quickSort(self, A, start, end):
        if start >= end:
            return
        idx = self.partition(A, start, end)
        self.quickSort(A, start, idx - 1)
        self.quickSort(A, idx + 1, end)


sol = Solution2()
nums = [3, 10, 7, 8, 9, 1, 5, 2, 4, 6]
sol.sortIntegers2(nums)
nums
