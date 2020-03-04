# 152. 组合
# 中文English
# 给定两个整数 n 和 k. 返回从 1, 2, ... , n 中选出 k 个数的所有可能的组合.

# 样例 1:
# 输入: n = 4, k = 2
# 输出: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

# 样例 2:
# 输入: n = 4, k = 1
# 输出: [[1],[2],[3],[4]]

# 注意事项
# 你可以以任意顺序返回所有的组合, 但是一个组合内的所有数字需要是升序排列的.

class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        nums = [x for x in range(1, n+1)]
        rslt = []
        self.dfs_helper(nums, 0, k,[], rslt)
        return rslt

    def dfs_helper(self, nums, start_idx, nums_left, curr_choice, rslt):
        if nums_left == 0:
            rslt.append(curr_choice[:])

        for i in range(start_idx, len(nums)):
            curr_choice.append(nums[i])
            self.dfs_helper(nums, i+1, nums_left-1, curr_choice, rslt)
            curr_choice.pop()