class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    # /O(nlogk), the best algorithm based on comparing
    # //算法时间复杂度要求到O(nlogk)，k为颜色个数
    # //这种算法的思想类似与quickSort与mergeSort结合
    # //quickSort的思想在于partition进行分割
    # //mergeSort的思想在于直接取中间（这里表现为取中间大小的数），分为左右两个相等长度的部分
    # //区别在于partition的判定条件变为了中间大小的元素而不是中间位置的元素
    # //因此等号的取值可以只去一边也不会有影响
    def sortColors2(self, colors, k):
        # write your code here
        if len(colors) == 0:
            return
        self.rainbow_sort(colors, 1, k, 0, len(colors) - 1)

    def rainbow_sort(self, colors, color_from, color_to, index_from, index_to):
        if color_from == color_to or index_from == index_to:
            return
        # 区别在于partition的判定条件变为了中间大小的元素而不是中间位置的元素
        pivot = (color_to + color_from) // 2

        left = index_from
        right = index_to
        while left <= right:
            while left <= right and pivot >= colors[left]:
                left += 1
            # 等号的取值只去一边
            while left <= right and pivot < colors[right]:
                right -= 1

            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1

        self.rainbow_sort(colors, color_from, pivot, index_from, right)
        self.rainbow_sort(colors, pivot+1, color_to, left, index_to)
