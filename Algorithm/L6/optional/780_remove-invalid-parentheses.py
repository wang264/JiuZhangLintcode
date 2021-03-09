# 780. Remove Invalid Parentheses
# 中文English
# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
#
# Example
# Example 1:
#
# Input:
# "()())()"
# Ouput:
# ["(())()","()()()"]
# Example 2:
#
# Input:
# "(a)())()"
# Output:
#  ["(a)()()", "(a())()"]
# Example 3:
#
# Input:
# ")("
# Output:
#  [""]
# Notice
# The input string may contain letters other than the parentheses ( and ).

# 算法：bfs
#
# 删除最小数目的无效括号，使得输入字符串有效，那么我们考虑一个个地去删除字符，直到出现有效字符串
#
# 1.用队列维护bfs
# 2.每次取队头进行check
# 3.如果队头元素是有效字符串，那么没必要去bfs更短的串，用一个flag标记continue
# 4.如果依然无效字符串，对于这个字符串，删除其中一位压入队列
# 5.用一个set做剪枝，对于已经check过的字符串，直接跳过，
# 6.check函数用来判断是否有效，用一个count记录'（'和'）'的个数遇到'('则count++反之则count--，若中途出现count小于0的情况，则说明字符串无效，若最后count！=0则字符串无效
#  复杂度分析
#
# 时间复杂度O(n^2)
# n为字符串长度，最坏情况复杂度为m^2

# 空间复杂度O(n^2)
# n为字符串长度

from collections import deque


class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """

    def removeInvalidParentheses(self, s):
        # Write your code here
        rslt = []
        if len(s) == 0:
            rslt.append("")
            return rslt
        q = deque([])
        S = set()
        q.append(s)
        S.add(s)
        flag = False

        # bfs
        while len(q) > 0:
            curr_str = q.popleft()
            # curr_str，则找到答案
            if self.is_valid(curr_str):
                rslt.append(curr_str)
                flag = True
            # 不需要去找更短的串
            if flag:
                continue

            # 对于无效的字符串，依次删除一个字符压入队列
            for i in range(len(curr_str)):
                if curr_str[i] != '(' and curr_str[i] != ')':
                    continue
                str1 = curr_str[:i]
                str2 = curr_str[i + 1:]
                str3 = str1 + str2
                # 如果这个字符串未被check过，则压入队列
                if str3 not in S:
                    S.add(str3)
                    q.append(str3)

        return rslt

    def is_valid(self, s):
        # 记录count对
        count = 0
        for char in s:
            if char == '(':
                count += 1
            if char == ')':
                count -= 1
            if count < 0:
                return False
        if count == 0:
            return True
        else:
            return False

sol= Solution()
sol.removeInvalidParentheses(s="(a)())()")