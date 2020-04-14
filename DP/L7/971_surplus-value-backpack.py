# 971. 剩余价值背包
# 中文English
# 有一个容量为 c 的背包。
# 有 n 个 A 类物品，第 i 个 A 类物品的体积为 a[i]，物品的价值为装入该物品后背包剩余容量 * k1。
# 有 m 个 B 类物品，第 i 个 B 类物品的体积为 b[i]，物品的价值为装入该物品后背包剩余容量 * k2。
# 求最大可以获得的价值。

#
# 样例
# Example 1:
#
# Given k1 = `3`,k2 = `2`,c = ` 7`,n = `2`,m = `3`,a = `[4,3]`,b = `[1,3,2]`，return `23`.
# Input:
# 3 2 7 2 3
# [4,3]
# [1,3,2]
# Output:
# 23
#
# Explanation:
# 2 * (7-1)+2*(6-2) + 3 * (4-3) = 23
# Example 2:
#
# Given k1 = `1`,k2 = `2`,c = ` 5`,n = `1`,m = `1`,a = `[2]`,b = `[1]`，return `10`.
# Input:
# 1 2 5 1 1
# [2]
# [1]
# Output:
# 10
#
# Explanation:
# 2 * (5-1)+1*(4-2) = 10
# 注意事项
# 1 <= k1, k2, c, a[i], b[i] <= 10^7
# 1 <= n, m <= 1000
from itertools import accumulate


class Solution:
    """
    @param k1: The coefficient of A
    @param k2: The  coefficient of B
    @param c: The volume of backpack
    @param n: The amount of A
    @param m: The amount of B
    @param a: The volume of A
    @param b: The volume of B
    @return: Return the max value you can get
    """

    def getMaxValue(self, k1, k2, c, n, m, a, b):
        # Write your code here
        # 对于依次放入的两个同类物品，重量必须从小到大。
        # 所以A类和B类都是从小到大选的。

        # 双序列型
        # f[i][j] 表示取A类物品的前i个和B类物品的前j个放入背包得到的最大总价值。
        # 情况一：最后一个物品是A_i-1
        # 情况二：最后一个物品是B_j-1

        f = [[0] * (m + 1) for _ in range(n + 1)]

        a.sort()
        b.sort()
        asum = [0]+list(accumulate(a))
        bsum = [0]+list(accumulate(b))
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 and j == 0:
                    f[i][j] = 0
                    continue
                total_space = asum[i] + bsum[j]
                if total_space > c:
                    continue
                # 情况一：最后一个物品是A_i-1
                if i > 0:
                    f[i][j] = max(f[i][j], f[i - 1][j] + k1 * (c - total_space))
                # 情况二：最后一个物品是B_j-1
                if j > 0:
                    f[i][j] = max(f[i][j], f[i][j-1] + k2 * (c - total_space))

        rslt = 0
        for i in range(n + 1):
            for j in range(m + 1):
                rslt = max(rslt, f[i][j])
        return rslt