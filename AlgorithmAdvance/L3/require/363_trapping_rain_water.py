# 363. Trapping Rain Water
# 中文English
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.
#
# 363. 接雨水
# 中文English
# 给出 n 个非负整数，代表一张X轴上每个区域宽度为 1 的海拔图, 计算这个海拔图最多能接住多少（面积）雨水。
# Trapping Rain Water
#
# Example
# Example 1:
#
# Input: [0,1,0]
# Output: 0
# Example 2:
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Challenge
# O(n) time and O(1) memory
#
# O(n) time and O(n) memory is also acceptable.
class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """

    # for each cell/location heights[i]
    # the amount of rain water it can trap is
    # left_max -> max (heights[0]...heights[i])
    # right_max -> max (heights[i]...heights[-1])
    # amount_rain_trap = min(left_max, right_max) - heights[i]
    def trapRainWater(self, heights):
        if len(heights) ==0 :
            return 0
        # write your code here
        # iterate from left to right, find the maximum of the ith cell to heights[0]
        left_max = []
        right_max = []
        temp_max = heights[0]
        for height in heights:
            if height >= temp_max:
                left_max.append(height)
                temp_max = height
            else:
                left_max.append(temp_max)

        temp_max = heights[-1]
        for height in reversed(heights):
            if height >= temp_max:
                right_max.append(height)
                temp_max = height
            else:
                right_max.append(temp_max)

        right_max = list(reversed(right_max))

        amount_rain_trapped = 0
        for i, height in enumerate(heights):
            amount_rain_trapped += min(left_max[i], right_max[i]) - height

        return amount_rain_trapped


sol = Solution()
sol.trapRainWater(heights=[0, 1, 0])
sol.trapRainWater(heights=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
