# 563. Backpack V
# 中文English
# Given n items with size nums[i] which an integer array and all positive numbers.
# An integer target denotes the size of a backpack.
# Find the number of possible ways to fill the backpack.
#
# Each item may only be used once
#
# Example
# Given candidate items [1,2,3,3,7] and target 7,
#
# A solution set is:
# [7]
# [1, 3, 3]
# return 2

class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """

    # f[i][w]= 用前i个物品拼出重量w  的方案数

    # f[i][w] = f[i-1][w] + f[i-1][w - A[i-1]]
    # 前i个物品能否拼出重量w = 前i-1拼出重量w的方案数 + 前i-1拼出重量w-A[i-1]的方案数。
    def backPackV_space_too_complex(self, nums, target):
        # write your code here
        n = len(nums)
        f = [[None] * (target + 1) for _ in range(n + 1)]

        f[0][0] = 1  # 前0个物品拼重量w
        for w in range(1, target + 1):
            f[0][w] = 0  # 前0个物品无法拼出非0的重量

        for i in range(1, n + 1):
            f[i % 2][0] = 1  # 前i个物品拼重量0
            for w in range(1, target + 1):
                # 不用第i个物品去拼
                f[i][w] = f[i - 1][w]

                # 用第i个物品去拼
                if w - nums[i - 1] >= 0:
                    f[i][w] += f[i - 1][w - nums[i - 1]]

        # 用前N个物品拼出Target的方案数
        return f[n][target]

    def backPackV_time_too_complex(self, nums, target):
        # write your code here
        n = len(nums)
        # i 只跟 i-1有关，所以只用开两行。
        f = [[None] * (target + 1) for _ in range(0, 2)]

        f[0][0] = 1  # 前0个物品拼重量w
        for w in range(1, target + 1):
            f[0][w] = 0  # 前0个物品无法拼出非0的重量

        for i in range(1, n + 1):
            f[i % 2][0] = 1  # 前i个物品拼重量0
            for w in range(1, target + 1):
                # 不用第i个物品去拼
                f[i % 2][w] = f[(i - 1) % 2][w]

                # 用第i个物品去拼
                if w - nums[i - 1] >= 0:
                    f[i % 2][w] += f[(i - 1) % 2][w - nums[i - 1]]

        # 用前N个物品拼出Target的方案数
        return f[n % 2][target]

    def backPackV(self, nums, target):
        # write your code here
        n = len(nums)
        # i 只跟 i-1有关，所以只用开两行。
        f = [[0] * (target + 1) for _ in range(0, 2)]

        f[0][0] = 1  # 前0个物品拼重量0
        for w in range(1, target + 1):
            f[0][w] = 0  # 前0个物品无法拼出非0的重量

        prefix_sum = 0
        for i in range(1, n + 1):
            f[i % 2][0] = 1  # 前i个物品拼重量0
            prefix_sum += nums[i - 1]
            # 没有必要每次都算到 target 那么多的值。
            # 例如: i=2. nums=[2,4,5,1,4], target=10, 用前两个最多能拼到w=2+4=6, w>6的情况下一定是0， 我们直接在
            # 初始化的时候就设好为0
            for w in range(1, min(target, prefix_sum) + 1):
                # 不用第i个物品去拼
                f[i % 2][w] = f[(i - 1) % 2][w]

                # 用第i个物品去拼
                if w - nums[i - 1] >= 0:
                    f[i % 2][w] += f[(i - 1) % 2][w - nums[i - 1]]

        # 用前N个物品拼出Target的方案数
        return f[n % 2][target]


nums = [1, 2, 3, 3, 7]
target = 7
sol = Solution()
sol.backPackV(nums, target)
