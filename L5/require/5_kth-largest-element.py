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
nums = [595240,373125,463748,417209,209393,747977,864346,419023,925673,307640,597868,833339,130763,814627,766415,79576,459038,990103,944521,708820,473246,499960,742286,758503,270229,991199,770718,529265,498975,721068,727348,29619,712557,724373,823743,318203,290432,476213,412181,869308,496482,793858,676162,165869,160511,260864,502521,611678,786798,356560,916620,922168,89350,857183,964051,979979,916565,186532,905289,653307,351329,195491,866281,183964,650765,675046,661642,578936,78684,50105,688326,648786,645823,652329,961553,381367,506439,77735,707959,373271,316194,185079,686945,342608,980794,78777,687520,27772,711098,661265,167824,688245,286419,400823,198119,35400,916784,81169,874377,377128,922531,866135,319912,867697,10904]
sol.kthLargestElement(n=105, nums=nums)



