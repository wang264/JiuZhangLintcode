# 5. Kth Largest Element
# 中文English
# Find K-th largest element in an array.
#
# Example
# Example 1:
#
# Input:
# n = 1, nums = [1,3,4,2]
# Output:
# 4
# Example 2:
#
# Input:
# n = 3, nums = [9,3,2,4,8]
# Output:
# 4
# Challenge
# O(n) time, O(1) extra memory.
#
# Notice
# You can swap elements in the array


class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def kthLargestElement(self, n, nums):
        # use quick select template
        if n is None or n < 1 or n > len(nums):
            return None

        return self.partition(nums, 0, len(nums) - 1, len(nums) - n)

    def partition(self, nums, start, end, k):
        if start == end:
            return nums[k]
        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
        # at this stage, start < right < left < end
        if k <= right:
            return self.partition(nums, start, right, k)
        if k >= left:
            return self.partition(nums, left, end, k)
        # if right<k<left
        return nums[k]


sol = Solution()
assert sol.kthLargestElement(n=1, nums=[1, 3, 4, 2]) == 4
assert sol.kthLargestElement(n=3, nums=[9, 3, 2, 4, 8]) == 4
assert sol.kthLargestElement(n=5, nums=[1, 20, 9, 3, 2, 4, 8, 10, 11, 13, 21]) == 10
assert sol.kthLargestElement(n=7, nums=[1, 20, 9, 3, 2, 4, 8, 10, 11, 13, 21]) == 8
