# 397. Longest Continuous Increasing Subsequence
# 中文English
# Give an integer array，find the longest increasing continuous subsequence in this array.
#
# An increasing continuous subsequence:
#
# Can be from right to left or from left to right.
# Indices of the integers in the subsequence should be continuous.
# Example
# Example 1:
#
# Input: [5, 4, 2, 1, 3]
# Output: 4
# Explanation:
# For [5, 4, 2, 1, 3], the LICS  is [5, 4, 2, 1], return 4.
# Example 2:
#
# Input: [5, 1, 2, 3, 4]
# Output: 4
# Explanation:
# For [5, 1, 2, 3, 4], the LICS  is [1, 2, 3, 4], return 4.
# Challenge
# O(n) time and O(1) extra space.

class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """

    def longestIncreasingContinuousSubsequence(self, A):
        n = len(A)
        if n < 2:
            return n
        f_increase = [None] * n
        f_decrease = [None] * n

        # f_increase[i],
        # the maximum length of increasing continuous subsequence(from left to right) that end at index i.
        # f_decrease[i],
        # the maximum length of decreasing continuous subsequence(from left to right) that end at index i.

        f_increase[0] = 1
        f_decrease[0] = 1

        for i in range(1, n):
            if A[i - 1] < A[i]:
                f_increase[i] = f_increase[i - 1] + 1  # if it is increasing, then we count the ith number in, so length +1
                f_decrease[i] = 1
            elif A[i - 1] > A[i]:
                f_decrease[i] = f_decrease[i - 1] + 1
                f_increase[i] = 1  # if it is decreasing, we need to restart

        return max(max(f_increase), max(f_decrease))


sol = Solution()
sol.longestIncreasingContinuousSubsequence([5, 1, 2, 3, 4])


class Solution2:
    """
    @param A: An array of Integer
    @return: an integer
    """

    def longestIncreasingContinuousSubsequence(self, A):
        if len(A) == 0:
            return 0
            # write your code here
        return max(self.helper(A), self.helper(list(reversed(A))))

    def helper(self, A):
        dp = [None] * len(A)
        # dp[i]= longest continuous increasing subsequence(from left to right)  ending at index i

        dp[0] = 1
        for i in range(1, len(A)):
            dp[i] = 1

            if A[i - 1] >= A[i]:
                continue
            dp[i] = max(dp[i - 1] + 1, dp[i])

        return max(dp)
