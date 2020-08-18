# 121. Word Ladder II
# 中文English
# Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, output sequence in dictionary order.
# Transformation rule such that:
#
# 1. Only one letter can be changed at a time
# 2. Each intermediate word must exist in the dictionary

# Example
# Example 1:
#
# Input：start = "a"，end = "c"，dict =["a","b","c"]
# Output：[["a","c"]]
# Explanation：
# "a"->"c"

# Example 2:
#
# Input：start ="hit"，end = "cog"，dict =["hot","dot","dog","lot","log"]
# Output：[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
# Explanation：
# 1."hit"->"hot"->"dot"->"dog"->"cog"
# 2."hit"->"hot"->"lot"->"log"->"cog"
# The dictionary order of the first sequence is less than that of the second.

# Notice
# *. All words have the same length.
# *. All words contain only lowercase alphabetic characters.
# *. At least one solution exists.


class MyUndirectedGraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = list()

    def __repr__(self):
        return self.label

    def add_neighbor(self, neighbor_node):
        if neighbor_node not in self.neighbors:
            self.neighbors.append(neighbor_node)


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """

    def findLadders(self, start, end, dict):
        # write your code here

        start_node = self.build_graph_and_return_starting_node(start_label=start,
                                                               end_label=end,
                                                               dict=dict)
        rslt = []
        visited = set()
        dummy_node = MyUndirectedGraphNode("dummy")
        dummy_node.neighbors = [start_node]
        self.dfs_helper(dummy_node, [], rslt, visited, end)
        return rslt

    def dfs_helper(self, curr_node, curr_path, rslt, visited, target_label):

        if curr_node.label == target_label:
            # if this is the first answer
            if len(rslt) == 0:
                rslt.append(curr_path[:])
            else:
                # this answer is same length of the other one
                if len(curr_path) == len(rslt[0]):
                    rslt.append(curr_path[:])
                # this answer is of shorter length
                elif len(curr_path) < len(rslt[0]):
                    rslt.clear()
                    rslt.append(curr_path[:])
                else:
                    pass
        else:
            # not see the target yet, we continue our search.
            for neighbor_node in curr_node.neighbors:
                if neighbor_node in visited:
                    continue
                visited.add(neighbor_node)
                curr_path.append(neighbor_node.label)
                self.dfs_helper(neighbor_node, curr_path, rslt, visited, target_label)
                curr_path.pop()
                visited.remove(neighbor_node)

    # build the graph, and return
    def build_graph_and_return_starting_node(self, start_label, end_label, dict):
        label_to_node = {}
        word_set = set(dict)
        word_set.add(start_label)
        word_set.add(end_label)
        # build node
        for word in word_set:
            graph_node = MyUndirectedGraphNode(word)
            label_to_node[word] = graph_node
        # fix neighbor
        for word in word_set:
            node = label_to_node[word]
            for neighbor_label in self.find_all_possible_neighbors(word, word_set):
                neighbor_node = label_to_node[neighbor_label]
                node.add_neighbor(neighbor_node)

        return label_to_node[start_label]

    def find_all_possible_neighbors(self, word, word_set):
        rslt_list = []
        # change the word at index 'i'
        for i in range(len(word)):
            # change the word[i] to different char
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char == word[i]:
                    continue
                new_word = word[0:i] + char + word[i + 1:]
                if new_word in word_set:
                    rslt_list.append(new_word)
        return rslt_list


sol = Solution()
# sol.find_all_possible_neighbors(word='dog', word_set=["hot", "dot", "dog", "lot", "log", "hit", "cog"])
node = sol.build_graph_and_return_starting_node(start_label="hit", end_label="cog",
                                                dict=["hot", "dot", "dog", "lot", "log"])
sol.findLadders(start="hit", end="cog", dict=["hot", "dot", "dog", "lot", "log"])

# 算法：BFS+DFS
# 题目要求找出所有从start到end的最短转换序列，显然我们需要考虑bfs搜索最短路，路径中的下一跳都存在于字典内，由于都是小写字母，可以枚举当前字符串下一跳可能的所有字符串,对于字符串s,将他的每一位都用'a'-'z'替换一遍，判断被替换字母后的s是否存在于dict中,这样相比直接在dict中搜索下一跳可以有效的减少时间复杂度（如果直接找下一跳那么必须遍历dict）。跑完所有最短路径后再dfs将图转换为start--end的路径

# 1.先添加end到dict中，便于计算
# 2.先对start--end通过队列bfs计算出所有最短路
# 3.对于每个当前字符串用暴力替换每一位的字母，查找是否存在于dict中
# 4.通过dfs遍历所有最短路，打印出所有路径

# 复杂度分析
# 时间复杂度O((V+E))
# bfs O(V+E)遍历所有边 E（即当前字符串的下一跳）和点V，dfsO(size(dict))跑最后的最短路


# 空间复杂度O(size(dict)*k)
# 存每个字符串与下一跳字符串的集合以及最短路径

from collections import defaultdict
from collections import deque


class Solution2:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """

    def findLadders(self, start, end, dict):
        dict = set(dict)
        # 将end添加进dict,防止结果为[]
        dict.add(end)
        res = []
        # 记录单词下一步能转到的单词
        next_word_dict = defaultdict(list)

        # 记录到start距离
        distance = {}

        distance[start] = 0
        # bfs搜start--end的最短路径
        self.bfs(start, end, distance, next_word_dict, dict)
        # dfs输出距离最短的路径
        self.dfs([start], end, res, 0, distance, next_word_dict)
        return res
        # 暴力匹配,当前字符串修改一个字母后的新字符串存在于dict中

    def next_words(self, word, dict):
        ans = []
        for i in range(len(word)):
            # 97=ord('a')，123=ord('z')+1
            for j in range(97, 123):
                tmp = word[:i] + chr(j) + word[i + 1:]
                if tmp != word and tmp in dict:
                    ans.append(tmp)

        return ans

        # 求到start的距离

    def bfs(self, start, end, distance, next_word_dict, dict):
        q = deque()
        q.append(start)
        step = 0
        flag = False  # 标记是否找到结果
        while len(q) is not 0:
            step += 1
            n = len(q)
            for i in range(n):
                word = q[0]
                q.popleft()
                for nextword in self.next_words(word, dict):
                    next_word_dict[word].append(nextword)
                    # 当下一跳是end时，就可以结束搜索
                    if nextword == end:
                        flag = True
                    # 如果没被添加过，则进行添加
                    if nextword not in distance:
                        distance[nextword] = step
                        q.append(nextword)
            if flag:
                break

    # 遍历所有从start到end的路径
    def dfs(self, curr_path, end, res, step, distance, next_word_dict):
        if curr_path[-1] == end:
            res.append(curr_path)
            return
        for word in next_word_dict[curr_path[-1]]:
            if distance[word] == step + 1:
                self.dfs(curr_path + [word], end, res, step + 1, distance, next_word_dict)


sol = Solution2()
sol.findLadders(start="hit", end="cog", dict=["hot", "dot", "dog", "lot", "log"])
