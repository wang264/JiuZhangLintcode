import math


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