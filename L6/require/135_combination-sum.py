# 135. 数字组合
# 中文English
# 给定一个候选数字的集合 candidates 和一个目标值 target.
# 找到 candidates 中所有的和为 target 的组合.
# 在同一个组合中, candidates 中的某个数字不限次数地出现.
#
# 样例 1:
# 输入: candidates = [2, 3, 6, 7], target = 7
# 输出: [[7], [2, 2, 3]]
#
# 样例 2:
# 输入: candidates = [1], target = 3
# 输出: [[1, 1, 1]]
#
# 注意事项
# 1.所有数值 (包括 target ) 都是正整数.
# 2.返回的每一个组合内的数字必须是非降序的.
# 3.返回的所有组合之间可以是任意顺序.
# 4.解集不能包含重复的组合.

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """

    def combinationSum(self, candidates, target):
        # write your code here
        candidates = list(sorted(set(candidates)))
        curr_path = []
        rslt = []
        start_idx = 0
        self.dfs_helper(candidates, target, start_idx, curr_path, rslt)
        return rslt

    # 递归的定义：在candidates[start ... n-1] 中找到所有的组合，他们的和为 target
    # 和前半部分的 combination 拼起来放到 results 里
    # （找到所有以 combination 开头的满足条件的组合，放到 results）
    def dfs_helper(self, candidates, target, start_idx, curr_path, rslt):
        if target == 0:
            rslt.append(curr_path[:])
            return
        if target < 0:
            return

        # 递归的拆解：挑一个数放到 combination 里
        for i in range(start_idx, len(candidates)):
            curr_path.append(candidates[i])
            self.dfs_helper(candidates, target - candidates[i], i, curr_path, rslt)
            curr_path.pop()  # backtracking


# sol = Solution()
# sol.combinationSum([2, 3, 6, 7], 7)