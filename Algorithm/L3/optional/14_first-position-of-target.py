class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        # write your code here
        left, right = 0, len(nums)-1
        while left + 1 < right :
            mid = (left + right) // 2
            if nums[mid] < target :
                left = mid
            else :
                right = mid
        if nums[left] == target :
            return left
        elif nums[right] == target :
            return right
        return -1;