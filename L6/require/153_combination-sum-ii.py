# 153. 数字组合 II
# 给定一个数组 num 和一个整数 target. 找到 num 中所有的数字之和为 target 的组合.
#
# 样例 1:
# 输入: num = [7,1,2,5,1,6,10], target = 8
# 输出: [[1,1,6],[1,2,5],[1,7],[2,6]]
#
# 样例 2:
# 输入: num = [1,1,1], target = 2
# 输出: [[1,1]]
# 解释: 解集不能包含重复的组合
#
# 注意事项
# 1.在同一个组合中, num 中的每一个数字仅能被使用一次.
# 2.所有数值 (包括 target ) 都是正整数.
# 3.返回的每一个组合内的数字必须是非降序的.
# 4.返回的所有组合之间可以是任意顺序.
# 5.解集不能包含重复的组合.


class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """

    def combinationSum2(self, candidates, target):
        # write your code here
        candidates.sort()
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
            # 去重逻辑，在某次dfs中，对于该次dfs可能访问到的node,
            # 如果该node不是第一个，且与之前的node.val相等，则continue.
            # for example. if we have [1,1,1,2,2,2,3,3] we label them as
            # [1_a, 1_b, 1_c, 2_a, 2_b, 2_c, 3_a, 3_b] to prevent duplicate result
            # we can only allow each time to select 1_a< 1_b< 1_c if we try to select 1_b before 1_a,
            # we should not allow that.
            if i != start_idx and candidates[i - 1] == candidates[i]:
                continue
            curr_path.append(candidates[i])
            # dfs递归的时候+1, 跳过重复使用当前数字。
            self.dfs_helper(candidates, target - candidates[i], i + 1, curr_path, rslt)
            curr_path.pop()  # backtracking
