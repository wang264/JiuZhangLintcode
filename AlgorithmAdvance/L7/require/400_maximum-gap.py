# 400. Maximum Gap
# 中文English
# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
#
# Return 0 if the array contains less than 2 elements.
#
# Example
# Example 1:
#
# Input: [1, 9, 2, 5]
# Output: 4
# Explanation: The sorted form is [1, 2, 5, 9], and the maximum gap is between 5 and 9.
# Example 2:
#
# Input: [1]
# Output: 0
# Explanation: The array contains less than 2 elements.
# Challenge
# Sort is easy but will cost O(nlogn) time. Try to solve it in linear time and space.
#
# Notice
# You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.


# 算法：基数排序（**Bucket sort**）
# 桶排序的思想是近乎彻底的分治思想。桶排序假设待排序的一组数均匀独立的分布在一个范围中，并将这一范围划分成几个子范围（桶）。
# 然后基于某种映射函数f ，将待排序列的关键字 k 映射到第i个桶中 (即桶数组B 的下标i) ，那么该关键字k 就作为 B[i]中的元素
# (每个桶B[i]都是一组大小为N/M 的序列 )。接着将各个桶中的数据有序的合并起来 : 对每个桶B[i] 中的所有元素进行
# 比较排序 (可以使用快排)。然后依次枚举输出 B[0]….B[M] 中的全部内容即是一个有序序列。

# 桶的实现逻辑：
#
# 设置一个定量的数组当作空桶子。
# 寻访序列，并且把项目一个一个放到对应的桶子去。
# 对每个不是空的桶子进行排序。
# 从不是空的桶子里把项目再放回原来的序列中。

# 具体实现:
#
# 假设有N个元素A到B。
# 首先我们定义 max_v 和 min_v 表示这个数组的最大/最小元素, N 表示这个数组元素的个数. 那么这个数组一共会有 N - 1 个间距
# 这 N - 1 个间距的平均值就是 avgGap =ceil (max_v - min_v) / (N - 1), 这个平均值也是答案的最小值. 因为这 N 个元素平均分配时, 最大的间距最小.
# 然后我们对这 N 个元素分类, 分类依据就是这个元素与 min_v的间距是 avgGap 的多少倍. 为什么这样分类呢? 因为这样分类, 同一组内的元素的间距必然不会是最大间距.
# 这时我们要找的最大间距处于组与组之间, 即某一组里最小的元素与它上一组的最大的元素的间距的最大值. 因此, 我们只需要维护每一组里最小与最大的元素即可.
# 令bucket（桶）的大小len = ceil[(max_v - min_v) / (N - 1)]，则最多会有(max_v -min_v) / len + 1个桶
# 对于数组中的任意整数K，很容易通过算式loc = (K - min_v) / len - 1找出其桶的位置，然后维护每一个桶的最大值和最小值
# 设定 bucket_max 和 bucket_min 数组, bucket_max[i] 表示原数组中与 bucket_min的差为 avgGap 的 i 倍(向下取整)的最大的元素, 同理 bucket_min[i] 表示相同含义下的最小的元素.
# 然后我们遍历 bucket_min, bucket_max, 将第 i 组的最小值 bucket_min[i] 与第 i - 1 组的最大值 bucket_max[i - 1] 做差, 维护最大值就可以得到答案了.

# 复杂度分析

import math


# 时间复杂度O(n)
# n为数组的大小
# 空间复杂度O(n)
# n为数组的大小


class Solution:
    """
    @param nums: an array of integers
    @return: the maximun difference
    """

    def maximumGap(self, nums):
        size = len(nums)
        if size < 2:  # 特判
            return 0;
        if size == 2:
            return abs(nums[1] - nums[0])
        int_max, int_min = 2147483647, -2147483648
        min_v, max_v = int_max, int_min
        for i in range(size):  # 找到nums中的最大最小值
            if nums[i] < min_v:
                min_v = nums[i]
            if nums[i] > max_v:
                max_v = nums[i]
        bucket_len = (float(max_v) - float(min_v)) / (size - 1)  # 计算桶的长度
        if bucket_len == 0:  # 说明nums中的所有元素值相同，答案就是0
            return 0
        bucket_min = [int_max] * size
        bucket_max = [int_min] * size
        for i in range(size):
            # 找到桶的位置
            index = math.ceil(float(nums[i] - min_v) / bucket_len) - 1
            index = max(0, index)
            if nums[i] < bucket_min[index]:
                bucket_min[index] = nums[i]
            if nums[i] > bucket_max[index]:
                bucket_max[index] = nums[i]
        res = 0
        # 对每个数入桶，然后结果肯定是这个桶的最小值和上个桶的最大值之间的差值
        for i in range(1, size):
            if bucket_min[i] == int_max and bucket_max[i] == int_min:
                bucket_min[i] = bucket_min[i - 1]
                bucket_max[i] = bucket_max[i - 1]
            else:
                res = max(res, bucket_min[i] - bucket_max[i - 1])
        return res


sol = Solution()
assert sol.maximumGap(nums=[1, 9, 2, 5]) == 4
