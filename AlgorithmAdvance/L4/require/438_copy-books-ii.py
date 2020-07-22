#
# 438: 书籍复印 II · Copy Books II
# LintCode 版权所有
# 动态规划
# 二分法
# 描述
# Given n books and each book has the same number of pages. There are k persons to copy these books and the i-th person needs times[i] minutes to copy a book.
#
# Each person can copy any number of books and they start copying at the same time. What's the best strategy to assign books so that the job can be finished at the earliest time?
#
# Return the shortest time.
#
# 样例
# Example 1:
#
# Input: n = 4, times = [3, 2, 4]
# Output: 4
# Explanation:
#     First person spends 3 minutes to copy 1 book.
#     Second person spends 4 minutes to copy 2 books.
#     Third person spends 4 minutes to copy 1 book.
# Example 2:
#
# Input: n = 4, times = [3, 2, 4, 5]
# Output: 4
# Explanation: Use the same strategy as example 1 and the forth person does nothing.

# 描述
# 给定 n 本书, 每本书具有相同的页数. 现在有 k 个人来复印这些书. 其中第 i 个人需要 times[i]
# 分钟来复印一本书. 每个人可以复印任意数量的书. 怎样分配这 k 个人的任务, 使得这 n 本书能够被尽快复印完?
#
# 返回完成复印任务最少需要的分钟数.
#
# 样例
# 样例 1:
#
# 输入: n = 4, times = [3, 2, 4]
# 输出: 4
# 解释: 第一个人复印 1 本书, 花费 3 分钟. 第二个人复印 2 本书, 花费 4 分钟. 第三个人复印 1 本书, 花费 4 分钟.
# 样例 2:
#
# 输入: n = 4, times = [3, 2, 4, 5]
# 输出: 4
# 解释: 使用与样例 1相同的策略, 第四个人不参与复印.


class Solution:
    """
    @param n: An integer
    @param times: an array of integers
    @return: an integer
    """

    # 二分答案
    # 如果能在 x 分钟内分完 n 本书 ---> 那正确答案是x或者小于x
    # 如果不能在x 分钟内分完 n 本书 ---> 那正确答案一定大于x

    def can_copy(self, num_books_need_copy, reading_speeds, time_limit):
        books_copied = 0
        for reading_speed in reading_speeds:
            books_copied += time_limit / reading_speed
        if books_copied >= num_books_need_copy:
            return True
        else:
            return False

    def copyBooksII(self, n, times):
        left = 1  # 最少需要1分钟
        right = max(times) * n  # 最多需要的时间，其他人不干活。就让那个干的最慢的干活。
        while left + 1 < right:
            mid = (left + right) // 2
            # 如果能在 x 分钟内分完 n 本书 ---> 那正确答案是x或者小于x
            if self.can_copy(num_books_need_copy=n, reading_speeds=times, time_limit=mid):
                right = mid
            # 如果不能在x 分钟内分完 n 本书 ---> 那正确答案一定大于x
            else:
                left = mid

        # 答案一定在Left或者Right中。优先返回Left
        if self.can_copy(n, times, time_limit=left):
            return left
        else:
            return right


sol = Solution()
sol.copyBooksII(4, [3, 2, 4])
sol.copyBooksII(4, [3, 2, 4, 5])