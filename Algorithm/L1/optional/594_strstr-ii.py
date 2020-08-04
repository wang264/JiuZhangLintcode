# 594. strStr II
# 中文English
# Implement strStr function in O(n + m) time.
#
# strStr return the first index of the target string in a source string. The length of the target string
# is m and the length of the source string is n.
# If target does not exist in source, just return -1.
#
# Example
# Example 1:
#
# Input：source = "abcdef"， target = "bcd"
# Output：1
# Explanation：
# The position of the first occurrence of a string is 1.
# Example 2:
#
# Input：source = "abcde"， target = "e"
# Output：4
# Explanation：
# The position of the first occurrence of a string is 4.

#
# 算法：HASH
# 字符串Hash可以通俗的理解为，把一个字符串转换为一个整数。
# 如果我们通过某种方法，将字符串转换为一个整数，就可以快速的判断两个字符串是否相同。
# 当然如果有不同的两个字符串同时Hash到一个整数，这样就比较麻烦了，所以我们希望构造这个Hash函数使得他们成为一个单射。
#
# 算法思路
# 给定一个字符串S,对于一个字符c我们规定id(c)=c-'a'+1
# hash[i]=(hash[i-1]*p+id(s[i]))%MOD
# p和MOD均为质数，并且要尽量大
#
# 代码思路
# 计算target的hash值
# 计算source的hash值的过程中，依次计算每targetLen位的hash值。
#     -假设target长度为2，source为“abcd”
#     -hash("cd") = (hash("bc + d") - hash("b")*2 ) % BASE
#
# 复杂度分析
# N表示字符串source长度，M表示字符串target长度
# 空间复杂度：O(1)
# 时间复杂度：O(N+M)


class Solution:
    # @param {string} source a source string
    # @param {string} target a target string
    # @return {int} an integer as index
    def strStr2(self, source, target):
        # Write your code here
        if source is None or target is None:
            return -1
        m = len(target)
        n = len(source)
        if m == 0:
            return 0
        BASE = 100007
        targetCode = 0
        power = 1
        # 先计算一下target的hash值
        for i in range(m):
            targetCode = (targetCode * 31 + ord(target[i]) - ord('a')) % BASE
            if targetCode < 0:
                targetCode += BASE

        for i in range(m - 1):
            power = power * 31 % BASE

        sourceCode = 0

        # 当source code 加上右边一个character，就要减掉左边的一个character
        for i in range(n):
            if i >= m:
                sourceCode = (sourceCode - power * (ord(source[i - m]) - ord('a'))) % BASE

            sourceCode = (sourceCode * 31 + ord(source[i]) - ord('a')) % BASE

            if sourceCode < 0:
                sourceCode += BASE

            # 若hash值相同，返回答案
            if i >= m - 1 and sourceCode == targetCode:
                return i - m + 1

        return -1
