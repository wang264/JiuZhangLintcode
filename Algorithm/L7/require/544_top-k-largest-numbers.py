class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """

    def topk(self, nums, k):
        # write your code here
        # in descending order
        self.quick_select(nums, 0, len(nums)-1, k)
        res = nums[:k]
        res.sort(reverse=True)
        return res

    def quick_select(self, nums, start, end, k):
        if start == end:
            return

        pivot = nums[start]
        left, right = start, end

        while left <= right:
            # descending order.
            # everything larger than pivot would be put to left
            while left <= right and nums[left] > pivot:
                left += 1
            # descending order.
            # everything smaller than pivot would be put to right
            while left <= right and nums[right] < pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        # after the above while loop,
        # start < right < left < end
        # larger than pivot |||< right < left||| smaller than pivot

        # if there are more than k numbers larger than pivot, then the k-th largest
        # will be in the left part.
        if right - start + 1 >= k:
            self.quick_select(nums, start, right, k)

        # if there are less than k numbers larger than pivot, then the k-th largest
        # will be in the right part.
        # and then the k-th largest would be k-(left - start) largest.
        if left - start + 1 <= k:
            self.quick_select(nums, left, end, k - (left - start))