# 394. Coins in a Line
# 中文English
# There are n coins in a line. Two players take turns to take one or two coins from right side until
# there are no more coins left. The player who take the last coin wins.
#
# Could you please decide the first player will win or lose?
#
# If the first player wins, return true, otherwise return false.
#
# Example
# Example 1:
#
# Input: 1
# Output: true
# Example 2:
#
# Input: 4
# Output: true
# Explanation:
# The first player takes 1 coin at first. Then there are 3 coins left.
# Whether the second player takes 1 coin or two, then the first player can take all coin(s) left.
# Challenge
# O(n) time and O(1) memory

# 394. Coins in a Line
# 中文English
# There are n coins in a line. Two players take turns to take one or two coins from right side
# until there are no more coins left. The player who take the last coin wins.
#
# Could you please decide the first player will win or lose?
#
# If the first player wins, return true, otherwise return false.
#
# Example
# Example 1:
#
# Input: 1
# Output: true
# Example 2:
#
# Input: 4
# Output: true
# Explanation:
# The first player takes 1 coin at first. Then there are 3 coins left.
# Whether the second player takes 1 coin or two, then the first player can take all coin(s) left.
# Challenge
# O(n) time and O(1) memory


class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """

    def firstWillWin(self, n):
        # dp[i] with i coins on the table, the player first to act will win?
        # 如果取1个或者2个石子后，能让剩下的局面先手必败，则当前先手必胜。
        # 如果不管怎么走，剩下的局面都是先手必胜，则当前先手必败。

        # 必胜：可以从当前的局面走出一步，让对手必败。
        # 必败，自己无论怎么走，对手面对剩下的局面都必胜。
        if n == 0:
            return False
        if n == 1:
            return True

        dp = [None] * (n + 1)
        dp[1] = True
        dp[2] = True
        dp[0] = False  # the player next to act see 0 coins means it lost

        for i in range(3, n + 1):
            if dp[i - 1] is True and dp[i - 2] is True:  # 你无论拿一颗还是两颗，对手都必胜。那你必败。
                dp[i] = False
            else:
                dp[i] = True

        return dp[n]


sol = Solution()
assert sol.firstWillWin(4) is True
assert sol.firstWillWin(1) is True


