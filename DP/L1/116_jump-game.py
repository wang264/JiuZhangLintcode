# 116. Jump Game
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
# Example
# Example 1
#
# Input : [2,3,1,1,4],   (ex. means in index 1, the value is three, you can jump up to 3 stones to the right. )
# Output : true
# Example 2
#
# Input : [3,2,1,0,4]
# Output : false
# Notice
# This problem have two method which is Greedy and Dynamic Programming.
#
# The time complexity of Greedy method is O(n).
#
# The time complexity of Dynamic Programming method is O(n^2).
#
# We manually set the small data set to allow you pass the test in both ways. This is just to let you learn how to use
# this problem in dynamic programming ways. If you finish it in dynamic programming ways,
# you can try greedy method to make it accept again.

class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """

    def canJump(self, A):
        # write your code here
        # dp[j]=True/False, means if the frog can jump to the jth stone.
        # dp[j] = (f[0] and 0+A[0]>=j) OR (f[1] and 1+A[1]>=j)  OR (f[2] and 2+A[2]>=j) OR ..... OR (f[j-1] and j-1+A[j-1]>=j)
        # for each jth stone, we iterate through 0<=i<j, if we can reach the ith stone and can jump to jth stone from
        # the ith stone, then we can say that we can reach to jth stone.

        dp = [False] * len(A)
        dp[0] = True
        for j in range(len(dp)):
            for i in range(0, j):
                dp[j] = dp[j] or (dp[i] and i + A[i] >= j)

        return dp[-1]
