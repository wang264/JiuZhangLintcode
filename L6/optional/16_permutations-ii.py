# 16. 带重复元素的排列
# 中文English
# 给出一个具有重复数字的列表，找出列表所有不同的排列。
#
# 样例 1：
# 输入：[1,1]
# 输出：
# [
#   [1,1]
# ]
# 样例 2：
# 输入：[1,2,2]
# 输出：
# [
#   [1,2,2],
#   [2,1,2],
#   [2,2,1]
# ]
#
# 挑战
# 使用递归和非递归分别完成该题。
class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        rslt = []
        selected = [False for _ in range(len(nums))]
        nums.sort()
        self.dfs_helper(nums, [], selected, rslt)
        return rslt

    def dfs_helper(self, nums, curr_permute, selected, rslt):
        if len(curr_permute) == len(nums):
            rslt.append(curr_permute[:])
            return

        for i in range(len(nums)):

            if selected[i]:
                continue
            # 1' 1" 2
            # => 1' 1" 2 => √
            # => 1" 1' 2 => x
            # 不能跳过上一个1选下一个1
            if i > 0 and nums[i] == nums[i - 1] and not selected[i - 1]:
                continue

            selected[i] = True
            curr_permute.append(nums[i])
            self.dfs_helper(nums, curr_permute, selected, rslt)
            selected[i] = False
            curr_permute.pop()
