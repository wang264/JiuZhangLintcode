# 197. Permutation Index
# 中文English
# Given a permutation which contains no repeated number, find its index in all the permutations of these numbers, which are ordered in lexicographical order. The index begins at 1.
#
# 样例
# Example 1:
#
# Input:[1,2,4]
# Output:1
# Example 2:
#
# Input:[3,2,1]
# Output:6


# 解题方法
# 例如给定一个排列 356421， 因为第一位为3，因此1 和 2 开头的全排列已经经过了，以1开头的全排列个数为5!，2也是。
# 因此该全排列的排名 > 2 * 5!
# 第二位为5，对于以3开头的全排列，排在35前面的有31,32,34开头的三个全排列。在356421中，5右边比5小的也正是1,2,4。
# 我们可以发现：序列长度为n，对于给定排列P某位上的数，假设这个数在P上从右起排第m位，
# 我们只要看看该数右侧的位数上还有几个比它小的，就知道该数以右的部分在对应所有子序列中的排名了。

import math


class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """

    def permutationIndex(self, A):
        # write your code here
        index = 1
        for i in range(len(A)):
            # count is to count how many number is smaller than A[i] from A[i+1] to end
            count = 0
            for j in range(i + 1, len(A)):
                if A[j] < A[i]:
                    count += 1

            factor = math.factorial(len(A) - 1 - i)
            index += factor * count

        return index
#
# sol = Solution()
# sol.permutationIndex(A=[3, 5, 6, 4, 2, 1])