# 总的来说就是不断将divisor 乘2 直到它大于dividend.
# 记录下来以后更新dividend，复原divisor和count.

class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """

    def divide(self, dividend, divisor):
        # write your code here
        negative = False
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            negative = True

        ans, count, b, a = 0, 1, abs(divisor), abs(dividend)
        while a >= b:
            # divisor 一直乘2
            b = b << 1

            # 如果乘完还小，那ok,记录当前乘了多少
            if b <= a:
                count = count << 1

            # 如果乘完大了，就后退一步，更新剩余的dividend, 还原divisor, 记录上一步乘了多少，还原count
            else:
                b = b >> 1
                a = a - b
                b = abs(divisor)
                ans += count
                count = 1

        if negative:
            ans = -ans
        if ans > 2147483647:
            return 2147483647
        return ans


sol = Solution()
sol.divide(100, 9)


