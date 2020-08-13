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
#

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


# this is a better solution.
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
        # 第k大---->从小到大排列后的第 len(nums)-k +1 小 ---->这数的index 是len(nums)-k

        return self.partition(nums, 0, len(nums) - 1, len(nums) - n)
    # return the number k+1 smallest, which index at k. if the array is sorted.

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

        # start < right < left < end
        # left - right can equal to 2 instead of 1.
        if k <= right:
            return self.partition(nums, start, right, k)
        if k >= left:
            return self.partition(nums, left, end, k)

        return nums[k]


class Solution2:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def kthLargestElement(self, n, nums):
        if nums is None:
            return -1
        return self.quick_select(nums, 0, len(nums) - 1, n)

    def quick_select(self, nums, start, end, k):
        if start == end:
            return nums[start]
        pivot = nums[(start + end) // 2]
        left = start
        right = end
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # start <= right< left <= end
        # from start ot right there are (right - start+1) numbers
        # if k<= (right - start +1) we know that this number must be in A[start] ~~~~ A[right]
        if k <= right - start + 1:
            return self.quick_select(nums, start, right, k)
        # from start to left, there are left - start + 1 numbers,
        elif k >= left - start + 1:
            # from A[start] to A[left-1] ( A[right]) there are left - start numbers,
            # if we start counting from A[left],
            # then the kth from A[start] is the k-(left-start) from A[left]
            return self.quick_select(nums, left, end, k - (left - start))
        else:
            # because it is possible that left - right =2 instead of left-right = 1
            return nums[right+1]

sol = Solution2()

sol.kthLargestElement(3, [9, 3, 2, 4, 8])==4

nums = [595240, 373125, 463748, 417209, 209393, 747977, 864346, 419023, 925673, 307640, 597868, 833339, 130763, 814627,
        766415, 79576, 459038, 990103, 944521, 708820, 473246, 499960, 742286, 758503, 270229, 991199, 770718, 529265,
        498975, 721068, 727348, 29619, 712557, 724373, 823743, 318203, 290432, 476213, 412181, 869308, 496482, 793858,
        676162, 165869, 160511, 260864, 502521, 611678, 786798, 356560, 916620, 922168, 89350, 857183, 964051, 979979,
        916565, 186532, 905289, 653307, 351329, 195491, 866281, 183964, 650765, 675046, 661642, 578936, 78684, 50105,
        688326, 648786, 645823, 652329, 961553, 381367, 506439, 77735, 707959, 373271, 316194, 185079, 686945, 342608,
        980794, 78777, 687520, 27772, 711098, 661265, 167824, 688245, 286419, 400823, 198119, 35400, 916784, 81169,
        874377, 377128, 922531, 866135, 319912, 867697, 10904]
sol.kthLargestElement(n=105, nums=nums) == 991199
