# Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.
#
# You need to support the following method:
#
# connect(a, b), an edge to connect node a and node b
# query(a), Returns the number of connected component nodes which include node a.
# connect(a, b), 添加一条连接节点 a, b的边
# query(a), 返回图中含 a 的联通区域内节点个数
# 样例
# Example 1:
#
# Input:
# ConnectingGraph2(5)
# query(1)
# connect(1, 2)
# query(1)
# connect(2, 4)
# query(1)
# connect(1, 4)
# query(1)
# Output:[1,2,3,3]
# Example 2:
#
# Input:
# ConnectingGraph2(6)
# query(1)
# query(2)
# query(1)
# query(5)
# query(1)
#
# Output:
# [1,1,1,1,1]


class ConnectingGraph2:
    """
    @param: n: An integer
    """

    def __init__(self, n):  # 初始化
        self.father = {}
        self.size = {}
        for i in range(n + 1):
            self.father[i] = i
            self.size[i] = 1

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """

    def connect(self, a, b):  # 合并
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            # root_b is the father of root_a now
            self.father[root_a] = root_b
            self.size[root_b] += self.size[root_a]  # update the count for size that store in root_b.

    def query(self, a):  # 询问
        root = self.find(a)
        return self.size[root]

    def find(self, x):  # 查询
        if self.father[x] == x:
            return x

        root = x
        while self.father[root] != root:
            root = self.father[root]

        # path compression
        while x != root:
            temp = self.father[x]
            self.father[x] = root
            x = temp
        return x

    """
    #递归写法
    def find(self,x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    """
