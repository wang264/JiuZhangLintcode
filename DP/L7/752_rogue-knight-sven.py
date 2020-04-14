# 752. Rogue Knight Sven
# 中文English
# In material plane "reality", there are n + 1 planets, namely planet 0, planet 1, ..., planet n.
# Each planet has a portal through which we can reach the target planet directly without passing through other planets.
# But portal has two shortcomings.
# First, planet i can only reach the planet whose number is greater than i, and the difference between i can not exceed the limit.
# Second, it takes cost[j] gold coins to reach the planet j through the portal.
# Now, Rogue Knight Sven arrives at the planet 0 with m gold coins, how many ways does he reach the planet n through the portal?
#
# 样例
# Example 1:
# Input:
# n = 1
# m = 1
# limit = 1
# cost = [0, 1]
# Output:
# 1
# Explanation:
# Plan 1: planet 0 → planet 1

# Example 2:
# Input:
# n = 1
# m = 1
# limit = 1
# cost = [0,2]
# Output:
# 0
# Explanation:
# He can not reach the target planet.
# 注意事项
# 1 <= n <= 50, 0 <= m <= 100, 1 <= limit <= 50,0 <= cost[i] <= 100。
# The problem guarantees cost [0] = 0, cause cost[0] does not make sense

class Solution:
    """
    @param n: the max identifier of planet.
    @param m: gold coins that Sven has.
    @param limit: the max difference.
    @param cost: the number of gold coins that reaching the planet j through the portal costs.
    @return: return the number of ways he can reach the planet n through the portal.
    """

    def getNumberOfWays(self, n, m, limit, cost):
        # f[i][j] 有多少种方式从星球0跳到星球i，手里还剩j枚金币。 i是坐标，j是状态。
        f = [[0] * (m+1) for _ in range(n + 1)]

        for i in range(0, n + 1):
            for j in range(0, m + 1):
                if i == 0:
                    if j == m:
                        f[i][j] = 1  # 初始时在星球0，手里有m个金币。
                        continue
                    else:
                        f[i][j] = 0  # 无法在星球0有非m个金币

                for k in range(1, limit + 1):
                    prev_planet = i - k
                    # 从prev_planet跳过来，在prev_planet时候手上有j+cost[i]个金币。
                    if prev_planet >= 0 and j + cost[i] <= m:
                        f[i][j] += f[prev_planet][j + cost[i]]

        return sum(f[n])


sol = Solution()
n = 1
m = 1
limit = 1
cost = [0, 1]

sol.getNumberOfWays(n, m, limit, cost)
