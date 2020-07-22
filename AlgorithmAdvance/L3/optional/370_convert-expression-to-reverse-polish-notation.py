# 370. Convert Expression to Reverse Polish Notation
# 中文English
# Given a string array representing an expression, and return the
# Reverse Polish notation of this expression. (remove the parentheses)

# 370. 将表达式转换为逆波兰表达式
# 中文English
# 给定一个字符串数组，它代表一个表达式，返回该表达式的逆波兰表达式。（去掉括号）

#
# Example
# Example 1:
#
# Input: ["3", "-", "4", "+", "5"]
# Output: ["3", "4", "-", "5", "+"]
# Explanation: 3 - 4 + 5 = -1 + 5 = 4
#     3 4 - 5 + = -1 5 + = 4
# Example 2:
#
# Input: ["(", "5", "-", "6", ")", "*", "7"]
# Output: ["5","6","-","7","*"]
# Explanation: (5 - 6) * 7 = -1 * 7 = -7
#     5 6 - 7 * = -1 7 * = -7
# Clarification
# Definition of Reverse Polish Notation:
#
# https://en.wikipedia.org/wiki/Reverse_Polish_notation
# https://baike.baidu.com/item/逆波兰表达式/9841727?fr=aladdin


class Solution:
    """
    @param expression: A string array
    @return: The Reverse Polish notation of this expression
    """

    def convertToRPN(self, expression):
        stk = []
        RPN = []
        for s in expression:
            if s == '(':
                stk.append(s)
            elif s == ')':
                pos = stk[::-1].index('(')
                RPN += stk[::-1][:pos]
                stk = stk[:-pos - 1]
            elif s[0] in '1234567890':
                RPN.append(s)
            else:
                priority = self.getPriority(s)
                while len(stk) and self.getPriority(stk[-1]) >= priority:
                    RPN.append(stk[-1])
                    stk.pop()
                stk.append(s)
        RPN += stk[::-1]
        return RPN

    def getPriority(self, s):
        if s in '*/':
            return 3
        if s in '+-':
            return 2
        if s in '()':
            return 1
        return 0

sol =Solution()
sol.convertToRPN(["(", "5", "-", "6", ")", "*", "7"])