# 600. Smallest Rectangle Enclosing Black Pixels
# 中文English
# An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel.
# The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and
# vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned)
# rectangle that encloses all black pixels.
#
# Example
# Example 1:
#
# Input：["0010","0110","0100"]，x=0，y=2
# Output：6
# Explanation：
# The upper left coordinate of the matrix is (0,1), and the lower right coordinate is (2,2).
# Example 2:
#
# Input：["1110","1100","0000","0000"], x = 0, y = 1
# Output：6
# Explanation：
# The upper left coordinate of the matrix is (0, 0), and the lower right coordinate is (1,2).

# 600. 包裹黑色像素点的最小矩形
# 中文English
# 一个由二进制矩阵表示的图，0 表示白色像素点，1 表示黑色像素点。黑色像素点是联通的，即只有一块黑色区域。
# 像素是水平和竖直连接的，给一个黑色像素点的坐标 (x, y) ，返回囊括所有黑色像素点的矩阵的最小面积。
#
# Example
# 样例 1:
#
# 输入：["0010","0110","0100"]，x=0，y=2
# 输出：6
# 解释：
# 矩阵左上角坐标是(0, 1), 右下角的坐标是(2, 2)
# 样例 2:
#
# 输入：["1110","1100","0000","0000"], x = 0, y = 1
# 输出：6
# 解释：
# 矩阵左上角坐标是(0,  0), 右下角坐标是(1, 3)

from collections import deque

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Solution_BFS:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """

    def is_valid(self, image, x, y):
        num_rows = len(image)
        num_cols = len(image[0])
        return 0 <= x < num_rows and 0 <= y < num_cols

    def is_black_dot(self, image, x, y):
        return image[x][y] == '1'

    def minArea(self, image, x, y):
        # write your code here
        image = [list(row) for row in image]
        queue = deque([(x, y)])
        visited = set()
        upper, lower, left, right = y, y, x, x
        while len(queue) != 0:
            x, y = queue.popleft()
            visited.add((x, y))
            if x < left:
                left = x
            if x > right:
                right = x
            if y > lower:
                lower = y
            if y < upper:
                upper = y
            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                # not out of bound & is black dot & never visited that location before
                if self.is_valid(image, new_x, new_y) and self.is_black_dot(image, new_x, new_y) and (
                        (new_x, new_y) not in visited):
                    queue.append((new_x, new_y))

        height = lower - upper + 1
        width = right - left + 1
        area = height * width

        return area


sol_bfs = Solution_BFS()
sol_bfs.minArea(image=["0010", "0110", "0100"], x=0, y=1)


# 算法：二分
# 关于BFS和DFS
# BFS和DFS的做法就是遍历这个黑色像素连通块，得到各个方向上的坐标极值，时间复杂度O(K)，K为黑色像素点个数，这种做法在黑色像素点数量巨大时效率极低。
# 另外关于BFS和DFS如何选择，这里建议使用BFS，因为DFS会占用大量的系统栈，空间复杂度上要劣于BFS
# 下面我们来介绍一种在大部分情况下空间和时间上均优于DFS和BFS的算法——二分
# 算法思路
# 二分找到四个方向上黑色像素点出现的坐标极值
# 代码思路
# 这边以二分最左侧黑色像素为例
# 设置左指针为0，右指针为y，因为我们保证y列上存在黑色像素，最左侧黑色像素所在列一定在y或者其左侧
# 若mid所在列存在黑色像素，说明最左侧黑色像素在mid列或者其左侧，r = mid，否则l = mid
# 判断l列是否存在黑色像素，若存在则left = l，否则left = r。注意一定要先判l列，因为r可能存在黑色像素，但并不是最左侧
# 以此类推继续找到最右侧，最上侧，最下侧的黑色像素所在列或行
# 计算面积(right - left + 1) * (bottom - top + 1)并将其返回
# 这里提一种优化，找到最左处和最右处的黑色像素位置left和right后，在找最上和最下坐标时，对于行的判断只需要扫描[row,left]到[row,right]即可
# 复杂度分析
# 空间复杂度：O(1)
# 时间复杂度：O(MlogN+NlogM)（最坏情况）
# 最坏情况即只有一个黑色像素点，那么每次判断列上或行上是否又黑色像素点需要扫描完整列或整行
# 二分的做法当遇到黑色像素点很少且给出的矩阵很大时效率会变得极低，而此时BFS的效率会相对高很多
# 后记
# 能否做到在任何情况下效率都显得相对较高呢？我们可以设定一个阈值cnt，先进行BFS遍历，当遍历次数达到cnt时改用二分法进行计算

class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """

    def minArea(self, image, x, y):
        n = len(image)
        if n == 0:
            return 0
        m = len(image[0])
        if m == 0:
            return 0
        # 二分最左侧黑色像素坐标
        l = 0
        r = y
        while l + 1 < r:
            mid = l + (r - l) // 2
            # 若mid所在列存在黑色像素，说明最左侧黑色像素在mid列或者其左侧，r = mid
            if self.check_column(image, mid):
                r = mid
            # 若mid所在列不存在黑色像素，说明最左侧黑色像素在mid列的右侧，l = mid
            else:
                l = mid
        if self.check_column(image, l):
            left = l
        else:
            left = r

        # 二分最右侧黑色像素坐标
        l = y
        r = m - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if self.check_column(image, mid):
                l = mid
            else:
                r = mid
        if self.check_column(image, r):
            right = r
        else:
            right = l

        # 二分最上侧黑色像素坐标
        l = 0
        r = x
        while l + 1 < r:
            mid = l + (r - l) // 2
            if self.check_row(image, mid, left, right):
                r = mid
            else:
                l = mid
        if self.check_row(image, l, left, right):
            top = l
        else:
            top = r
        l = x
        r = n - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if self.check_row(image, mid, left, right):
                l = mid
            else:
                r = mid
        if self.check_row(image, r, left, right):
            bottom = r
        else:
            bottom = l
        return (right - left + 1) * (bottom - top + 1)

    # 判断列上是否存在黑色像素
    def check_column(self, image, col):
        for i in range(len(image)):
            if image[i][col] == '1':
                return True
        return False

    # 判断行上是否存在黑色像素
    def check_row(self, image, row, left, right):
        for j in range(left, right + 1):
            if image[row][j] == '1':
                return True
        return False

sol = Solution()
sol.minArea(image=["0010", "0110", "0100"], x=0, y=1)
