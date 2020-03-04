# 10. 字符串的不同排列
# 中文English
# 给出一个字符串，找到它的所有排列，注意同一个字符串不要打印两次。
#
# 样例 1：
# 输入："abb"
# 输出：
# ["abb", "bab", "bba"]
#
# 样例 2：
# 输入："aabb"
# 输出：
# ["aabb", "abab", "baba", "bbaa", "abba", "baab"]

class Solution:
    """
    @param str: A string
    @return: all permutations
    """

    def stringPermutation2(self, str):
        # write your code here
        if len(str) == 0:
            return [""]
        chars = list(sorted(str))
        selected = [False for _ in range(len(str))]
        rslt = []
        self.dfs_helper(chars, [], selected, rslt)
        return rslt

    def dfs_helper(self, chars, curr_path, selected, rslt):
        if len(curr_path) == len(chars):
            rslt.append(''.join(curr_path))
            return

        for i in range(len(chars)):
            if selected[i]:
                continue
            # a' a" b
            # => a' a" b => √
            # => a" a' b => x
            # 不能跳过一个a选下一个a
            if i > 0 and chars[i] == chars[i - 1] and not selected[i - 1]:
                continue

            # make changes
            selected[i] = True
            curr_path.append(chars[i])

            # 找到所有 permutation 开头的排列
            # 找到所有 "a" 开头的
            self.dfs_helper(chars, curr_path, selected, rslt)

            # backtracking
            curr_path.pop()
            selected[i] = False