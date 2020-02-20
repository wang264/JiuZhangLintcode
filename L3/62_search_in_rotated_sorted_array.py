class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        if not A:
            return -1
            
        min_index = self.find_mid_index(A)
        
        left = 0
        right = len(A) -1
        
        if A[min_index]<= target <= A[right]:
            left = min_index
        else:
            right = min_index - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                left = mid
            else:
                right = mid
        
        if A[left] == target:
            return left
        
        if A[right] == target:
            return right
        
        return -1
        
        
        
    def find_mid_index(self, nums):
        # write your code here
        if not nums:
            return -1
        
        left = 0
        right = len(nums) -1
        
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]: # need to search the left part
                right = mid
            else:
                left = mid
        
        if nums[left] < nums[right]:
            return left
        else:
            return right