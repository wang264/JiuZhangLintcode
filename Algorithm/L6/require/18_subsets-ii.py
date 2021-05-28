# 18. Subsets II
# 中文English
# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
#
# Example
# Example 1:
#
# Input: [0]
# Output:
# [
#   [],
#   [0]
# ]
# Example 2:
#
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
# Challenge
# Can you do it in both recursively and iteratively?
#
# Notice
# Each element in a subset must be in non-descending order.
# The ordering between two subsets is free.
# The solution set must not contain duplicate subsets.

class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """

    def subsetsWithDup(self, nums):
        # write your code here
        nums.sort()
        rslt = []
        self.dfs_helper(nums, 0, [], rslt)
        return rslt

    def dfs_helper(self, nums, start_idx, curr_path, rslt):

        rslt.append(curr_path[:])
        for idx in range(start_idx, len(nums)):
            # remove duplicate
            # 去重逻辑，在某次dfs中，对于该次dfs可能访问到的node,
            # 如果该node不是第一个，且与之前的node.val相等，则continue.
            # for example. if we have [1,1,1,2,2,2,3,3] we label them as
            # [1_a, 1_b, 1_c, 2_a, 2_b, 2_c, 3_a, 3_b] to prevent duplicate result
            # we can only allow each time to select 1_a< 1_b< 1_c if we try to select 1_b before 1_a,
            # we should not allow that.
            if idx > 0 and idx != start_idx and nums[idx] == nums[idx - 1]:
                continue
            curr_path.append(nums[idx])
            self.dfs_helper(nums, idx + 1, curr_path, rslt)
            curr_path.pop()


sol = Solution()
sol.subsetsWithDup(nums=[1, 1, 1, 2, 2])
sol.subsetsWithDup(nums=[0])
sol.subsetsWithDup(nums=[4, 1, 0]) == [[], [0], [0, 1], [0, 1, 4], [0, 4], [1], [1, 4], [4]]
