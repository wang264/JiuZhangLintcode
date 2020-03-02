class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """

    def twoSum5(self, nums, target):
        if len(nums) < 2:
            return 0
        # write your code here
        nums.sort()

        left = 0
        right = len(nums) - 1
        ans = 0

        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                ans += right - left
                left += 1

        return ans


sol = Solution()
sol.twoSum5(nums=[-4, -3, 2, 7, 11, 15, 25], target=24)
