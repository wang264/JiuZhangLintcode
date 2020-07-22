# 183. Wood Cut
# 中文English
# Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could
# have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces
# of wood? Given L & k, return the maximum length of the small pieces.

# 183. 木材加工
# 中文English
# 有一些原木，现在想把这些木头切割成一些长度相同的小段木头，需要得到的小段的数目至少为 k。
# 当然，我们希望得到的小段越长越好，你需要计算能够得到的小段木头的最大长度。

#
# Example
# Example 1
#
# Input:
# L = [232, 124, 456]
# k = 7
# Output: 114
# Explanation: We can cut it into 7 pieces if any piece is 114cm long, however we can't cut it into 7 pieces if any piece is 115cm long.
# Example 2
#
# Input:
# L = [1, 2, 3]
# k = 7
# Output: 0
# Explanation: It is obvious we can't make it.
# Challenge
# O(n log Len), where Len is the longest length of the wood.
#
# Notice
# You couldn't cut wood into float length.
#
# If you couldn't get >= k pieces, return 0.

# 首先，我们发现。对于一个长度S,如果可以切出T段， 而对于另一个长度S'>S,可以切出T'段， 则一定有T>=T'
# 所以，如果长度S切出的段数不够K，答案S_prime肯定比S小-----》二分答案
# 同理，如果长度S切出的段数>=K，答案S_prime肯定>=S
# 时间复杂度 O(n*logL)

class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """

    def woodCut(self, L, k):
        if len(L) == 0:
            return 0
        # write your code here
        left = 0
        right = max(L)

        while left + 1 < right:
            mid = (left + right) // 2
            if self.get_number_of_pieces(L, mid) < k:  # answer must be smaller
                right = mid
            elif self.get_number_of_pieces(L, mid) > k:  # answer must be larger
                left = mid
            else:  # =k  could be an answer, but answer may be larger
                left = mid

        if self.get_number_of_pieces(L, right) == k:
            return right
        else:
            return left

    def get_number_of_pieces(self, L, length_of_each_piece):
        count = 0
        for l in L:
            count += l // length_of_each_piece
        return count


sol = Solution()
sol.woodCut(L=[232, 124, 456], k=7)
sol.woodCut(L=[4, 5, 6], k=90000)

# sol.get_number_of_pieces(L=[232, 124, 456], length_of_each_piece=30)
