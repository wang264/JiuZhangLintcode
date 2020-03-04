# 652. 因式分解
# 中文English
# 一个非负数可以被视为其因数的乘积。编写一个函数来返回整数 n 的因数所有可能组合。#

# 样例1
# 输入：8
# 输出： [[2,2,2],[2,4]]
# 解释： 8 = 2 x 2 x 2 = 2 x 4

# 样例2
# 输入：1
# 输出： []

# 注意事项
# 组合中的元素(a1,a2,...,ak)必须是非降序。(即，a1≤a2≤...≤ak)。
# 结果集中不能包含重复的组合。
class Solution:
    # @param {int} n an integer
    # @return {int[][]} a list of combination
    def getFactors(self, n):
        # write your code here
        result = []
        self.helper(result, [], n, 2)
        return result

    # 用 n=8作爲例子。
    def helper(self, result, item, n, start):
        # if len(item)>1 是爲了不要 【8】
        # n=1 代表拆分完畢
        if n == 1 and len(item) > 1:
            result.append(item[:])
            return

        import math
        for i in range(start, int(math.sqrt(n)) + 1):
            if n % i == 0:
                item.append(i)
                self.helper(result, item, n // i, i)
                item.pop()
        # 爲了在【2，2，2】的同時拿到【2，4】
        if n >= start:
            item.append(n)
            self.helper(result, item, 1, n)
            item.pop()
