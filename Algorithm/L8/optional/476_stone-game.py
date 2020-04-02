# 476. Stone Game
# 中文English
# There is a stone game.At the beginning of the game the player picks n piles of stones in a line.
#
# The goal is to merge the stones in one pile observing the following rules:
#
# 1.At each step of the game,the player can merge two adjacent piles to a new pile.
# 2.The score is the number of stones in the new pile.
# You are to determine the minimum of the total score.
#
# 样例
# Example 1:
#
# Input: [3, 4, 3]
# Output: 17
# Example 2:
#
# Input: [4, 1, 1, 4]
# Output: 18
# Explanation:
#   1. Merge second and third piles => [4, 2, 4], score = 2
#   2. Merge the first two piles => [6, 4]，score = 8
#   3. Merge the last two piles => [10], score = 18

import sys
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """

    def stoneGame(self, A):
        return self.memo_search(A, 0, len(A) - 1, {})

    def memo_search(self, A, start, end, memo):
        if (start, end) in memo:
            return memo[(start, end)]

        if start >= end:
            return 0

        cost = sum(A[start:end + 1])
        minimum = sys.maxsize
        for mid in range(start, end):
            left = self.memo_search(A, start, mid, memo)
            right = self.memo_search(A, mid + 1, end, memo)
            minimum = min(minimum, left + right + cost)

        memo[(start, end)] = minimum
        return minimum

#
# sol =Solution()
# sol.stoneGame(A=[4,1,1,4])