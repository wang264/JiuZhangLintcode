# 124. Longest Consecutive Sequence
# 中文English
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# 样例
# Example 1
#
# Input : [100, 4, 200, 1, 3, 2]
# Output : 4
# Explanation : The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length:4
# 说明
# Your algorithm should run in O(n) complexity.
#
# 真正的O(N)解
#
# 而且不需要动态的从哈希或set里删除元素。
#
# 这是一个计数题，别的解法都把它弄复杂了。假设你已经掌握了dict和set，往下看：
#
# 拿那个[100, 4, 200, 1, 3, 2]样例，你该怎么数数呢？你先从100数，然后呢，就没有了。再从4开始数，唉，不对，不应该，因为后面还有3，2，1
# 所以应该把4跳过去，待会从小的数开始数。再后面是200，因为没有199，所以应该从200开始。
#
# 或者这样看，每一个连续序列都可以被这个序列的最小值代表，要找到最小值才开始数，这样无重复，才能做到O(N)O(N)。
#
# 具体来看，这个代码做了三个NN的操作：
#
# 建dict
# for循环里，看每一个数字n是否有n-1存在
# while循环，从小到大的数连续序列

class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """

    def longestConsecutive(self, nums):
        # write your code here
        max_len, table = 0, {num: True for num in nums}

        for num in nums:
            # if num-1 in the 'nums', then we skip num from now,
            # because we alway only want to start from the lowest consecutive number.
            if num - 1 in table.keys():
                continue
            else:
                num_hi = num + 1
                while num_hi in table:
                    num_hi += 1
                max_len = max(max_len, num_hi - num)

        return max_len

#
# sol =Solution()
# sol.longestConsecutive(nums=[100, 4, 200, 1, 3, 2])