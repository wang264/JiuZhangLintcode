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



