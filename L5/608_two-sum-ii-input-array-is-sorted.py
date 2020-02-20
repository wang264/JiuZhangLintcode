class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, nums, target):
        # write your code here
        if len(nums) == 0 or len(nums) == 1:
            return [-1, -1]

        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == target:
                break
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1

        return [left + 1, right + 1]


sol = Solution()
sol.twoSum(nums=[2,7,11,15], target=9)