# 4. Ugly Number II
# 中文English
# Ugly number is a number that only have prime factors 2, 3 and 5.
#
# Design an algorithm to find the nth ugly number. The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...
#
# Example
# Example 1:
#
# Input: 9
# Output: 10
# Example 2:
#
# Input: 1
# Output: 1
# Challenge
# O(n log n) or O(n) time.
#
# Notice
# Note that 1 is typically treated as an ugly number.
#
# 这道题是之前那道 Ugly Number 的拓展，这里让找到第n个丑陋数，还好题目中给了很多提示，基本上相当于告诉我们解法了，根据提示中的信息，丑陋数序列可以拆分为下面3个子列表：
#
# (1) 1x2,  2x2, 2x2, 3x2, 3x2, 4x2, 5x2...
# (2) 1x3,  1x3, 2x3, 2x3, 2x3, 3x3, 3x3...
# (3) 1x5,  1x5, 1x5, 1x5, 2x5, 2x5, 2x5...
# 仔细观察上述三个列表，可以发现每个子列表都是一个丑陋数分别乘以 2，3，5，而要求的丑陋数就是从已经生成的序列中取出来的，每次都从三个列表中取出当前最小的那个加入序列，请参见代码如下：

class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """

    def nthUglyNumber(self, n):
        l = [1]
        p1, p2, p3 = 0, 0, 0

        while len(l) < n:
            v2 = l[p1] * 2
            v3 = l[p2] * 3
            v5 = l[p3] * 5
            minV = min(v2, v3, v5)
            if v2 == minV:
                p1 += 1
            if v3 == minV:
                p2 += 1
            if v5 == minV:
                p3 += 1
            l.append(minV)
        return l[-1]
#
# sol=Solution()
# sol.nthUglyNumber(n=20)
