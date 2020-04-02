# 198. Permutation Index II
# 中文English
# Given a permutation which may contain repeated numbers, find its index in all the permutations of these numbers, which are ordered in lexicographical order. The index begins at 1.
#
# 样例
# Example 1:
#
# Input :[1,4,2,2]
# Output:3
# Example 2:
#
# Input :[1,6,5,3,1]
# Output:24


class Solution:
    def permutationIndexII(self, A):
        if A is None or len(A) == 0:
            return 0

        index, factor, multi_fact = 1, 1, 1
        counter = {}
        for i in range(len(A) - 1, -1, -1):
            counter[A[i]] = counter.get(A[i], 0) + 1
            multi_fact *= counter[A[i]]

            count = 0
            for j in range(i + 1, len(A)):
                if A[i] > A[j]:
                    count += 1

            index += count * factor // multi_fact
            factor *= (len(A) - i)

        return index