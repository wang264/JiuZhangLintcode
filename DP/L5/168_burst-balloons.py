# 168. Burst Balloons
# 中文English
# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums.
# You are asked to burst all the balloons. If the you burst balloon i you will get
# nums[left] * nums[i] * nums[right] coins.
# Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.
#
# Find the maximum coins you can collect by bursting the balloons wisely.
#
# 样例
# Example 1:
#
# Input：[4, 1, 5, 10]
# Output：270
# Explanation：
# nums = [4, 1, 5, 10] burst 1, get coins 4 * 1 * 5 = 20
# nums = [4, 5, 10]   burst 5, get coins 4 * 5 * 10 = 200
# nums = [4, 10]    burst 4, get coins 1 * 4 * 10 = 40
# nums = [10]    burst 10, get coins 1 * 10 * 1 = 10
# Total coins 20 + 200 + 40 + 10 = 270
# Example 2:
#
# Input：[3,1,5]
# Output：35
# Explanation：
# nums = [3, 1, 5] burst 1, get coins 3 * 1 * 5 = 15
# nums = [3, 5] burst 3, get coins 1 * 3 * 5 = 15
# nums = [5] burst 5, get coins 1 * 5 * 1 = 5
# Total coins 15 + 15 + 5  = 35
# 注意事项
# You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100


class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """
    # 使用算法强化班与动态规划专题班中讲的区间动态规划。
    # dp[i][j]代表burst i + 1 ~ j - 1 这段时间的所有气球之后，只剩下 i, j 的最大收益。
    #
    # 将原来的数组前面和后面增加两个1，最后结果就是 dp[0][n - 1]（burst 掉所有气球只剩两个1）
    def maxCoins(self, nums):
        if not nums:
            return 0

        nums = [1, *nums, 1]  # insert 1 at the beginning and end.
        n = len(nums)

        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])

        return dp[0][n - 1]
