# 74. First Bad Version
# 中文English
# The code base version is an integer start from 1 to n. One day, someone committed a bad version in the code case, so it caused this version and the following versions are all failed in the unit tests. Find the first bad version.
#
# You can call isBadVersion to help you determine which version is the first bad one. The details interface can be found in the code's annotation part.
#
# Example
# Given n = 5:
#
#     isBadVersion(3) -> false
#     isBadVersion(5) -> true
#     isBadVersion(4) -> true
#
# Here we are 100% sure that the 4th version is the first bad version.
# Challenge
# You should call isBadVersion as few as possible.
#
# Notice
# Please read the annotation in code area to get the correct way to call isBadVersion in different language. For example, Java is SVNRepo.isBadVersion(v)


# class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
# bad version.
class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """

    def findFirstBadVersion(self, n):
        left = 1
        right = n
        while left + 1 < right:
            mid = (left + right) // 2
            if SVNRepo.isBadVersion(mid):
                right = mid
            else:
                left = mid

        if SVNRepo.isBadVersion(left):
            return left
        else:
            return right