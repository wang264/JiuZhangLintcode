import sys

class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """

    def twoSumClosest(self, nums, target):
        # write your code here
        if len(nums) < 2:
            return None
        nums.sort()
        left = 0
        right = len(nums) - 1

        cloest_pair = []
        min_diff = sys.maxsize
        while left < right:
            if nums[left] + nums[right] < target:
                if target - nums[left] - nums[right] < min_diff:
                    min_diff = target - nums[left] - nums[right]
                    cloest_pair = [nums[left], nums[right]]
                left += 1
            elif nums[left] + nums[right] > target:
                if nums[left] + nums[right] - target < min_diff:
                    min_diff = nums[left] + nums[right] - target
                    cloest_pair = [nums[left], nums[right]]
                right -= 1
            else:
                cloest_pair = [nums[left], nums[right]]
                return 0

        return min_diff

sol = Solution()
sol.twoSumClosest(nums=[-1,-2,-3,-4,-5,-6,-100,-98,-111,-11], target=-91)