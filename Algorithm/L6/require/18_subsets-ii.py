class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsetsWithDup(self, nums):
        # write your code here
        nums.sort()
        curr_set = []
        rslt = []
        start_idx = 0
        self.dfs_helper(nums, start_idx, curr_set, rslt)
        return rslt

    def dfs_helper(self, nums, start_idx, curr_set, rslt):
        rslt.append(curr_set[:])

        for i in range(start_idx, len(nums)):
            if i > start_idx and nums[i] == nums[i-1]:
                continue
            curr_set.append(nums[i])
            self.dfs_helper(nums, i+1, curr_set, rslt)
            curr_set.pop()