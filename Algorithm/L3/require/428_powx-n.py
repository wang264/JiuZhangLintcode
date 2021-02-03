# 428. Pow(x, n)
# 中文English
# Implement pow(x, n). (n is an integer.)
#
# Example
# Example 1:
#
# Input: x = 9.88023, n = 3
# Output: 964.498
# Example 2:
#
# Input: x = 2.1, n = 3
# Output: 9.261
# Example 3:
#
# Input: x = 1, n = 0
# Output: 1
# Challenge
# O(logn) time
#
# Notice
# You don't need to care about the precision of your answer, it's acceptable if the expected answer and your answer 's difference is smaller than 1e-3.

class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """

    def myPow(self, x, n):
        if n >= 2 ** 31:
            return 0

        if n <= -2 ** 31:
            return 0

        if n == 0:
            return 1
        # write your code here
        is_negative = False
        if n < 0:
            is_negative = True
            n = -1 * n

        if n % 2 == 1:  # if odd
            answer = self.myPow(x, n // 2) ** 2 * x
        else:
            answer = self.myPow(x, n // 2) ** 2

        if is_negative:
            return 1 / answer
        else:
            return answer




sol = Solution()
sol.myPow(x=9.88023, n=3)

sol.myPow(x=2, n=-2147483648)
