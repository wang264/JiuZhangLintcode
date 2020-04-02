class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """

    def moveZeroes(self, nums):
        # write your code here
        if len(nums) == 0 or len(nums) == 1:
            return nums

        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1

        while slow < len(nums):
            nums[slow] = 0
            slow += 1