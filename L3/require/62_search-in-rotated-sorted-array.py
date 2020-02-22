class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        if not A:
            return -1
        # write your code here
        min_idx = self.find_min_index(A)
        if A[min_idx]<=target<=A[len(A)-1]:
            return self.binary_search(A,left=min_idx,right=len(A)-1, target=target)
        else:
            return self.binary_search(A, left=0, right=min_idx-1 ,target=target)

    def binary_search(self,nums, left, right, target):

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                return mid

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1

    def find_min_index(self, A):
        left = 0
        right = len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid]>A[right]:
                left = mid
            else:
                right = mid

        if A[left] < A[right]:
            return left
        else:
            return right