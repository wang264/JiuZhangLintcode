# class Solution:
#     # @param k & A a integer and an array
#     # @return ans a integer
#     def kthLargestElement(self, k, A):
#         if not A or k < 1 or k > len(A):
#             return None
#         return self.partition(A, 0, len(A) - 1, len(A) - k)
#
#     def partition(self, nums, start, end, k):
#         """
#         During the process, it's guaranteed start <= k <= end
#         """
#         if start == end:
#             return nums[k]
#
#         left, right = start, end
#         pivot = nums[(start + end) // 2]
#         while left <= right:
#             while left <= right and nums[left] < pivot:
#                 left += 1
#             while left <= right and nums[right] > pivot:
#                 right -= 1
#             if left <= right:
#                 nums[left], nums[right] = nums[right], nums[left]
#                 left, right = left + 1, right - 1
#
#         # left is not bigger than right
#         if k <= right:
#             return self.partition(nums, start, right, k)
#         if k >= left:
#             return self.partition(nums, left, end, k)
#
#         return nums[k]


class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def kthLargestElement(self, n, nums):
        # write your code here
        if not n or n < 1 or n > len(nums):
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

        if k <= right:
            return self.partition(nums, start, right, k)
        if k >= left:
            return self.partition(nums, left, end, k)

        return nums[k]

sol=Solution()
sol.kthLargestElement(n=3, nums=[9,3,2,4,8])



