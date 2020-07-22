# 414. Divide Two Integers
# 中文English
# Divide two integers without using multiplication, division and mod operator.
#
# If it will overflow(exceeding 32-bit signed integer representation range), return 2147483647
#
# The integer division should truncate toward zero.
#
# Example
# Example 1:
#
# Input: dividend = 0, divisor = 1
# Output: 0
# Example 2:
#
# Input: dividend = 100, divisor = 9
# Output: 11


class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """

    def divide(self, dividend, divisor):
        # write your code here
        ans = 0
        negate = False
        if dividend < 0 and divisor < 0:
            dividend = -1 * dividend
            divisor = -1 * divisor
        elif divisor < 0:
            negate = True
            divisor = -1 * divisor
        elif dividend < 0:
            negate = True
            dividend = -1 * dividend

        while dividend >= divisor:
            count = 1
            temp_val = divisor
            while dividend >= temp_val:
                dividend -= temp_val
                ans += count
                temp_val = temp_val << 1
                count = count << 1

        if negate:
            ans = -1 * ans

        if ans >= 1 << 31:
            ans = (1 << 31) - 1
        return ans

sol = Solution()
assert sol.divide(100, 9) == 100 // 9
assert sol.divide(1, 1) == 1
assert sol.divide(-2147483648,-1) == 2147483647