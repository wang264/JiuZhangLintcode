# 52. Next Permutation
# 中文English
# Given a list of integers, which denote a permutation.
#
# Find the next permutation in ascending order.
#
# 样例
# Example 1:
#
# Input:[1]
# Output:[1]
# Example 2:
#
# Input:[1,3,2,3]
# Output:[1,3,3,2]
# Example 3:
#
# Input:[4,3,2,1]
# Output:[1,2,3,4]
# 注意事项
# The list may contains duplicate integers.


# 这道题让我们求下一个排列顺序，由题目中给的例子可以看出来，如果给定数组是降序，则说明是全排列的最后一种情况，则下一个排列就是最初始情况，可以参见之前的博客 Permutations。再来看下面一个例子，有如下的一个数组
#
# 1　　2　　7　　4　　3　　1
#
# 下一个排列为：
#
# 1　　3　　1　　2　　4　　7
#
# 那么是如何得到的呢，我们通过观察原数组可以发现，如果从末尾往前看，数字逐渐变大，到了2时才减小的，然后再从后往前找第一个比2大的数字，是3，那么我们交换2和3，再把此时3后面的所有数字转置一下即可，步骤如下：
#
# 1　　[2]　　7　　  4　　  3　　  1
#
# 1　　[2]　　7　　  4　　 [3]　　 1
#
# 1　　[3]　　7　　  4　　 [2]　　 1
#
# 1　　3　　 [1]　　[2]　　[4]　　[7]

class Solution:
    """
    @param nums: An array of integers
    @return: nothing
    """

    def nextPermutation(self, nums):
        # write your code here
        # find the first not increasing number from the right
        for i in reversed(range(0, len(nums) - 1)):
            if nums[i] < nums[i + 1]:
                # from right to nums[i+1] find the first number it encounter that are larger than nums[i]
                for j in reversed(range(i, len(nums))):
                    if nums[j] > nums[i]:
                        break
                # swap the two numbers
                nums[i], nums[j] = nums[j], nums[i]
                # reverse from nums[i+1] to the end
                self.reverse_helper(nums, i + 1, len(nums) - 1)
                return nums

        self.reverse_helper(nums, 0, len(nums) - 1)
        return nums

    def reverse_helper(self, nums, left, right):
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

#
# a = [1, 2, 7, 4, 3, 1]
# sol = Solution()
# sol.nextPermutation(nums=a)
