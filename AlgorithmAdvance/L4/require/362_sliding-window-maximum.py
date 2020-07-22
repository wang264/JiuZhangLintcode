# 362. Sliding Window Maximum
# 中文English
# Given an array of n integer with duplicate number, and a moving window(size k), move the window at each
# iteration from the start of the array, find the maximum number inside the window at each moving.
#
# Example
# Example 1:
#
# Input:
# [1,2,7,7,8]
# 3
# 输出:
# [7,7,8]
#
# Explanation：
# At first the window is at the start of the array like this `[|1, 2, 7| ,7, 8]` , return the maximum `7`;
# then the window move one step forward.`[1, |2, 7 ,7|, 8]`, return the maximum `7`;
# then the window move one step forward again.`[1, 2, |7, 7, 8|]`, return the maximum `8`;
# Example 2:
#
# Input:
# [1,2,3,1,2,3]
# 5
# Output:
# [3,3]
#
# Explanation:
# At first, the state of the window is as follows: ` [,2,3,1,2,1 | , 3] `, a maximum of ` 3 `;
# And then the window to the right one. ` [1, | 2,3,1,2,3 |] `, a maximum of ` 3 `;
# Challenge
# o(n) time and O(k) memory


# 类似单调栈， 但是两端都有操作
# 基本思想：如果 A[i] <= A[j] 而且 i < j, 那么A[i]就没有用了， 即以后永远不会成为窗口最大值。
# 因为 A[i] 比A[j]先被移除出窗口，但是A[j]还比A[i]大。。

# 窗口向右移动，左端元素移出队首（如果仍在队列中），右端元素A[j]移进队尾，并删除所有 小于或等于A[j]的元素。。

from collections import deque


class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """

    def maxSlidingWindow(self, nums, k):
        # write your code here
        rslt = []
        de_que = deque()

        if len(nums) == 0:
            return rslt

        # 先把前k-1个数扔进去
        for i in range(0, k - 1):
            self.add_to_queue(de_que, nums, idx=i)

        for i in range(k - 1, len(nums)):
            self.add_to_queue(de_que, nums, idx=i)
            rslt.append(nums[de_que[0]])
            self.remove_from_queue(de_que, nums, idx=i - (k - 1))

        return rslt

    def add_to_queue(self, de_que: deque, nums, idx):
        # 右端元素A[j]移进队尾，并删除所有 小于或等于A[j]的元素。。
        while len(de_que) != 0 and nums[de_que[-1]] <= nums[idx]:
            de_que.pop()

        de_que.append(idx)

    def remove_from_queue(self, de_que: deque, nums, idx):
        # 窗口向右移动，左端元素移出队首（如果仍在队列中）
        if de_que[0] == idx:
            de_que.popleft()


sol = Solution()
sol.maxSlidingWindow(nums=[1, 2, 7, 7, 8], k=3)
