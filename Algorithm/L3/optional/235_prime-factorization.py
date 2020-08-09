# 235. Prime Factorization
# 中文English
# Prime factorize a given integer.
#
# Example
# Example 1:
#
# Input: 10
# Output: [2, 5]
# Example 2:
#
# Input: 660
# Output: [2, 2, 3, 5, 11]
# Notice
# You should sort the factors in ascending order.


class Solution:
    # @param {int} num an integer
    # @return {int[]} an integer array

    def primeFactorization(self, num):
        # Write your code here
        # the math we use here is that the smallest prime factor is less than sqrt(num), if num is not prime.
        # that is to say, if it can not be divided by 2 to sqrt(num), then we know that num is prime
        k = 2
        result = []
        while k * k <= num:
            while num % k == 0:
                result.append(k)
                num //= k
            k = k + 1

        # if the number is prime number
        if num > 1:
            result.append(num)

        return result


class Solution2:
    """
    @param num: An integer
    @return: an integer array
    """

    def primeFactorization(self, num):
        # write your code here
        rslt = []
        factor = 2
        while num != 1 and factor * factor <= num:
            while num % factor == 0:
                num = num // factor
                rslt.append(factor)
            factor += 1

        if num != 1:
            rslt.append(num)
        return rslt


sol = Solution()
sol.primeFactorization(num=660)
sol.primeFactorization(num=41)
