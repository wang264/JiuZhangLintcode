class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """

    def kthSmallest(self, k, nums):
        return self.quick_select(nums, 0, len(nums) - 1, k - 1)

    # write your code here

    def quick_select(self, nums, start, end, k):
        if start == end:
            return nums[start]

        left, right = start, end
        pivot = nums[(start + end) // 2]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        # after the while loop   start <  right < left < right
        # 第k小的数在左边
        if right >= k and start <= right:
            return self.quick_select(nums, start, right, k)
        # 第k小的数在右边
        elif left <= k and left <= end:
            return self.quick_select(nums, left, end, k)
        else:
            return nums[k]
