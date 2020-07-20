# 找出有向图中的弱连通分量 · Find the Weak Connected Component in the Directed Graph
# Union Find
# LintCode 版权所有
# 描述
# Find the number Weak Connected Component in the directed graph. Each node in the graph contains a label and
# a list of its neighbors. (a weak connected component of a directed graph is a maximum subgraph in which
# any two vertices are connected by direct edge path.)
#
# Sort the elements of a component in ascending order.
# 样例
# Example 1:
#
# Input: {1,2,4#2,4#3,5#4#5#6,5}
# Output: [[1,2,4],[3,5,6]]
# Explanation:
#   1----->2    3-->5
#    \     |        ^
#     \    |        |
#      \   |        6
#       \  v
#        ->4
# Example 2:
#
# Input: {1,2#2,3#3,1}
# Output: [[1,2,3]]
# 说明
# graph model explaination:
# https://www.lintcode.com/help/graph
#
#
# 找出有向图中的弱连通分量 · Find the Weak Connected Component in the Directed Graph
# Union Find
# LintCode 版权所有
# 描述
# 请找出有向图中弱连通分量。图中的每个节点包含 1 个标签和1 个相邻节点列表。
# （有向图的弱连通分量是任意两点均有有向边相连的极大子图）
#
# 将连通分量内的元素升序排列。


print('same as 431')


