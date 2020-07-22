# 586. Sqrt(x) II
# 中文English
# Implement double sqrt(double x) and x >= 0.
#
# Compute and return the square root of x.
#
# Example
# Example 1:
#
# Input: n = 2
# Output: 1.41421356
# Example 2:
#
# Input: n = 3
# Output: 1.73205081
# Notice
# You do not care about the accuracy of the result, we will help you to output results.


class Solution:
    """
    @param x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        # write your code here
        left = 0
        if x<1:
            right=1
        else:
            right = x
        while left + 1e-10 < right:
            mid = (left+right)/2
            if mid*mid<x:
                left = mid
            elif mid*mid>x:
                right =mid
            else:
                return mid

        return left

sol = Solution()
sol.sqrt(3)
sol.sqrt(2)
sol.sqrt(0.1)
