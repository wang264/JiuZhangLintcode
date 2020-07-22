# 141. Sqrt(x)
# Implement int sqrt(int x).
#
# Compute and return the square root of x.
#
# Example1:
# Input: 0
# Output: 0
#
# Example 2:
# Input: 3
# Output: 1
#
# Explanation: return the largest integer y that y * y <= x.
#
# Example 3:
# Input: 4
# Output: 2
#
# Challenge O(log(x))

class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """

    def sqrt(self, x):
        # write your code here
        left = 0
        right = x
        while left + 1 < right:
            mid = (left + right) // 2
            if mid * mid < x:
                left = mid
            elif mid * mid > x:
                right = mid
            else:
                return mid

        if right * right <= x:
            return right
        else:
            return left


sol = Solution()
sol.sqrt(3)
sol.sqrt(0)
sol.sqrt(4)
