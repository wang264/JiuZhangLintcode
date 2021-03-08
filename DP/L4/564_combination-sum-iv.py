# 564. Combination Sum IV
# 中文English
# Given an integer array nums with all positive numbers and no duplicates, find the number of
# possible combinations that add up to a positive integer target.
#
# Example
# Example1
#
# Input: nums = [1, 2, 4], and target = 4
# Output: 6
# Explanation:
# The possible combination ways are:
# [1, 1, 1, 1]
# [1, 1, 2]
# [1, 2, 1]
# [2, 1, 1]
# [2, 2]
# [4]
# Example2
#
# Input: nums = [1, 2], and target = 4
# Output: 5
# Explanation:
# The possible combination ways are:
# [1, 1, 1, 1]
# [1, 1, 2]
# [1, 2, 1]
# [2, 1, 1]
# [2, 2]
# Notice
# A number in the array can be used multiple times in the combination.
# Different orders are counted as different combinations.

class SolutionDfsSlow:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """

    def backPackVI(self, nums, target):
        # write your code here
        rslt = [0]
        curr_path = []
        self.dfs_helper(nums, target, curr_path, curr_sum=0, rslt=rslt)

        return rslt[0]

    def dfs_helper(self, nums, target, curr_path, curr_sum, rslt):
        if curr_sum > target:
            return
        if curr_sum == target:
            rslt[0] += 1
            return
        for num in nums:
            curr_path.append(num)
            curr_sum += num
            self.dfs_helper(nums, target, curr_path, curr_sum, rslt)
            curr_path.pop()
            curr_sum -= num


class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """

    def backPackVI(self, nums, target):
        # write your code here
        # f[i] = 有多少种组合能拼出重量i
        # f[i] = 枚举最后一个包里的物品nums[0], nums[1] ... nums[n-1]。
        # f[i] = f[i - nums[0]] + f[i - nums[1]] ... + f[i - nums[n-1]]

        f = [None] * (target + 1)
        f[0] = 1
        for i in range(1, target + 1):
            f[i] = 0
            for j in range(len(nums)):
                # 如果最后一个物品为j, 有多少种组合能组成 i-nums[j] 的重量。
                if i - nums[j] < 0:
                    continue
                f[i] += f[i - nums[j]]

        return f[target]


sol = Solution()
nums = [1, 2, 4]
target = 4
sol.backPackVI(nums, target)

sol.backPackVI([1, 2, 4], 32)

sol.backPackVI(nums=[2, 3, 4, 5], target=7)


class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackVI(self, nums, target):
        # write your code here
        nums.sort()
        weight_to_ways = dict()

        rslt = self.dfs(nums,weight_to_ways,target)
        return rslt

    def dfs(self,nums,weight_to_ways,target):
        if target in weight_to_ways.keys():
            return weight_to_ways[target]

        if target==0:
            return 1
        if target <0:
            return 0

        rslt = 0
        for num in nums:
            if target-num>=0:
                rslt +=self.dfs(nums,weight_to_ways,target-num)
            else:
                break
        weight_to_ways[target]=rslt
        return rslt
