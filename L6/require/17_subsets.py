# 17. 子集
# 中文English
# 给定一个含不同整数的集合，返回其所有的子集。
#
# 样例 1：
#
# 输入：[0]
# 输出：
# [
#   [],
#   [0]
# ]
# 样例 2：
#
# 输入：[1,2,3]
# 输出：
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
# 挑战
# 你可以同时用递归与非递归的方式解决么？
#
# 注意事项
# 子集中的元素排列必须是非降序的，解集必须不包含重复的子集。

# 常規的DFS解法
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
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
            curr_set.append(nums[i])
            self.dfs_helper(nums, i+1, curr_set, rslt)
            curr_set.pop()

#
# sol = Solution()
# sol.subsets(nums=[1,2,3])

class Solution2:
    #一层一层的决策每个数要不要放到最后的集合里。
    def subsets(self, nums):
        nums.sort()
        index = 0
        rslt = []
        curr_set =[]
        self.search(nums, curr_set, index, rslt)
        return rslt

    def search(self, nums, curr_set, index, rslt):
        if index == len(nums):
            rslt.append(curr_set[:])
            return

        # option 1. not include current number in the subset
        self.search(nums, curr_set, index+1, rslt)
        # option 2, include current number in the subset
        curr_set.append(nums[index])
        self.search(nums, curr_set, index+1, rslt)
        curr_set.pop()