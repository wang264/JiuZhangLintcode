class Solution:
    """
    使用分治法来解决。
    传入两个区间，一个是颜色区间 color_from, color_to。另外一个是待排序的数组区间 index_from, index_to.
    找到颜色区间的中点，将数组范围内进行 partition，<= color 的去左边，>color 的去右边。
    然后继续递归。
    时间复杂度 O(nlogk)O(nlogk) n是数的个数， k 是颜色数目。这是基于比较的算法的最优时间复杂度。

    不基于比较的话，可以用计数排序（Counting Sort）
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        self.sort_helper(colors, 1, k, 0, len(colors)-1)

    def sort_helper(self, colors, color_from, color_to, index_from, index_to):
        if color_from == color_to or index_from == index_to:
            return

        color = (color_from + color_to)//2

        left, right = index_from, index_to

        while left < right:
            while left < right and colors[left] <= color:
                left += 1
            while left < right and colors[right] > color:
                right -= 1

            if left < right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1

        self.sort_helper(colors, color_from, color, index_from, right)
        self.sort_helper(colors, color+1, color_to, left, index_to)

sol = Solution()
l = [2,1,1,2,2]
sol.sortColors2(l, 2)
l



