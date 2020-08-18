# 15. Permutations
# 中文English
# Given a list of numbers, return all possible permutations.
#
# Example
# Example 1:
#
# Input: [1]
# Output:
# [
#   [1]
# ]
# Example 2:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
# Challenge
# Do it without recursion.
#
# Notice
# You can assume that there is no duplicate numbers in the list.
#
#

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        # write your code here
        self.results = []
        self.dfs(nums, [])
        return self.results

    def dfs(self, nums, curr_permutation):

        if len(curr_permutation) == len(nums):
            self.results.append(curr_permutation[:])
            return

        for i in range(0, len(nums)):
            if nums[i] not in curr_permutation:
                curr_permutation.append(nums[i])
                self.dfs(nums, curr_permutation)
                curr_permutation.pop()


# DFS, but use visited() to record numbers that already been selected.
class Solution2:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        rslt = []
        visited = set()
        self.dfs_helper(nums,[],visited,rslt)
        return rslt

    def dfs_helper(self,nums,curr_path, visited, rslt):
        n = len(nums)
        if len(curr_path) == n:
            rslt.append(curr_path[:])
            return

        for i in range(n):
            if nums[i] in visited:
                continue
            curr_path.append(nums[i])
            visited.add(nums[i])
            self.dfs_helper(nums,curr_path,visited,rslt)
            curr_path.pop()
            visited.remove(nums[i])

sol = Solution2()
sol.permute(nums=[1,2,3])