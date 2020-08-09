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
