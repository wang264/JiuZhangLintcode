class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """

    def partitionArray(self, nums, k):
        # write your code here
        if len(nums) == 0:
            return 0

        left = 0
        right = len(nums) - 1
        pivot = k

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] >= pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1

        return left


class Solution2:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """

    def partitionArray(self, nums, k):
        # write your code here
        n = len(nums)
        if n == 0:
            return 0

        # pivot is  k
        prev = -1
        for curr in range(0, n):
            if nums[curr] >= k:
                continue
            else:  # if nums[curr] < k
                prev += 1
                nums[prev], nums[curr] = nums[curr], nums[prev]

        return prev + 1


sol = Solution2()
sol.partitionArray(nums=[3, 2, 2, 1], k=2)
