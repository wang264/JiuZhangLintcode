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
        for i, c in enumerate(S):
            left, right = 0, i - 1
            while left < right:
                if S[left] + S[right] > S[i]:
                    rslt += right - left
                    right -= 1
                else:
                    left += 1

        return rslt
