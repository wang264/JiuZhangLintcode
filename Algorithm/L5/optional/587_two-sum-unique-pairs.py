class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """

    def twoSum6(self, nums, target):
        # write your code here
        if len(nums) < 2:
            return 0

        nums.sort()
        ans = 0
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                ans += 1
                left += 1
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

            elif nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1

        return ans


sol = Solution()
sol.twoSum6(nums=[7, 11, 11, 1, 2, 3, 4], target=22)
