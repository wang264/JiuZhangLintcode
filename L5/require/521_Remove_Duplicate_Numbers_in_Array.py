class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """

    def deduplication(self, nums):
        # write your code here
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        nums.sort()
        count = 1
        prev = 0
        for curr in range(1, len(nums)):
            if nums[curr] != nums[prev]:
                prev += 1
                nums[prev] = nums[curr]
                count += 1
        return count
# sol = Solution()
# nums = [1, 3,1,4,4,2]
# sol.deduplication(nums)