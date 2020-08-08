# 892. Alien Dictionary
# 中文English
# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you.
# You receive a list of non-empty words from the dictionary,
# where words are sorted lexicographically by the rules of this new language.
# Derive the order of letters in this language.
#
# Example
# Example 1:
#
# Input：["wrt","wrf","er","ett","rftt"]
# Output："wertf"
# Explanation：
# from "wrt"and"wrf" ,we can get 't'<'f'
# from "wrt"and"er" ,we can get 'w'<'e'
# from "er"and"ett" ,we can get 'r'<'t'
# from "ett"and"rftt" ,we can get 'e'<'r'
# So return "wertf"
#
# Example 2:
#
# Input：["z","x"]
# Output："zx"
# Explanation：
# from "z" and "x"，we can get 'z' < 'x'
# So return "zx"

# Notice
# 1.You may assume all letters are in lowercase.
# 2.The dictionary is invalid, if a is prefix of b and b is appear before a.
# 3.If the order is invalid, return an empty string.
# 4.There may be multiple valid order of letters, return the smallest in normal lexicographical order
#
# 892. 外星人词典
# 中文English
# 有一种新的使用拉丁字母的外来语言。但是，你不知道字母之间的顺序。你会从词典中收到一个非空的单词列表，其中的单词在这种
# 新语言的规则下按字典顺序排序。请推导出这种语言的字母顺序。
#
# Example
# 样例 1:
#
# 输入：["wrt","wrf","er","ett","rftt"]
# 输出："wertf"
# 解释：
# 从 "wrt"和"wrf" ,我们可以得到 't'<'f'
# 从 "wrt"和"er" ,我们可以得到'w'<'e'
# 从 "er"和"ett" ,我们可以得到 get 'r'<'t'
# 从 "ett"和"rftt" ,我们可以得到 'e'<'r'
# 所以返回 "wertf"
#
# 样例 2:
#
# 输入：["z","x"]
# 输出："zx"
# 解释：
# 从 "z" 和 "x"，我们可以得到 'z' < 'x'
# 所以返回"zx"
# Notice
# 1.你可以假设所有的字母都是小写。
# 2.如果a是b的前缀且b出现在a之前，那么这个顺序是无效的。
# 3.如果顺序是无效的，则返回空字符串。
# 4.这里可能有多个有效的字母顺序，返回以正常字典顺序看来最小的。

from heapq import heappush, heappop, heapify


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alienOrder(self, words):
        graph = self.build_graph(words)
        if not graph:
            return ""
        return self.topological_sort(graph)

    def build_graph(self, words):
        # key is node, value is neighbors
        graph = {}

        # initialize graph
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set()

        # add edges
        n = len(words)
        # compare each word with its next word in the alien dictionary
        for i in range(n - 1):
            min_len = min(len(words[i]), len(words[i + 1]))
            for j in range(min_len):
                # if jth character of word i is different from the j th character of word i+1
                if words[i][j] != words[i + 1][j]:
                    # add the directed edges words[i][j]< words[i+1][j]
                    graph[words[i][j]].add(words[i + 1][j])
                    break
                # last character
                if j == min_len - 1:
                    if len(words[i]) > len(words[i + 1]):
                        return None

        return graph

    def topological_sort(self, graph):
        # initialize indegree
        indegree = {node: 0 for node in graph}

        # calculate indegree
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1

        # use heapq instead of regular queue so that we can get the
        # smallest lexicographical order
        queue = [node for node in graph if indegree[node] == 0]
        heapify(queue)

        # regular bfs algorithm to do topological sorting
        topo_order = ""
        while queue:
            node = heappop(queue)
            topo_order += node
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    heappush(queue, neighbor)

        # if all nodes popped
        if len(topo_order) == len(graph):
            return topo_order

        return ""


sol = Solution()
assert sol.alienOrder(words=["abc", "ab"]) == ""
