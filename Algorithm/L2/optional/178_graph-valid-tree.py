# 算法：bfs

# 算法思路
# 一棵拥有n个节点的树有n-1条边，树是连通的，没有环的。
# 给定一个无向图让我们判断是否为树，我们只需要判断是否连通且无环即可。
# 我们可以从根节点出发向儿子节点进行广度优先搜索bfs，如果能遍历完所有的点，且没有环存在，那么说明这个无向图是树。
# 已知给定的边不重复，所以可以通过判断边数是否为(n - 1)条来判断是否无环。

# 代码思路
# 首先判断边数是否为(n - 1)条，若不是则返回false
# 然后从根节点开始进行bfs搜索

# 复杂度分析
# 假设有n个点，m条边。
# 用邻接矩阵存储n个点之间的边的关系，空间复杂度为O(n^2)。
# 建图时每条边都会访问 1 次，搜索时每个点都会被询问1次，时间复杂度为O(max(n, m))。

from collections import deque


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        # write your code here
        num_edges = len(edges)
        if num_edges != n - 1:
            return False
        # adjacent[i][j] = True means ith node and jth node is connected.
        adjacent = [[False] * n for _ in range(n)]
        for edge in edges:
            node_1, node_2 = edge
            adjacent[node_1][node_2] = adjacent[node_2][node_1] = True

        visited = set()
        # 0作为根结点，开始向下遍历
        visited.add(0)
        queue = deque([0])

        number_of_visited_node = 1
        while queue:
            node = queue.popleft()
            # find all it's neighbors
            for possible_neighbor in range(n):
                if adjacent[node][possible_neighbor] is False:
                    continue
                # if these two nodes are connected and not visited
                # 如果相邻且没有被访问过，说明是儿子，加入队列
                if possible_neighbor not in visited:
                    visited.add(possible_neighbor)
                    number_of_visited_node += 1
                    queue.append(possible_neighbor)

        if number_of_visited_node == n:
            return True
        else:
            return False
