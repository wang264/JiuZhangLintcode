# 427. 生成括号
# 给定 n，表示有 n 对括号, 请写一个函数以将其生成所有的括号组合，并返回组合结果。
#
# 样例 1:
# 输入: 3
# 输出: ["((()))", "(()())", "(())()", "()(())", "()()()"]
#
# 样例 2:
# 输入: 2
# 输出: ["()()", "(())"]

class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """

    def generateParenthesis(self, n):
        # write your code here
        if n == 0:
            return []
        rslt = []
        self.dfs_helper(n, 0, 0, [], rslt)
        return rslt

    # 如果当前右括号数量等于括号对数 n, 那么当前字符串即是一种组合, 放入解中.
    # 如果当前左括号数量等于括号对数 n, 那么当前字符串后续填充满右括号, 即是一种组合.
    # 如果当前左括号数量未超过n:
    # 如果左括号多于右括号, 那么此时可以添加一个左括号或右括号, 递归进入下一层
    # 如果左括号不多于右括号, 那么此时只能添加一个左括号, 递归进入下一层
    def dfs_helper(self, n, left, right, curr_path, rslt):
        """
        left: number of left parenthesis
        right: number of right parenthesis
        curr_path: current combination
        rslt: the results
        """
        if right > left:  # immediately not valid
            return
        if left == n and right == n:
            rslt.append(''.join(curr_path))
        if left < n:
            curr_path.append('(')
            self.dfs_helper(n, left+1, right, curr_path, rslt)
            curr_path.pop()
        if right < n:
            curr_path.append(')')
            self.dfs_helper(n, left, right+1, curr_path, rslt)
            curr_path.pop()