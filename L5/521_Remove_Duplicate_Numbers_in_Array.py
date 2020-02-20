class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if len(nums) == 0 or len(nums) == 1:
            return nums

        n = len(nums)
        nums.sort()
        slow = 0
        fast = 1
        while fast<n:
            if nums[fast] != nums[slow]:
                nums[slow+1] = nums[fast]
                slow += 1

            fast += 1
            
        return nums