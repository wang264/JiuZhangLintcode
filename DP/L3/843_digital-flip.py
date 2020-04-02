# 843. Digital Flip
# Given an array of 01. You can flip 1 to be 0 or flip 0 to be 1.
#
# Find the minimum number of flipping steps so that the array meets the following rules:
#
# The back of 1 can be either1 or 0, but0 must be followed by 0.
# means no patten of '01'
#
# Example
# Example 1:
#
# Input: [1,0,0,1,1,1]
# Output: 2
# Explanation: Turn two 0s into 1s.
# Example 2:
#
# Input: [1,0,1,0,1,0]
# Output: 2
# Explanation: Turn the second 1 and the third 1 into 0.
# Notice
# The length of the given array n <= 100000.

import sys


class Solution:
    """
    @param nums: the array
    @return: the minimum times to flip digit
    """

    def flipDigit(self, nums):
        # f[i][j] = minimum number of flip for first i numbers,
        # that satisfy no '01' patten exist, while the ith number(nums[i-1]) is equal to j,
        n = len(nums)
        f = [[sys.maxsize] * 2 for _ in range(n + 1)]

        f[0][0] = f[0][1] = 0

        for i in range(1, n + 1):
            # when ith number nums[i-1]'s value equal to j
            for j in range(2):
                # when the (i-1)th number, nums[i-2]'s value equal to k
                for k in range(2):
                    if k == 0 and j == 1:
                        continue
                    # in order for the last digit equal to j, do we need to flip?
                    if nums[i - 1] == j:
                        flip_last_digit = 0
                    else:
                        flip_last_digit = 1
                    f[i][j] = min(f[i][j], f[i - 1][k] + flip_last_digit)

        return min(f[n][0], f[n][1])


sol = Solution()
nums = [1, 0, 1, 0, 1, 0]
sol.flipDigit(nums)
