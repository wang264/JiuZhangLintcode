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
        # write your code here
        if not nums:
            return 0
        nums = [1, *nums, 1] # insert 1 at the beginning and end.
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for j in range(length - 1, n):  # end idx
                i = j - length + 1  # start idx
                # iterate k,    i<k<j # 在i, j 区间（i,j不被扎破)枚举最后一个被扎破的气球K。
                k = i + 1
                while k < j:
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
                    k += 1
        return dp[0][n - 1]


sol = Solution()
sol.maxCoins(nums=[4, 1, 5, 10])
