# 437. Copy Books
# 中文English
# Given n books and the i-th book has pages[i] pages. There are k persons to copy these books.
#
# These books list in a row and each person can claim a continous range of books.
# For example, one copier can copy the books from i-th to j-th continously,
# but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).
# They start copying books at the same time and they all cost 1 minute to copy 1 page of a book.
# What's the best strategy to assign books so that the slowest copier can finish at earliest time?
#
# Return the shortest time that the slowest copier spends.
#
# Example
# Example 1:
#
# Input: pages = [3, 2, 4], k = 2
# Output: 5
# Explanation:
#     First person spends 5 minutes to copy book 1 and book 2.
#     Second person spends 4 minutes to copy book 3.
# Example 2:
#
# Input: pages = [3, 2, 4], k = 3
# Output: 4
# Explanation: Each person copies one of the books.
# Challenge
# O(nk) time
#
# Notice
# The sum of book pages is less than or equal to 2147483647
#
# 437. 书籍复印
# 中文English
# 给定 n 本书, 第 i 本书的页数为 pages[i]. 现在有 k 个人来复印这些书籍, 而每个人只能复印编号连续的一段的书,
# 比如一个人可以复印 pages[0], pages[1], pages[2], 但是不可以只复印 pages[0], pages[2], pages[3] 而不复印 pages[1].
# 所有人复印的速度是一样的, 复印一页需要花费一分钟, 并且所有人同时开始复印.
# 怎样分配这 k 个人的任务, 使得这 n 本书能够被尽快复印完?
# 返回完成复印任务最少需要的分钟数.
#
# Example
# 样例 1:
#
# 输入: pages = [3, 2, 4], k = 2
# 输出: 5
# 解释: 第一个人复印前两本书, 耗时 5 分钟. 第二个人复印第三本书, 耗时 4 分钟.
# 样例 2:
#
# 输入: pages = [3, 2, 4], k = 3
# 输出: 4
# 解释: 三个人各复印一本书.
# Challenge
# 时间复杂度 O(nk)
#
# Notice
# 书籍页数总和小于等于2147483647
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """

    # greedy algorithm
    # get at the number of people needed if we need to finish copy all the books in time_limit minutes.
    def get_least_people(self, pages, time_limit):
        count = 0
        time_cost = 0
        for page in pages:
            if time_cost + page > time_limit:
                count += 1
                time_cost = 0
            time_cost += page

        return count + 1

    def copyBooks(self, pages, k):
        left = max(pages)
        right = sum(pages)
        while left + 1 < right:
            mid = (left + right) / 2
            # if the people needed is less than K, means that we could be more efficient. the time it take should be
            # even less.
            if self.get_least_people(pages, mid) <= k:
                right = mid
            # if the people needed is larger of equal to K, means that to achieve the same task with only K people,
            # we need to give them more time.
            else:
                left = mid

        if self.get_least_people(pages, left) <= k:
            return left
        else:
            return right
