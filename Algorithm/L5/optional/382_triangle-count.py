# 382. Triangle Count
# 中文English
# Given an array of integers, how many three numbers can be found in the array, so that we can build an triangle whose three edges length is the three numbers that we find?
#
# Example
# Example 1:
#
# Input: [3, 4, 6, 7]
# Output: 3
# Explanation:
# They are (3, 4, 6),
#          (3, 6, 7),
#          (4, 6, 7)
# Example 2:
#
# Input: [4, 4, 4, 4]
# Output: 4
# Explanation:
# Any three numbers can form a triangle.
# So the answer is C(3, 4) = 4


class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """

    def triangleCount(self, S):
        # write your code here
        # 组成三角形需要是两边之和大于第三边，且两边之差小于第三边
        # if a <= b <= c   then we only need to test if a + b > c to decide if they can be triangle, other
        # requireent already satisfy.
        S.sort()
        rslt = 0
        # iterate over c
        for i, c in enumerate(S):
            idx_a, idx_b = 0, i - 1
            while idx_a < idx_b:
                a, b = S[idx_a], S[idx_b]
                if a + b > c:
                    rslt += idx_b - idx_a
                    idx_b -= 1
                else:
                    idx_a += 1

        return rslt


sol = Solution()
assert sol.triangleCount(S=[3, 4, 6, 7]) == 3
