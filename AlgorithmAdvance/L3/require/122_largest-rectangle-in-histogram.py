# 122. Largest Rectangle in Histogram
# 中文English
# Given n non-negative integers representing the histogram's bar height where the
# width of each bar is 1, find the area of largest rectangle in the histogram.
#
# Example
# Example 1:
#
# Input：[2,1,5,6,2,3]
# Output：10
# Explanation：
# The third and fourth rectangular truncated rectangle has an area of 2*5=10.
# Example 2:
#
# Input：[1,1]
# Output：2
# Explanation：
# The first and second rectangular truncated rectangle has an area of 2*1=2.


class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """

    # 最大矩形一定是某个柱形往左往右直到不能前进，形成的矩形。
    # 需要知道一个数字往左和往右第一个小于这个数字的位置。
    # 单调递增栈：
    #   - 压栈时弹出来大于等于自己的值。
    #   - 最后停下来时碰到的栈顶就是左边第一个比自己小的值。
    #   - 一个数X被新来的值R弹出栈顶，那么R就是X右边第一个小于等于X的值。
    #       * 如果有相同的数，那么最靠右的Bar会求得最大的面积
    #       * 最后插入-1
    # 时间复杂度 O(n)
    def largestRectangleArea(self, height):
        # write your code here
        if height is None or len(height) == 0:
            return 0
        max_area = 0
        stack = []
        for i in range(len(height) + 1):
            if i == len(height):
                curr = -1  # 把剩下的全部踢走
            else:
                curr = height[i]
            while len(stack) != 0 and curr <= height[stack[-1]]:
                # kick
                # 对于栈顶来说，谁把它踢走，谁就是右边第一个比他小的数
                # 被踢的那个数左边第一个比他小的数字就是它在栈里的前一个数。
                h = height[stack.pop()]  # h is the height of the middle column
                if len(stack) == 0:
                    left = 0
                else:
                    left = stack[-1] + 1
                right = i - 1
                this_area = h * (right - left + 1)
                max_area = max(this_area, max_area)

            stack.append(i)

        return max_area


sol = Solution()
sol.largestRectangleArea(height=[2, 1, 5, 6, 2, 3])
sol.largestRectangleArea(height=[1, 2, 3, 4, 5])
