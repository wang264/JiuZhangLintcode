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
        self.dfs_helper(nums, 0, k, [], rslt)
        return rslt

    def dfs_helper(self, nums, start_idx, nums_left, curr_choice, rslt):
        if nums_left == 0:
            rslt.append(curr_choice[:])

        for i in range(start_idx, len(nums)):
            curr_choice.append(nums[i])
            self.dfs_helper(nums, i+1, nums_left-1, curr_choice, rslt)
            curr_choice.pop()


class Solution2:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        curr_path = []
        curr_num = 1
        rslt = []
        self.dfs_helper(n, curr_num, k, curr_path, rslt)
        return rslt

    def dfs_helper(self, n, curr_num, k, curr_path, rslt):
        if len(curr_path) == k:
            rslt.append(curr_path[:])

        for num in range(curr_num,n+1):
            curr_path.append(num)
            self.dfs_helper(n, num+1,k,curr_path,rslt)
            curr_path.pop()

sol =Solution2()
sol.combine(n=4,k=2)